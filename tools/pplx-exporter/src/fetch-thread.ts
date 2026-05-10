import type { Page } from "playwright";
import type { ConversationResponse, ExporterConfig } from "./types.js";

/**
 * Fetches a single thread's full conversation data.
 * Pattern from kylebrodeur/perplexity-exporter — page.evaluate(fetch()) inherits cookies.
 */
export async function fetchThread(
  page: Page,
  slug: string,
  config: ExporterConfig
): Promise<ConversationResponse | null> {
  let lastError: string | null = null;

  for (let attempt = 0; attempt < config.maxRetries; attempt++) {
    if (attempt > 0) {
      const backoffMs = Math.min(2000 * Math.pow(2, attempt - 1), 32000);
      console.log(`[fetch] Retry ${attempt}/${config.maxRetries} for ${slug} — waiting ${backoffMs}ms`);
      await page.waitForTimeout(backoffMs);
    }

    const result = await page.evaluate(async (threadSlug: string) => {
      try {
        const response = await fetch(`https://www.perplexity.ai/rest/thread/${threadSlug}`);
        if (!response.ok) {
          return { error: `HTTP ${response.status}`, data: null };
        }
        const raw = await response.json();
        return { error: null, data: raw };
      } catch (err) {
        return { error: String(err), data: null };
      }
    }, slug);

    if (result.error) {
      lastError = result.error;

      if (result.error.includes("404")) {
        console.warn(`[fetch] Thread ${slug} not found (404) — skipping.`);
        return null;
      }

      if (result.error.includes("401") || result.error.includes("403")) {
        throw new Error(`[fetch] Auth error on thread ${slug}: ${result.error}`);
      }

      continue;
    }

    if (!result.data) continue;

    return normalizeResponse(result.data);
  }

  console.error(`[fetch] Failed after ${config.maxRetries} attempts for ${slug}: ${lastError}`);
  return null;
}

function normalizeResponse(raw: unknown): ConversationResponse {
  if (Array.isArray(raw)) {
    return { entries: raw, status: "ok" };
  }

  const obj = raw as Record<string, unknown>;

  const entries = (obj.entries ?? obj.steps ?? obj.data ?? []) as ConversationResponse["entries"];

  return {
    status: (obj.status as string) ?? "ok",
    entries: Array.isArray(entries) ? entries : [],
    thread_title: obj.thread_title as string | undefined,
    collection_info: obj.collection_info as ConversationResponse["collection_info"],
    updated_datetime: obj.updated_datetime as string | undefined,
  };
}
