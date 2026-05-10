"""Main entry point — CLI orchestrator."""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
import uuid
from pathlib import Path

from . import __version__
from .audit import (
    audit_discovery_complete,
    audit_run_end,
    audit_run_start,
    audit_thread_failed,
    audit_thread_fetched,
)
from .auth import get_session_token, load_token, save_token
from .checkpoint import (
    load_checkpoint,
    mark_discovery_complete,
    mark_thread_processed,
    save_checkpoint,
)
from .config import ExporterConfig
from .discovery import discover_all_threads
from .fetch import fetch_thread
from .http import AuthError, HTTPClient, HTTPError, RateLimiter
from .manifest import add_entry, create_manifest, save_manifest
from .render import render_thread, slugify_filename
from .types import ManifestEntry, ThreadStub

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("pplx_exporter")


def main() -> None:
    """CLI entry point."""
    args = parse_args()
    config = ExporterConfig(
        output_dir=Path(args.output).resolve(),
        headless=args.headless,
        rate_limit_ms=args.rate_limit,
        batch_size=args.batch_size,
    )
    config.retry.max_retries = args.max_retries

    try:
        asyncio.run(run_export(config))
    except KeyboardInterrupt:
        logger.info("Interrupted — checkpoint saved, safe to resume")
        sys.exit(130)
    except AuthError as exc:
        logger.error("Auth failed: %s", exc)
        logger.info("Delete %s and re-run to re-authenticate", config.token_path)
        sys.exit(1)


async def run_export(config: ExporterConfig) -> None:
    """Main export orchestration."""
    config.output_dir.mkdir(parents=True, exist_ok=True)

    # Auth
    token = load_token(config.token_path)
    if not token:
        logger.info("No saved session — launching browser for login...")
        token = await get_session_token(config.browser_data_dir, headless=config.headless)
        save_token(token, config.token_path)
        logger.info("Token saved to %s", config.token_path)

    # HTTP client
    rate_limiter = RateLimiter(config.rate_limit_ms)
    client = HTTPClient(session_token=token, rate_limiter=rate_limiter, retry_config=config.retry)

    # Checkpoint
    checkpoint = load_checkpoint(config.checkpoint_path)
    run_id = checkpoint.run_id or str(uuid.uuid4())[:8]
    checkpoint.run_id = run_id

    audit_run_start(config.audit_log_path, run_id)
    logger.info("Export run %s started (v%s)", run_id, __version__)

    # Discovery
    if checkpoint.discovery_completed and checkpoint.discovered_threads:
        logger.info("Resuming — %d threads from checkpoint, %d already processed",
                    len(checkpoint.discovered_threads), len(checkpoint.processed_slugs))
        threads = [_dict_to_stub(d) for d in checkpoint.discovered_threads]
    else:
        logger.info("Starting discovery...")
        threads = await discover_all_threads(client, batch_size=config.batch_size)
        mark_discovery_complete(checkpoint, threads)
        save_checkpoint(checkpoint, config.checkpoint_path)
        audit_discovery_complete(config.audit_log_path, len(threads))
        logger.info("Discovered %d threads", len(threads))

    # Filter already-processed
    pending = [t for t in threads if t.slug not in set(checkpoint.processed_slugs)]
    logger.info("Threads to fetch: %d (skipping %d already done)", len(pending), len(threads) - len(pending))

    # Fetch + render
    manifest = create_manifest(run_id)
    exported = 0

    for i, stub in enumerate(pending, 1):
        logger.info("[%d/%d] Fetching: %s", i, len(pending), stub.title[:60])

        try:
            thread_data = await fetch_thread(client, stub.slug)
        except (HTTPError, AuthError) as exc:
            logger.error("Failed to fetch %s: %s", stub.slug, exc)
            audit_thread_failed(config.audit_log_path, stub.slug, str(exc), 0)
            if isinstance(exc, AuthError):
                raise
            continue

        # Render and save
        markdown, sha, byte_count = render_thread(thread_data)

        space_dir = slugify_filename(thread_data.space or "unsorted")
        thread_dir = config.output_dir / space_dir
        thread_dir.mkdir(parents=True, exist_ok=True)

        filename = slugify_filename(thread_data.title)
        md_path = thread_dir / f"{filename}.md"
        json_path = thread_dir / f"{filename}.json"

        md_path.write_text(markdown, encoding="utf-8")
        json_path.write_text(
            json.dumps(thread_data.raw, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        # Manifest + audit
        rel_path = str(md_path.relative_to(config.output_dir))
        add_entry(manifest, ManifestEntry(
            slug=stub.slug,
            title=thread_data.title,
            space=thread_data.space,
            file_path=rel_path,
            byte_count=byte_count,
            sha256=sha,
            created_at=thread_data.created_at,
            updated_at=thread_data.updated_at,
        ))
        audit_thread_fetched(config.audit_log_path, stub.slug, byte_count, sha)

        # Checkpoint after each thread
        mark_thread_processed(checkpoint, stub.slug)
        save_checkpoint(checkpoint, config.checkpoint_path)
        exported += 1

    # Finalise
    save_manifest(manifest, config.manifest_path)
    audit_run_end(config.audit_log_path, run_id, exported)
    await client.close()

    logger.info("Export complete: %d threads exported to %s", exported, config.output_dir)
    logger.info("Manifest: %s | Audit: %s", config.manifest_path, config.audit_log_path)


def _dict_to_stub(d: dict) -> ThreadStub:
    return ThreadStub(
        slug=d["slug"],
        title=d.get("title", ""),
        space=d.get("space"),
        space_uuid=d.get("space_uuid"),
        last_query_datetime=d.get("last_query_datetime", ""),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pplx-export",
        description="Export Perplexity conversations to Markdown + JSON",
    )
    parser.add_argument("-o", "--output", default="./pplx-export", help="Output directory")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode")
    parser.add_argument("--rate-limit", type=int, default=1500, help="Ms between requests (default: 1500)")
    parser.add_argument("--batch-size", type=int, default=20, help="Threads per discovery batch (default: 20)")
    parser.add_argument("--max-retries", type=int, default=5, help="Max retries on failure (default: 5)")
    parser.add_argument("--token", type=str, default=None, help="Session token (skip browser login)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser.parse_args()


if __name__ == "__main__":
    main()
