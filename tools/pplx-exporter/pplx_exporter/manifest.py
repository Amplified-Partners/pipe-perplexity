"""Manifest — summary of export run."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .types import ManifestEntry


def create_manifest(run_id: str) -> dict[str, Any]:
    return {
        "export_run_id": run_id,
        "export_timestamp": datetime.now(UTC).isoformat(),
        "tool_version": "0.1.0",
        "total_threads": 0,
        "threads": [],
    }


def add_entry(manifest: dict[str, Any], entry: ManifestEntry) -> None:
    manifest["threads"].append({
        "slug": entry.slug,
        "title": entry.title,
        "space": entry.space,
        "file_path": entry.file_path,
        "byte_count": entry.byte_count,
        "sha256": entry.sha256,
        "created_at": entry.created_at,
        "updated_at": entry.updated_at,
    })
    manifest["total_threads"] = len(manifest["threads"])


def save_manifest(manifest: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
