import { resolve } from "node:path";
import type { ExporterConfig } from "./types.js";

const DEFAULT_OUTPUT_DIR = resolve(process.cwd(), "pplx-export");

export function buildConfig(overrides: Partial<ExporterConfig> = {}): ExporterConfig {
  const outputDir = overrides.outputDir ?? DEFAULT_OUTPUT_DIR;

  return {
    outputDir,
    browserDataDir: overrides.browserDataDir ?? resolve(outputDir, ".browser-data"),
    checkpointPath: overrides.checkpointPath ?? resolve(outputDir, "checkpoint.json"),
    auditLogPath: overrides.auditLogPath ?? resolve(outputDir, "audit.log"),
    manifestPath: overrides.manifestPath ?? resolve(outputDir, "manifest.json"),
    headless: overrides.headless ?? false,
    rateLimitMs: overrides.rateLimitMs ?? 1500,
    maxRetries: overrides.maxRetries ?? 5,
    batchSize: overrides.batchSize ?? 20,
  };
}
