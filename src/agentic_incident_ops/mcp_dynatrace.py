from __future__ import annotations

import asyncio
from typing import Any

from .models import IncidentInput
from .redaction import redact
from .settings import Settings


class DynatraceMCPClient:
    """Collect incident context through Dynatrace MCP when credentials exist."""

    def __init__(self, settings: Settings):
        self.settings = settings

    def collect_context(self, incident: IncidentInput) -> dict[str, Any]:
        if not self.settings.dynatrace_configured:
            return self._demo_context(incident)

        try:
            return asyncio.run(self._collect_remote(incident))
        except RuntimeError:
            return {
                "mode": "configured_but_skipped",
                "reason": "MCP remote collection requires a standalone event loop.",
                "endpoint": _safe_endpoint(self.settings.dynatrace_mcp_url),
            }
        except Exception as exc:  # pragma: no cover - depends on external MCP.
            return {
                "mode": "configured_but_unavailable",
                "reason": redact(exc),
                "endpoint": _safe_endpoint(self.settings.dynatrace_mcp_url),
            }

    async def _collect_remote(self, incident: IncidentInput) -> dict[str, Any]:
        from mcp import ClientSession
        from mcp.client.streamable_http import streamablehttp_client

        headers = {"Authorization": f"Bearer {self.settings.dynatrace_mcp_token}"}
        async with streamablehttp_client(self.settings.dynatrace_mcp_url, headers=headers) as streams:
            read_stream, write_stream, *_ = streams
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                tools_result = await session.list_tools()
                tool_names = [tool.name for tool in getattr(tools_result, "tools", [])]
                preferred = _choose_tool(tool_names)
                call_result: Any = None
                if preferred:
                    call_result = await session.call_tool(
                        preferred,
                        {
                            "query": (
                                f"Investigate {incident.severity} incident for "
                                f"{incident.service}: {incident.title}"
                            )
                        },
                    )
                return {
                    "mode": "dynatrace_mcp",
                    "endpoint": _safe_endpoint(self.settings.dynatrace_mcp_url),
                    "tools": tool_names,
                    "selected_tool": preferred,
                    "result": redact(call_result) if call_result is not None else "",
                }

    def _demo_context(self, incident: IncidentInput) -> dict[str, Any]:
        return {
            "mode": "demo",
            "endpoint": "not_configured",
            "tools": [
                "dynatrace.problems.investigate",
                "dynatrace.dql.query",
                "dynatrace.timeseries.forecast",
                "dynatrace.entities.resolve",
            ],
            "selected_tool": "dynatrace.problems.investigate",
            "result": {
                "problem": f"{incident.service} latency regression",
                "probable_root_cause": "New canary revision correlates with latency and payment failures.",
                "blast_radius": ["checkout-api", "payment-authorizer", "cart-conversion"],
                "confidence": 0.78,
            },
        }


def _choose_tool(tool_names: list[str]) -> str:
    for keyword in ("problem", "investigate", "dql", "query"):
        for name in tool_names:
            if keyword in name.lower():
                return name
    return tool_names[0] if tool_names else ""


def _safe_endpoint(endpoint: str) -> str:
    if not endpoint:
        return ""
    return endpoint.replace("https://", "").split("/")[0]
