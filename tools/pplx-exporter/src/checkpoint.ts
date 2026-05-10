import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname } from "node:path";
import type { Checkpoint, SpaceMetadata, ThreadStub } from "./types.js";
import { randomUUID } from "node:crypto";

export function loadCheckpoint(path: string): Checkpoint {
  if (!existsSync(path)) {
    return createFreshCheckpoint();
  }

  try {
    const raw = readFileSync(path, "utf-8");
    const data = JSON.parse(raw) as Checkpoint;
    console.log(
      `[checkpoint] Resumed: ${data.processedSlugs.length} threads already done, discovery=${data.discoveryCompleted}`
    );
    return data;
  } catch {
    console.warn("[checkpoint] Corrupt checkpoint file — starting fresh.");
    return createFreshCheckpoint();
  }
}

export function saveCheckpoint(path: string, checkpoint: Checkpoint): void {
  const dir = dirname(path);
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });

  checkpoint.lastUpdated = new Date().toISOString();
  writeFileSync(path, JSON.stringify(checkpoint, null, 2), "utf-8");
}

export function markDiscoveryComplete(checkpoint: Checkpoint, threads: ThreadStub[]): void {
  checkpoint.discoveryCompleted = true;
  checkpoint.discoveredThreads = threads;
}

export function markThreadProcessed(checkpoint: Checkpoint, slug: string): void {
  if (!checkpoint.processedSlugs.includes(slug)) {
    checkpoint.processedSlugs.push(slug);
  }
}

export function addSpace(checkpoint: Checkpoint, space: SpaceMetadata): void {
  const exists = checkpoint.spaces.some((s) => s.url === space.url || s.name === space.name);
  if (!exists) {
    checkpoint.spaces.push(space);
  }
}

function createFreshCheckpoint(): Checkpoint {
  return {
    processedSlugs: [],
    discoveryCompleted: false,
    spaces: [],
    discoveredThreads: [],
    lastUpdated: new Date().toISOString(),
    runId: randomUUID(),
  };
}
