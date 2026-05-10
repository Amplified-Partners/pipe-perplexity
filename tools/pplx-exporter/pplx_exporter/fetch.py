"""Thread fetch — retrieve full conversation data with cursor pagination."""

from __future__ import annotations

import logging
from typing import Any

from .config import API_VERSION, THREAD_ENDPOINT
from .http import HTTPClient
from .types import Entry, ThreadData

logger = logging.getLogger(__name__)

SUPPORTED_BLOCK_USE_CASES = [
    "refinement_filters",
    "canvas_mode",
    "maps_preview",
    "answer_tabs",
    "price_comparison_widgets",
]


async def fetch_thread(client: HTTPClient, slug: str) -> ThreadData:
    """Fetch a complete thread with all entries via cursor pagination.

    First request uses limit=10 (basic metadata), subsequent pages use limit=100.
    Follows the exact pattern from the Perplexity-to-Obsidian extension.
    """
    entries: list[Entry] = []
    seen_uuids: set[str] = set()
    cursor: str | None = None
    is_first = True
    thread_title = ""
    collection_title: str | None = None
    collection_uuid: str | None = None
    thread_metadata: dict[str, Any] = {}
    seen_cursors: set[str] = set()

    while True:
        params: dict[str, Any] = {
            "with_parent_info": "true",
            "with_schematized_response": "true",
            "version": API_VERSION,
            "source": "default",
            "offset": "0",
            "from_first": "true",
        }

        for use_case in SUPPORTED_BLOCK_USE_CASES:
            params.setdefault("supported_block_use_cases", [])

        limit = 10 if is_first else 100
        params["limit"] = str(limit)
        if cursor:
            params["cursor"] = cursor

        query_string = _build_query_string(params)
        path = f"{THREAD_ENDPOINT}/{slug}?{query_string}"

        data: dict[str, Any] = await client.get(path)

        if data.get("status") != "success":
            logger.error("Thread fetch failed for %s: status=%s", slug, data.get("status"))
            break

        if not collection_title and data.get("collection_info"):
            info = data["collection_info"]
            collection_title = info.get("title")
            collection_uuid = info.get("uuid")

        if not thread_metadata and data.get("thread_metadata"):
            thread_metadata = data["thread_metadata"]

        raw_entries = data.get("entries", [])
        for raw_entry in raw_entries:
            uuid = raw_entry.get("uuid", "")
            if uuid and uuid in seen_uuids:
                continue
            if uuid:
                seen_uuids.add(uuid)

            entry = _parse_entry(raw_entry)
            entries.append(entry)

        next_cursor = data.get("next_cursor")
        if not next_cursor:
            break

        cursor_str = str(next_cursor) if not isinstance(next_cursor, str) else next_cursor
        if cursor_str in seen_cursors:
            logger.warning("Repeated cursor for %s — stopping pagination", slug)
            break
        seen_cursors.add(cursor_str)
        cursor = cursor_str
        is_first = False

    if not thread_title and thread_metadata:
        thread_title = thread_metadata.get("title", "")

    created_at = thread_metadata.get("created_datetime", "")
    updated_at = thread_metadata.get("updated_datetime", "")
    if not updated_at and entries:
        updated_at = entries[-1].updated_at

    return ThreadData(
        slug=slug,
        title=thread_title or (entries[0].query[:80] if entries else slug),
        entries=entries,
        space=collection_title,
        space_uuid=collection_uuid,
        created_at=created_at,
        updated_at=updated_at,
        raw=data,
    )


def _build_query_string(params: dict[str, Any]) -> str:
    """Build URL query string, handling repeated keys for arrays."""
    parts: list[str] = []
    for key, value in params.items():
        if isinstance(value, list):
            for item in value:
                parts.append(f"{key}={item}")
        else:
            parts.append(f"{key}={value}")
    return "&".join(parts)


def _parse_entry(raw: dict[str, Any]) -> Entry:
    """Parse a single entry from API response."""
    query = raw.get("query_str", "")
    updated_at = raw.get("updated_datetime", "")

    answer_parts: list[str] = []
    sources: list[dict[str, str]] = []

    blocks = raw.get("blocks", [])
    for block in blocks:
        md = block.get("markdown_answer", "")
        if md:
            answer_parts.append(md)

        block_sources = block.get("web_results", []) or block.get("sources", [])
        for src in block_sources:
            sources.append({
                "title": src.get("title", ""),
                "url": src.get("url", ""),
                "snippet": src.get("snippet", ""),
            })

    return Entry(
        query=query,
        answer="\n\n".join(answer_parts),
        sources=sources,
        updated_at=updated_at,
    )
