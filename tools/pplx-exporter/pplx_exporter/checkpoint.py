"""Checkpoint — save/load state for resumability."""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .types import Checkpoint, ThreadStub

logger = logging.getLogger(__name__)


def load_checkpoint(path: Path) -> Checkpoint:
    """Load checkpoint from disk. Returns fresh checkpoint if file missing or corrupt."""
    if not path.exists():
        return Checkpoint()

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return Checkpoint(
            processed_slugs=data.get("processed_slugs", []),
            discovery_completed=data.get("discovery_completed", False),
            discovered_threads=data.get("discovered_threads", []),
            last_updated=data.get("last_updated", ""),
            run_id=data.get("run_id", ""),
        )
    except (json.JSONDecodeError, KeyError) as exc:
        logger.warning("Corrupt checkpoint, starting fresh: %s", exc)
        return Checkpoint()


def save_checkpoint(checkpoint: Checkpoint, path: Path) -> None:
    """Persist checkpoint to disk."""
    checkpoint.last_updated = datetime.now(UTC).isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_checkpoint_to_dict(checkpoint), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def mark_discovery_complete(checkpoint: Checkpoint, threads: list[ThreadStub]) -> None:
    """Mark discovery phase complete with the discovered thread list."""
    checkpoint.discovery_completed = True
    checkpoint.discovered_threads = [_stub_to_dict(t) for t in threads]


def mark_thread_processed(checkpoint: Checkpoint, slug: str) -> None:
    """Record a thread as successfully processed."""
    if slug not in checkpoint.processed_slugs:
        checkpoint.processed_slugs.append(slug)


def _checkpoint_to_dict(cp: Checkpoint) -> dict[str, Any]:
    return {
        "processed_slugs": cp.processed_slugs,
        "discovery_completed": cp.discovery_completed,
        "discovered_threads": cp.discovered_threads,
        "last_updated": cp.last_updated,
        "run_id": cp.run_id,
    }


def _stub_to_dict(stub: ThreadStub) -> dict[str, Any]:
    return {
        "slug": stub.slug,
        "title": stub.title,
        "space": stub.space,
        "space_uuid": stub.space_uuid,
        "last_query_datetime": stub.last_query_datetime,
    }
