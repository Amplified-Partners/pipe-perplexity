import { createHash } from "node:crypto";
import type { ConversationResponse, Entry, Block, SourceRow } from "./types.js";

interface RenderOptions {
  slug: string;
  spaceName?: string;
  spaceUuid?: string;
}

export interface RenderedThread {
  markdown: string;
  sha256: string;
  byteCount: number;
  title: string;
  createdAt?: string;
  updatedAt?: string;
}

export function renderThread(conversation: ConversationResponse, opts: RenderOptions): RenderedThread {
  const title = conversation.thread_title ?? conversation.entries?.[0]?.thread_title ?? "Untitled";
  const updatedAt = conversation.updated_datetime ?? conversation.entries?.[0]?.updated_datetime;
  const createdAt = findEarliestDate(conversation.entries);
  const spaceName = opts.spaceName ?? conversation.collection_info?.title;
  const spaceUuid = opts.spaceUuid ?? conversation.collection_info?.uuid;

  const frontmatter = buildFrontmatter({
    pplx_slug: opts.slug,
    pplx_url: `https://www.perplexity.ai/search/${opts.slug}`,
    title,
    space: spaceName,
    space_uuid: spaceUuid,
    created_at: createdAt,
    updated_at: updatedAt,
    source: "perplexity",
    tier: "INTUITED",
    tier_note: "Exported from Perplexity UI. Content not independently verified.",
    export_tool: "pplx-exporter-v0.1",
  });

  const body = renderEntries(conversation.entries);
  const markdown = frontmatter + "\n" + body;
  const byteCount = Buffer.byteLength(markdown, "utf-8");
  const sha256 = createHash("sha256").update(markdown).digest("hex");

  return { markdown, sha256, byteCount, title, createdAt, updatedAt };
}

function buildFrontmatter(fields: Record<string, string | undefined>): string {
  const lines = ["---"];
  for (const [key, value] of Object.entries(fields)) {
    if (value === undefined || value === null) continue;
    const escaped = value.includes(":") || value.includes('"') ? `"${value.replace(/"/g, '\\"')}"` : value;
    lines.push(`${key}: ${escaped}`);
  }
  lines.push("---");
  return lines.join("\n");
}

function renderEntries(entries: Entry[]): string {
  if (!entries || entries.length === 0) return "*No conversation content found.*\n";

  const sections: string[] = [];

  for (const entry of entries) {
    if (entry.query_str) {
      sections.push(`## ${entry.query_str}\n`);
    }

    if (entry.blocks && Array.isArray(entry.blocks)) {
      for (const block of entry.blocks) {
        sections.push(renderBlock(block));
      }
    }
  }

  return sections.join("\n");
}

function renderBlock(block: Block): string {
  switch (block.intended_usage) {
    case "ask_text":
      return (block.markdown_block?.answer ?? "") + "\n";

    case "sources_answer_mode":
      return renderSources(block.sources_mode_block?.rows ?? []);

    case "image_answer_mode":
      return renderImages(block.image_mode_block?.media_items ?? []);

    case "video_answer_mode":
      return renderVideos(block.video_mode_block?.media_items ?? []);

    default:
      if (block.markdown_block?.answer) {
        return block.markdown_block.answer + "\n";
      }
      return "";
  }
}

function renderSources(sources: SourceRow[]): string {
  if (sources.length === 0) return "";

  const lines = ["\n### Sources\n"];
  for (let i = 0; i < sources.length; i++) {
    const s = sources[i];
    const title = s.title ?? s.url ?? `Source ${i + 1}`;
    const url = s.url ?? "#";
    lines.push(`${i + 1}. [${title}](${url})`);
  }
  return lines.join("\n") + "\n";
}

function renderImages(items: { url?: string; alt?: string }[]): string {
  if (items.length === 0) return "";

  const lines = items.map((img) => `![${img.alt ?? "image"}](${img.url ?? ""})`);
  return lines.join("\n") + "\n";
}

function renderVideos(items: { url?: string; title?: string }[]): string {
  if (items.length === 0) return "";

  const lines = items.map((v) => `[${v.title ?? "Video"}](${v.url ?? ""})`);
  return lines.join("\n") + "\n";
}

function findEarliestDate(entries: Entry[]): string | undefined {
  if (!entries || entries.length === 0) return undefined;

  const dates = entries
    .map((e) => e.updated_datetime)
    .filter(Boolean)
    .sort();

  return dates[0] ?? undefined;
}
