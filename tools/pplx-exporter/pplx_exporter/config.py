"""Configuration for the exporter."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Final

API_VERSION: Final[str] = "2.18"
BASE_URL: Final[str] = "https://www.perplexity.ai"
SESSION_COOKIE: Final[str] = "__Secure-next-auth.session-token"

DISCOVERY_ENDPOINT: Final[str] = "/rest/thread/list_ask_threads"
THREAD_ENDPOINT: Final[str] = "/rest/thread"

BROWSER_PROFILES: Final[tuple[str, ...]] = (
    "chrome",
    "chrome120",
    "chrome123",
    "chrome124",
    "chrome131",
    "safari17_0",
)

DEFAULT_HEADERS: Final[dict[str, str]] = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "x-app-apiclient": "default",
    "x-app-apiversion": API_VERSION,
}


@dataclass
class RetryConfig:
    max_retries: int = 5
    base_delay: float = 2.0
    max_delay: float = 32.0
    jitter: float = 0.3


@dataclass
class ExporterConfig:
    output_dir: Path = field(default_factory=lambda: Path("./pplx-export"))
    headless: bool = False
    rate_limit_ms: int = 1500
    discovery_rate_ms: int = 2000
    batch_size: int = 20
    retry: RetryConfig = field(default_factory=RetryConfig)

    @property
    def browser_data_dir(self) -> Path:
        return self.output_dir / ".browser-data"

    @property
    def checkpoint_path(self) -> Path:
        return self.output_dir / "checkpoint.json"

    @property
    def audit_log_path(self) -> Path:
        return self.output_dir / "audit.log"

    @property
    def manifest_path(self) -> Path:
        return self.output_dir / "manifest.json"

    @property
    def token_path(self) -> Path:
        return self.output_dir / ".token"
