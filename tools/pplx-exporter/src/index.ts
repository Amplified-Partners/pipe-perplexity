#!/usr/bin/env node
/**
 * pplx-exporter v0.1.0 — Perplexity conversation exporter
 *
 * Exports all Perplexity threads to Markdown (YAML frontmatter) + JSON,
 * with manifest, audit log, and full checkpoint resumability.
 *
 * Devon-0730 | 2026-05-10 | Amplified Partners
 */

import { resolve } from "node:path";
import { writeFileSync, mkdirSync, existsSync } from "node:fs";
import { buildConfig } from "./config.js";
import { launchBrowser, ensureLoggedIn } from "./auth.js";
import { loadCheckpoint, saveCheckpoint, markDiscoveryComplete, markThreadProcessed, addSpace } from "./checkpoint.js";
import { discoverAllThreads } from "./discovery.js";
import { fetchThread } from "./fetch-thread.js";
import { renderThread } from "./render.js";
import { createManifest, addManifestEntry, saveManifest } from "./manifest.js";
import { auditRunStart, auditRunEnd, auditDiscoveryComplete, auditThreadFetched, auditThreadFailed } from "./audit.js";
import type { ExporterConfig, ThreadStub } from "./types.js";

function parseArgs(): Partial<ExporterConfig> {
  const args = process.argv.slice(2);
  const overrides: Partial<ExporterConfig> = {};

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case "--output":
      case "-o":
        overrides.outputDir = resolve(args[++i]);
        break;
      case "--headless":
        overrides.headless = true;
        break;
      case "--rate-limit":
        overrides.rateLimitMs = parseInt(args[++i], 10);
        break;
      case "--batch-size":
        overrides.batchSize = parseInt(args[++i], 10);
        break;
      case "--max-retries":
        overrides.maxRetries = parseInt(args[++i], 10);
        break;
      case "--help":
      case "-h":
        printHelp();
        process.exit(0);
    }
  }

  return overrides;
}

function printHelp(): void {
  console.log(`
pplx-exporter v0.1.0 — Export your Perplexity conversations

Usage: npx tsx src/index.ts [options]

Options:
  -o, --output <dir>     Output directory (default: ./pplx-export)
  --headless             Run browser in headless mode (requires existing session)
  --rate-limit <ms>      Delay between thread fetches in ms (default: 1500)
  --batch-size <n>       Threads per discovery batch (default: 20)
  --max-retries <n>      Max retries per thread on failure (default: 5)
  -h, --help             Show this help

First run opens a browser for interactive login.
Subsequent runs reuse the saved session (browser-data directory).
`.trim());
}

function sanitizeFilename(name: string): string {
  return name
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, "")
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-")
    .slice(0, 80)
    .replace(/^-|-$/g, "");
}

function ensureDir(dir: string): void {
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
}

async function main(): Promise<void> {
  const overrides = parseArgs();
  const config = buildConfig(overrides);

  console.log("╔══════════════════════════════════════════╗");
  console.log("║   pplx-exporter v0.1.0                  ║");
  console.log("║   Amplified Partners                    ║");
  console.log("╚══════════════════════════════════════════╝");
  console.log(`[main] Output: ${config.outputDir}`);

  ensureDir(config.outputDir);

  const checkpoint = loadCheckpoint(config.checkpointPath);
  const manifest = createManifest(checkpoint.runId);

  auditRunStart(config.auditLogPath, checkpoint.runId);

  // Launch browser and authenticate
  const { context, page } = await launchBrowser(config);

  try {
    await ensureLoggedIn(page);

    // Discovery phase
    let threads: ThreadStub[];

    if (checkpoint.discoveryCompleted && checkpoint.discoveredThreads.length > 0) {
      console.log(`[main] Discovery already complete — ${checkpoint.discoveredThreads.length} threads cached.`);
      threads = checkpoint.discoveredThreads;
    } else {
      threads = await discoverAllThreads(page, config);
      markDiscoveryComplete(checkpoint, threads);
      auditDiscoveryComplete(config.auditLogPath, threads.length);
      saveCheckpoint(config.checkpointPath, checkpoint);
    }

    // Collect space metadata
    for (const t of threads) {
      if (t.collection) {
        addSpace(checkpoint, {
          name: t.collection.title,
          uuid: t.collection.uuid,
          url: `https://www.perplexity.ai/collections/${t.collection.uuid ?? ""}`,
        });
      }
    }

    // Filter already-processed threads
    const pending = threads.filter((t) => !checkpoint.processedSlugs.includes(t.slug));
    console.log(`[main] ${pending.length} threads to export (${checkpoint.processedSlugs.length} already done).`);

    // Fetch and render each thread
    let exportedCount = 0;

    for (const threadStub of pending) {
      const slug = threadStub.slug;
      if (!slug) continue;

      console.log(`[main] Fetching: ${threadStub.title ?? slug}`);

      const conversation = await fetchThread(page, slug, config);

      if (!conversation) {
        auditThreadFailed(config.auditLogPath, slug, "null response after retries", config.maxRetries);
        markThreadProcessed(checkpoint, slug);
        saveCheckpoint(config.checkpointPath, checkpoint);
        continue;
      }

      // Render to Markdown
      const spaceName = threadStub.collection?.title;
      const spaceUuid = threadStub.collection?.uuid;
      const rendered = renderThread(conversation, { slug, spaceName, spaceUuid });

      // Determine output path
      const spaceDir = spaceName ? sanitizeFilename(spaceName) : "_unsorted";
      const threadDir = resolve(config.outputDir, spaceDir);
      ensureDir(threadDir);

      const filename = sanitizeFilename(rendered.title || slug) || slug;
      const mdPath = resolve(threadDir, `${filename}.md`);
      const jsonPath = resolve(threadDir, `${filename}.json`);

      // Write Markdown
      writeFileSync(mdPath, rendered.markdown, "utf-8");

      // Write raw JSON alongside
      writeFileSync(jsonPath, JSON.stringify(conversation, null, 2), "utf-8");

      // Update manifest
      const relativePath = `${spaceDir}/${filename}.md`;
      addManifestEntry(manifest, {
        slug,
        title: rendered.title,
        space: spaceName,
        spaceUuid,
        created_at: rendered.createdAt,
        updated_at: rendered.updatedAt,
        file_path: relativePath,
        byte_count: rendered.byteCount,
        sha256: rendered.sha256,
      });

      // Audit + checkpoint
      auditThreadFetched(config.auditLogPath, slug, rendered.byteCount, rendered.sha256);
      markThreadProcessed(checkpoint, slug);
      saveCheckpoint(config.checkpointPath, checkpoint);
      exportedCount++;

      // Rate limit
      await page.waitForTimeout(config.rateLimitMs);
    }

    // Save final manifest
    saveManifest(config.manifestPath, manifest);
    auditRunEnd(config.auditLogPath, exportedCount);

    console.log(`\n[main] Export complete.`);
    console.log(`[main] Total exported this run: ${exportedCount}`);
    console.log(`[main] Total in manifest: ${manifest.total_threads}`);
    console.log(`[main] Output: ${config.outputDir}`);
  } finally {
    await context.close();
  }
}

main().catch((err) => {
  console.error("[fatal]", err);
  process.exit(1);
});
