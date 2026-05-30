from __future__ import annotations

from .redaction import redact
from .settings import Settings


class GeminiPlanner:
    """Small Gemini wrapper with a deterministic fallback for demo mode."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def summarize(self, prompt: str) -> dict[str, str]:
        if not self.settings.gemini_configured:
            return {
                "mode": "demo",
                "model": self.settings.google_model,
                "text": "Gemini key not configured. Using deterministic incident reasoning for the demo.",
            }

        try:
            from google import genai

            client = genai.Client(api_key=self.settings.gemini_api_key)
            response = client.models.generate_content(
                model=self.settings.google_model,
                contents=prompt,
            )
            return {
                "mode": "gemini",
                "model": self.settings.google_model,
                "text": redact(getattr(response, "text", "") or str(response)),
            }
        except Exception as exc:  # pragma: no cover - depends on provider state.
            return {
                "mode": "gemini_unavailable",
                "model": self.settings.google_model,
                "text": f"Gemini call failed safely: {redact(exc)}",
            }
