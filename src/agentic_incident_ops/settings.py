from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    app_name: str = "AegisOps Incident Agent"
    track: str = "agentic_incident_ops"
    partner_track: str = "Dynatrace"
    environment: str = os.getenv("AGENT_ENV", "demo")
    google_project: str = os.getenv("GOOGLE_CLOUD_PROJECT", "")
    google_location: str = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
    google_model: str = os.getenv("GOOGLE_GENAI_MODEL", "gemini-3.5-flash")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY", "")
    dynatrace_mcp_url: str = os.getenv("DYNATRACE_MCP_URL", "")
    dynatrace_mcp_token: str = os.getenv("DYNATRACE_MCP_TOKEN", "")
    allow_mutating_actions: bool = os.getenv("ALLOW_MUTATING_ACTIONS", "false").lower() == "true"

    @property
    def gemini_configured(self) -> bool:
        return bool(self.gemini_api_key)

    @property
    def dynatrace_configured(self) -> bool:
        return bool(self.dynatrace_mcp_url and self.dynatrace_mcp_token)
