import { appendFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname } from "node:path";
import type { AuditEntry } from "./types.js";

export function appendAudit(path: string, entry: AuditEntry): void {
  const dir = dirname(path);
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });

  const line = JSON.stringify({ ...entry, ts: entry.ts ?? new Date().toISOString() }) + "\n";
  appendFileSync(path, line, "utf-8");
}

export function auditThreadFetched(path: string, slug: string, bytes: number, hash: string): void {
  appendAudit(path, {
    ts: new Date().toISOString(),
    event: "thread_fetched",
    slug,
    bytes,
    hash,
    status: "ok",
  });
}

export function auditThreadFailed(path: string, slug: string, error: string, retry: number): void {
  appendAudit(path, {
    ts: new Date().toISOString(),
    event: "thread_fetch_failed",
    slug,
    error,
    retry,
    status: "error",
  });
}

export function auditDiscoveryComplete(path: string, totalThreads: number): void {
  appendAudit(path, {
    ts: new Date().toISOString(),
    event: "discovery_complete",
    status: "ok",
    bytes: totalThreads,
  });
}

export function auditRunStart(path: string, runId: string): void {
  appendAudit(path, {
    ts: new Date().toISOString(),
    event: "run_start",
    status: "ok",
    slug: runId,
  });
}

export function auditRunEnd(path: string, totalExported: number): void {
  appendAudit(path, {
    ts: new Date().toISOString(),
    event: "run_end",
    status: "ok",
    bytes: totalExported,
  });
}
