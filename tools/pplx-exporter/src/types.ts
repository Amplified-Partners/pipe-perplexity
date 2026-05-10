/**
 * Core types for the Perplexity exporter.
 * Derived from reverse-engineered API responses (STRUCTURED from code analysis).
 */

export interface ThreadStub {
  slug: string;
  title: string;
  collection?: { title: string; uuid: string };
  last_query_datetime: string;
}

export interface Block {
  intended_usage:
    | "ask_text"
    | "sources_answer_mode"
    | "image_answer_mode"
    | "video_answer_mode"
    | string;
  markdown_block?: { answer: string };
  sources_mode_block?: { rows: SourceRow[] };
  image_mode_block?: { media_items: ImageItem[] };
  video_mode_block?: { media_items: VideoItem[] };
}

export interface SourceRow {
  title?: string;
  url?: string;
  snippet?: string;
}

export interface ImageItem {
  url?: string;
  alt?: string;
}

export interface VideoItem {
  url?: string;
  title?: string;
}

export interface Entry {
  thread_url_slug: string;
  thread_title?: string;
  query_str: string;
  updated_datetime: string;
  collection_info?: { title: string; uuid?: string };
  blocks: Block[];
}

export interface ConversationResponse {
  status?: string;
  entries: Entry[];
  thread_title?: string;
  collection_info?: { title: string; uuid: string };
  updated_datetime?: string;
}

export interface SpaceMetadata {
  url: string;
  name: string;
  uuid?: string;
}

export interface ConversationMetadata {
  slug: string;
  title: string;
  spaceName?: string;
  spaceUuid?: string;
  createdAt?: string;
  updatedAt?: string;
}

export interface Checkpoint {
  processedSlugs: string[];
  discoveryCompleted: boolean;
  spaces: SpaceMetadata[];
  discoveredThreads: ThreadStub[];
  lastUpdated: string;
  runId: string;
}

export interface ManifestEntry {
  slug: string;
  title: string;
  space?: string;
  spaceUuid?: string;
  created_at?: string;
  updated_at?: string;
  file_path: string;
  byte_count: number;
  sha256: string;
}

export interface Manifest {
  export_run_id: string;
  export_timestamp: string;
  tool_version: string;
  total_threads: number;
  threads: ManifestEntry[];
}

export interface AuditEntry {
  ts: string;
  event: string;
  slug?: string;
  bytes?: number;
  hash?: string;
  status?: string;
  error?: string;
  retry?: number;
}

export interface ExporterConfig {
  outputDir: string;
  browserDataDir: string;
  checkpointPath: string;
  auditLogPath: string;
  manifestPath: string;
  headless: boolean;
  rateLimitMs: number;
  maxRetries: number;
  batchSize: number;
}
