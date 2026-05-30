from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from typing import Any


def utc_now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


@dataclass
class IncidentInput:
    title: str
    service: str
    severity: str
    started_at: str
    symptoms: list[str] = field(default_factory=list)
    telemetry_links: list[str] = field(default_factory=list)
    suspected_change: str = ""
    business_impact: str = ""
    constraints: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "IncidentInput":
        return cls(
            title=str(data.get("title") or "Untitled incident"),
            service=str(data.get("service") or "unknown-service"),
            severity=str(data.get("severity") or "SEV-3"),
            started_at=str(data.get("started_at") or utc_now_iso()),
            symptoms=_as_list(data.get("symptoms")),
            telemetry_links=_as_list(data.get("telemetry_links")),
            suspected_change=str(data.get("suspected_change") or ""),
            business_impact=str(data.get("business_impact") or ""),
            constraints=_as_list(data.get("constraints")),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AgentStep:
    name: str
    intent: str
    tool: str
    status: str
    evidence: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ActionProposal:
    action_id: str
    title: str
    rationale: str
    command_preview: str
    risk: str
    approval_required: bool = True

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str):
        if not value.strip():
            return []
        return [line.strip() for line in value.splitlines() if line.strip()]
    return [str(value)]
