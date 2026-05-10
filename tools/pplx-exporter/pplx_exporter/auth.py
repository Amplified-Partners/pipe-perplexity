"""Authentication — extract session token via Playwright interactive login."""

from __future__ import annotations

import logging
from pathlib import Path

from .config import BASE_URL, SESSION_COOKIE

logger = logging.getLogger(__name__)


async def get_session_token(browser_data_dir: Path, headless: bool = False) -> str:
    """Get session token, either from stored file or via interactive login.

    Opens a Playwright browser with persistent context so cookies are retained.
    If already logged in, grabs the token immediately. Otherwise, waits for user login.
    """
    from playwright.async_api import async_playwright

    browser_data_dir.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch_persistent_context(
            user_data_dir=str(browser_data_dir),
            headless=headless,
            channel="chromium",
        )

        page = browser.pages[0] if browser.pages else await browser.new_page()
        await page.goto(f"{BASE_URL}/library")
        logger.info("Navigated to library — checking login state...")

        token = await _extract_token(browser)
        if token:
            logger.info("Already logged in — token extracted")
            await browser.close()
            return token

        logger.info("Not logged in — waiting for interactive login (up to 5 minutes)...")
        print("\n>>> Browser opened. Please log in to Perplexity. <<<\n")

        for _ in range(300):
            import asyncio

            await asyncio.sleep(1)
            token = await _extract_token(browser)
            if token:
                logger.info("Login detected — token extracted")
                await browser.close()
                return token

        await browser.close()
        raise TimeoutError("Login not detected within 5 minutes")


async def _extract_token(context: object) -> str | None:
    """Extract session cookie from browser context."""
    cookies = await context.cookies(BASE_URL)  # type: ignore[union-attr]
    for cookie in cookies:
        if cookie.get("name") == SESSION_COOKIE:
            value = cookie.get("value", "")
            if value:
                return value
    return None


def save_token(token: str, path: Path) -> None:
    """Persist token to file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(token, encoding="utf-8")


def load_token(path: Path) -> str | None:
    """Load token from file if it exists."""
    if path.exists():
        content = path.read_text(encoding="utf-8").strip()
        return content if content else None
    return None
