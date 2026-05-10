import type { Page } from "playwright";
import type { ThreadStub, ExporterConfig } from "./types.js";

/**
 * Discovers all threads using the paginated POST /rest/thread/list_ask_threads endpoint.
 * Pattern from simwai/perplexity-ai-export — the only reliable pagination approach.
 */
export async function discoverAllThreads(page: Page, config: ExporterConfig): Promise<ThreadStub[]> {
  console.log("[discovery] Detecting API version...");
  const apiVersion = await detectApiVersion(page);
  console.log(`[discovery] Using API version: ${apiVersion}`);

  console.log("[discovery] Paginating through all threads...");
  const allThreads: ThreadStub[] = [];
  let offset = 0;
  let emptyBatches = 0;

  // eslint-disable-next-line no-constant-condition
  while (true) {
    const batch = await fetchThreadBatch(page, apiVersion, offset, config.batchSize);

    if (!batch || batch.length === 0) {
      emptyBatches++;
      if (emptyBatches >= 2) break;
      offset += config.batchSize;
      continue;
    }

    emptyBatches = 0;
    allThreads.push(...batch);
    console.log(`[discovery] Found ${allThreads.length} threads so far (batch offset=${offset})`);

    if (batch.length < config.batchSize) break;

    offset += config.batchSize;
    await page.waitForTimeout(config.rateLimitMs);
  }

  console.log(`[discovery] Total threads discovered: ${allThreads.length}`);
  return deduplicateThreads(allThreads);
}

async function detectApiVersion(page: Page): Promise<string> {
  try {
    const [version] = await Promise.all([
      new Promise<string>((resolve) => {
        const timeout = setTimeout(() => resolve("2.18"), 8000);

        page.on("request", (request) => {
          const url = request.url();
          if (url.includes("/rest/thread/list_ask_threads") || url.includes("/rest/thread/list_recent")) {
            const versionMatch = url.match(/[?&]version=([^&]+)/);
            if (versionMatch) {
              clearTimeout(timeout);
              resolve(versionMatch[1]);
            }
          }
        });
      }),
      page.goto("https://www.perplexity.ai/library", { waitUntil: "networkidle" }),
    ]);
    return version;
  } catch {
    console.warn("[discovery] Could not detect API version, falling back to 2.18");
    return "2.18";
  }
}

async function fetchThreadBatch(
  page: Page,
  apiVersion: string,
  offset: number,
  limit: number
): Promise<ThreadStub[]> {
  const result = await page.evaluate(
    async ({ apiVersion, offset, limit }) => {
      try {
        const response = await fetch(
          `/rest/thread/list_ask_threads?version=${apiVersion}&source=default`,
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              limit,
              ascending: false,
              offset,
              search_term: "",
            }),
          }
        );

        if (!response.ok) return { error: `HTTP ${response.status}`, data: [] };

        const data = await response.json();
        const threads = Array.isArray(data) ? data : [];

        return {
          error: null,
          data: threads.map((t: Record<string, unknown>) => ({
            slug: t.slug ?? t.thread_url_slug ?? "",
            title: t.title ?? t.thread_title ?? "Untitled",
            collection: t.collection ?? t.collection_info ?? undefined,
            last_query_datetime: t.last_query_datetime ?? t.updated_datetime ?? "",
          })),
        };
      } catch (err) {
        return { error: String(err), data: [] };
      }
    },
    { apiVersion, offset, limit }
  );

  if (result.error) {
    console.warn(`[discovery] Batch fetch error at offset=${offset}: ${result.error}`);
  }

  return result.data as ThreadStub[];
}

function deduplicateThreads(threads: ThreadStub[]): ThreadStub[] {
  const seen = new Map<string, ThreadStub>();
  for (const t of threads) {
    if (t.slug && !seen.has(t.slug)) {
      seen.set(t.slug, t);
    }
  }
  return [...seen.values()];
}
