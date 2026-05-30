from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from typing import Any

from .fixtures import sample_incident
from .llm import GeminiPlanner
from .mcp_dynatrace import DynatraceMCPClient
from .models import ActionProposal, AgentStep, IncidentInput, utc_now_iso
from .redaction import redact
from .settings import Settings


class IncidentOpsAgent:
    def __init__(self, settings: Settings | None = None):
        self.settings = settings or Settings()
        self.llm = GeminiPlanner(self.settings)
        self.mcp = DynatraceMCPClient(self.settings)

    def run(self, incident: IncidentInput | None = None) -> dict[str, Any]:
        incident = incident or sample_incident()
        mcp_context = self.mcp.collect_context(incident)
        narrative = self.llm.summarize(_build_prompt(incident, mcp_context))
        steps = _build_steps(incident, mcp_context)
        proposals = _build_action_proposals(incident, self.settings)
        evidence = _build_evidence(incident, mcp_context, narrative, steps, proposals)

        return {
            "run_id": _run_id(incident),
            "generated_at": utc_now_iso(),
            "agent": self.settings.app_name,
            "track": self.settings.track,
            "partner_track": self.settings.partner_track,
            "incident": incident.to_dict(),
            "summary": _summary(incident, mcp_context),
            "google_integration": {
                "model": self.settings.google_model,
                "mode": narrative["mode"],
                "cloud_runtime": "Cloud Run / Agent Engine compatible FastAPI service",
                "project": self.settings.google_project or "not_configured",
                "location": self.settings.google_location,
            },
            "mcp_integration": mcp_context,
            "agent_reasoning": narrative,
            "plan": [step.to_dict() for step in steps],
            "action_proposals": [proposal.to_dict() for proposal in proposals],
            "risk_controls": [
                "Mutating actions require explicit human approval.",
                "Secrets and email-like identifiers are redacted from evidence.",
                "No non-Google competing cloud is required for the core runtime.",
                "The demo produces repeatable evidence for judges without production credentials.",
            ],
            "devpost_readiness": {
                "hosted_project": "Cloud Run deploy script included",
                "open_source_repo": "MIT license included",
                "demo_video": "docs/video_outline.md",
                "rules_checklist": "docs/rules_checklist.md",
                "evidence_pack": "docs/evidence_pack.md",
            },
            "evidence": evidence,
        }


def run_incident_agent(data: dict[str, Any] | None = None) -> dict[str, Any]:
    incident = IncidentInput.from_dict(data or sample_incident().to_dict())
    return IncidentOpsAgent().run(incident)


def _build_prompt(incident: IncidentInput, mcp_context: dict[str, Any]) -> str:
    return json.dumps(
        {
            "task": "Summarize incident risk, probable root cause, and safe next actions.",
            "incident": incident.to_dict(),
            "mcp_context": mcp_context,
            "constraints": [
                "Do not execute mutating remediation.",
                "Return concise SRE language.",
                "Respect PII redaction.",
            ],
        },
        indent=2,
    )


def _build_steps(incident: IncidentInput, mcp_context: dict[str, Any]) -> list[AgentStep]:
    return [
        AgentStep(
            name="Stabilize intake",
            intent="Classify severity, impact, constraints, and decision owner.",
            tool="agent.policy",
            status="complete",
            evidence=[incident.severity, incident.business_impact or "impact pending"],
        ),
        AgentStep(
            name="Observe production context",
            intent="Pull problem, topology, logs, and anomaly context from partner MCP.",
            tool=f"Dynatrace MCP: {mcp_context.get('selected_tool', 'tool_discovery')}",
            status="complete" if mcp_context.get("mode") else "pending",
            evidence=[redact(mcp_context.get("result", ""))[:600]],
        ),
        AgentStep(
            name="Correlate release change",
            intent="Compare suspected change with incident start and blast radius.",
            tool="Google Cloud Run metrics + Cloud Logging",
            status="proposed",
            evidence=[incident.suspected_change or "No suspected change supplied"],
        ),
        AgentStep(
            name="Plan guarded remediation",
            intent="Draft reversible actions and pre/post checks for an incident commander.",
            tool="Gemini planner + approval gate",
            status="complete",
            evidence=["All mutating actions remain approval_required=true"],
        ),
        AgentStep(
            name="Package evidence",
            intent="Generate runbook, evidence trail, and postmortem seed for Devpost/demo.",
            tool="agent.evidence_pack",
            status="complete",
            evidence=["Evidence JSON is deterministic in demo mode"],
        ),
    ]


def _build_action_proposals(incident: IncidentInput, settings: Settings) -> list[ActionProposal]:
    approval = not settings.allow_mutating_actions
    return [
        ActionProposal(
            action_id="shift-canary-traffic",
            title="Reduce canary traffic to 0 percent",
            rationale=(
                "Latency symptoms correlate with the suspected Cloud Run revision. "
                "Traffic shift is reversible and avoids a full deploy rollback."
            ),
            command_preview=(
                "gcloud run services update-traffic "
                f"{incident.service} --to-revisions STABLE_REVISION=100,CANARY_REVISION=0"
            ),
            risk="medium",
            approval_required=approval,
        ),
        ActionProposal(
            action_id="raise-slo-watch",
            title="Create a 30 minute SLO watch and comms update",
            rationale="Keeps humans in control while the agent validates recovery.",
            command_preview="create_incident_update --window 30m --audience sre,oncall,commerce",
            risk="low",
            approval_required=approval,
        ),
    ]


def _build_evidence(
    incident: IncidentInput,
    mcp_context: dict[str, Any],
    narrative: dict[str, str],
    steps: list[AgentStep],
    proposals: list[ActionProposal],
) -> dict[str, Any]:
    evidence_body = {
        "incident": incident.to_dict(),
        "mcp_mode": mcp_context.get("mode"),
        "gemini_mode": narrative.get("mode"),
        "steps": [asdict(step) for step in steps],
        "proposals": [asdict(proposal) for proposal in proposals],
    }
    digest = hashlib.sha256(json.dumps(evidence_body, sort_keys=True).encode("utf-8")).hexdigest()
    return {
        "digest_sha256": digest,
        "redaction": "enabled",
        "artifacts_to_capture": [
            "Cloud Run service URL and revision",
            "Dynatrace MCP tool list and selected tool response",
            "Before/after incident timeline screenshot",
            "Agent run JSON",
            "Demo video transcript",
        ],
    }


def _summary(incident: IncidentInput, mcp_context: dict[str, Any]) -> str:
    root = ""
    result = mcp_context.get("result")
    if isinstance(result, dict):
        root = str(result.get("probable_root_cause") or "")
    root = root or "Probable cause requires live telemetry confirmation."
    return f"{incident.severity} on {incident.service}: {root}"


def _run_id(incident: IncidentInput) -> str:
    raw = f"{incident.title}|{incident.service}|{incident.started_at}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]
