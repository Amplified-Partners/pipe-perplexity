"""HTTP client with curl_cffi — Cloudflare bypass via Chrome TLS fingerprint."""

from __future__ import annotations

import asyncio
import logging
from random import choice
from time import monotonic
from typing import Any

from curl_cffi.requests import AsyncSession, Response

from .config import BASE_URL, BROWSER_PROFILES, DEFAULT_HEADERS, SESSION_COOKIE, RetryConfig

logger = logging.getLogger(__name__)


class RateLimiter:
    """Token-bucket rate limiter."""

    def __init__(self, min_interval_ms: int) -> None:
        self._min_interval = min_interval_ms / 1000.0
        self._last_request: float = 0.0

    async def acquire(self) -> None:
        now = monotonic()
        if self._last_request > 0:
            elapsed = now - self._last_request
            wait = self._min_interval - elapsed
            if wait > 0:
                await asyncio.sleep(wait)
        self._last_request = monotonic()


class HTTPClient:
    """Async HTTP client wrapping curl_cffi with fingerprint rotation and retry."""

    def __init__(
        self,
        session_token: str,
        rate_limiter: RateLimiter | None = None,
        retry_config: RetryConfig | None = None,
    ) -> None:
        self._token = session_token
        self._rate_limiter = rate_limiter
        self._retry = retry_config or RetryConfig()
        self._impersonate = choice(BROWSER_PROFILES)
        self._session: AsyncSession | None = None

    async def _get_session(self) -> AsyncSession:
        if self._session is None:
            self._session = AsyncSession(
                headers=dict(DEFAULT_HEADERS),
                cookies={SESSION_COOKIE: self._token},
                timeout=60,
                impersonate=self._impersonate,
            )
        return self._session

    def _rotate_fingerprint(self) -> None:
        self._impersonate = choice(BROWSER_PROFILES)
        if self._session is not None:
            self._session.close()
            self._session = None

    async def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        url = f"{BASE_URL}{path}"
        return await self._request("GET", url, params=params)

    async def post(self, path: str, json_body: dict[str, Any] | None = None) -> Any:
        url = f"{BASE_URL}{path}"
        return await self._request("POST", url, json_body=json_body)

    async def _request(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
    ) -> Any:
        last_exc: Exception | None = None

        for attempt in range(self._retry.max_retries + 1):
            if self._rate_limiter:
                await self._rate_limiter.acquire()

            try:
                session = await self._get_session()
                extra_headers = {
                    "x-perplexity-request-endpoint": url,
                    "x-perplexity-request-try-number": str(attempt + 1),
                }

                if method == "GET":
                    resp: Response = await session.get(url, params=params, headers=extra_headers)
                else:
                    resp = await session.post(url, json=json_body, headers=extra_headers)

                if resp.status_code == 401:
                    raise AuthError("Session token expired or invalid (401)")
                if resp.status_code == 429 or resp.status_code == 503:
                    raise RetryableError(f"Rate limited or unavailable ({resp.status_code})")
                if resp.status_code >= 400:
                    raise HTTPError(f"HTTP {resp.status_code}: {resp.text[:200]}")

                return resp.json()

            except RetryableError as exc:
                last_exc = exc
                if attempt < self._retry.max_retries:
                    delay = min(
                        self._retry.base_delay * (2**attempt),
                        self._retry.max_delay,
                    )
                    jitter = delay * self._retry.jitter
                    wait = delay + jitter * (2 * (monotonic() % 1) - 1)
                    logger.warning(
                        "Retry %d/%d after %.1fs: %s",
                        attempt + 1,
                        self._retry.max_retries,
                        wait,
                        exc,
                    )
                    self._rotate_fingerprint()
                    await asyncio.sleep(max(0.0, wait))
                continue

        if last_exc:
            raise last_exc
        raise RuntimeError("Request loop exited without result")

    async def close(self) -> None:
        if self._session:
            self._session.close()
            self._session = None


class AuthError(Exception):
    pass


class RetryableError(Exception):
    pass


class HTTPError(Exception):
    pass
