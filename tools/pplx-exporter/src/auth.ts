import { chromium, type BrowserContext, type Page } from "playwright";
import type { ExporterConfig } from "./types.js";

export async function launchBrowser(config: ExporterConfig): Promise<{ context: BrowserContext; page: Page }> {
  const context = await chromium.launchPersistentContext(config.browserDataDir, {
    headless: config.headless,
    viewport: { width: 1280, height: 800 },
    userAgent:
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
  });

  const page = context.pages()[0] ?? (await context.newPage());
  return { context, page };
}

export async function isLoggedIn(page: Page): Promise<boolean> {
  const libraryLink = await page.locator('a[href*="/library"]').count();
  if (libraryLink > 0) return true;

  const profileIndicator = await page.locator('[data-testid="user-menu"], [aria-label="User menu"]').count();
  return profileIndicator > 0;
}

export async function ensureLoggedIn(page: Page): Promise<void> {
  await page.goto("https://www.perplexity.ai/library", { waitUntil: "networkidle" });
  await page.waitForTimeout(2000);

  if (await isLoggedIn(page)) {
    console.log("[auth] Session valid — already logged in.");
    return;
  }

  console.log("[auth] Not logged in. Opening browser for interactive login...");
  console.log("[auth] Please log in to Perplexity in the browser window.");
  console.log("[auth] Waiting for login to complete (checking every 3s)...");

  const maxWaitMs = 300_000; // 5 minutes
  const checkIntervalMs = 3000;
  const startTime = Date.now();

  while (Date.now() - startTime < maxWaitMs) {
    await page.waitForTimeout(checkIntervalMs);
    if (await isLoggedIn(page)) {
      console.log("[auth] Login detected. Continuing.");
      return;
    }
  }

  throw new Error("[auth] Login timeout — user did not complete login within 5 minutes.");
}
