"""Core data types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ThreadStub:
    slug: str
    title: str
    space: str | None = None
    space_uuid: str | None = None
    last_query_datetime: str = ""
    has_next_page: bool = False
    total_threads: int | None = None


@dataclass
class Entry:
    query: str = ""
    answer: str = ""
    sources: list[dict[str, str]] = field(default_factory=list)
    updated_at: str = ""


@dataclass
class ThreadData:
    slug: str = ""
    title: str = ""
    entries: list[Entry] = field(default_factory=list)
    space: str | None = None
    space_uuid: str | None = None
    created_at: str = ""
    updated_at: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class Checkpoint:
    processed_slugs: list[str] = field(default_factory=list)
    discovery_completed: bool = False
    discovered_threads: list[dict[str, Any]] = field(default_factory=list)
    last_updated: str = ""
    run_id: str = ""


@dataclass
class ManifestEntry:
    slug: str
    title: str
    space: str | None = None
    file_path: str = ""
    byte_count: int = 0
    sha256: str = ""
    created_at: str | None = None
    updated_at: str | None = None
