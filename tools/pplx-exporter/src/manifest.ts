import { writeFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname } from "node:path";
import type { Manifest, ManifestEntry } from "./types.js";

const TOOL_VERSION = "0.1.0";

export function createManifest(runId: string): Manifest {
  return {
    export_run_id: runId,
    export_timestamp: new Date().toISOString(),
    tool_version: TOOL_VERSION,
    total_threads: 0,
    threads: [],
  };
}

export function addManifestEntry(manifest: Manifest, entry: ManifestEntry): void {
  manifest.threads.push(entry);
  manifest.total_threads = manifest.threads.length;
}

export function saveManifest(path: string, manifest: Manifest): void {
  const dir = dirname(path);
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });

  manifest.export_timestamp = new Date().toISOString();
  writeFileSync(path, JSON.stringify(manifest, null, 2), "utf-8");
}
