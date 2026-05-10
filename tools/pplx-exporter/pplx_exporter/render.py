"""Render thread data to Markdown with YAML frontmatter."""

from __future__ import annotations

import hashlib
import re

from .config import BASE_URL
from .types import ThreadData


def render_thread(thread: ThreadData) -> tuple[str, str, int]:
    """Render a thread to Markdown with YAML frontmatter.

    Returns (markdown_string, sha256_hash, byte_count).
    """
    frontmatter = _build_frontmatter(thread)
    body = _build_body(thread)
    markdown = f"---\n{frontmatter}---\n\n{body}"

    encoded = markdown.encode("utf-8")
    sha = hashlib.sha256(encoded).hexdigest()
    return markdown, f"sha256:{sha}", len(encoded)


def _build_frontmatter(thread: ThreadData) -> str:
    """Build YAML frontmatter block."""
    lines: list[str] = []
    lines.append(f"pplx_slug: {thread.slug}")
    lines.append(f"pplx_url: {BASE_URL}/search/{thread.slug}")
    lines.append(f"title: {_yaml_quote(thread.title)}")

    if thread.space:
        lines.append(f"space: {_yaml_quote(thread.space)}")

    if thread.created_at:
        lines.append(f"created_at: \"{thread.created_at}\"")
    if thread.updated_at:
        lines.append(f"updated_at: \"{thread.updated_at}\"")

    lines.append("source: perplexity")
    lines.append("tier: INTUITED")
    lines.append("export_tool: pplx-exporter-v0.1")
    lines.append("")

    return "\n".join(lines)


def _build_body(thread: ThreadData) -> str:
    """Build the conversation body."""
    parts: list[str] = []
    parts.append(f"# {thread.title}\n")

    for i, entry in enumerate(thread.entries, 1):
        if entry.query:
            parts.append(f"## Q{i}: {entry.query}\n")
        if entry.answer:
            parts.append(entry.answer)
            parts.append("")

        if entry.sources:
            parts.append("### Sources\n")
            for src in entry.sources:
                title = src.get("title", "")
                url = src.get("url", "")
                if url:
                    parts.append(f"- [{title}]({url})")
                elif title:
                    parts.append(f"- {title}")
            parts.append("")

    return "\n".join(parts)


def _yaml_quote(value: str) -> str:
    """Quote a string for YAML if it contains special characters."""
    if any(c in value for c in (':', '#', '"', "'", '{', '}', '[', ']', ',', '&', '*', '?', '|', '>', '!', '%', '@')):
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    if not value or value != value.strip():
        return f'"{value}"'
    return f'"{value}"'


def slugify_filename(title: str) -> str:
    """Convert a title to a filesystem-safe filename."""
    clean = re.sub(r'[<>:"/\\|?*]', "", title)
    clean = re.sub(r"\s+", "-", clean.strip())
    clean = clean[:120]
    return clean or "untitled"
