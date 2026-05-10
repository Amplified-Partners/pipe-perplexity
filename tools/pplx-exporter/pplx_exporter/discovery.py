"""Thread discovery — paginated list of all conversations."""

from __future__ import annotations

import logging
from typing import Any

from .config import API_VERSION, DISCOVERY_ENDPOINT
from .http import HTTPClient
from .types import ThreadStub

logger = logging.getLogger(__name__)


async def discover_all_threads(
    client: HTTPClient,
    batch_size: int = 20,
) -> list[ThreadStub]:
    """Discover all threads via paginated POST to list_ask_threads.

    Uses offset-based pagination. Stops when the API returns fewer results
    than the batch size or when has_next_page is False.
    """
    threads: list[ThreadStub] = []
    offset = 0
    seen_slugs: set[str] = set()
    empty_batches = 0

    while True:  # noqa: PLW0120
        body = {
            "limit": batch_size,
            "ascending": False,
            "offset": offset,
            "search_term": "",
        }

        url = f"{DISCOVERY_ENDPOINT}?version={API_VERSION}&source=default"
        data: Any = await client.post(url, json_body=body)

        if not data or not isinstance(data, list):
            empty_batches += 1
            if empty_batches >= 2:
                break
            offset += batch_size
            continue

        empty_batches = 0
        batch_count = 0

        for item in data:
            slug = item.get("slug", "")
            if not slug or slug in seen_slugs:
                continue
            seen_slugs.add(slug)
            batch_count += 1

            stub = ThreadStub(
                slug=slug,
                title=item.get("title", "Untitled"),
                space=item.get("collection_title"),
                space_uuid=item.get("collection_uuid"),
                last_query_datetime=item.get("last_query_datetime", ""),
                has_next_page=item.get("has_next_page", False),
                total_threads=item.get("total_threads"),
            )
            threads.append(stub)

        logger.info("Discovered %d threads (batch offset=%d, new=%d)", len(threads), offset, batch_count)

        has_next = data[0].get("has_next_page", False) if data else False
        if not has_next or len(data) < batch_size:
            break

        offset += batch_size

    logger.info("Discovery complete: %d total threads", len(threads))
    return threads
