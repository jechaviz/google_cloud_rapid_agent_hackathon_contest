# Demo video outline

Duracion objetivo: 2:45 a 3:00.

## Titulo

AegisOps Incident Agent: Gemini + Dynatrace MCP for guarded incident response

## Shot list

### 0:00-0:20 - Hook

Mostrar dashboard con incidente de checkout.

Narracion: "Incident response fails when teams spend the first minutes copying
logs, guessing blast radius, and debating risky fixes. AegisOps turns that into
a supervised agent run."

### 0:20-0:45 - Architecture

Mostrar README o diagrama simple en pantalla:

- Web app on Cloud Run
- Gemini reasoning
- Dynatrace MCP context
- Approval-gated remediation
- Evidence pack

### 0:45-1:30 - Live run

En la UI, editar un sintoma y presionar "Run triage". Mostrar:

- severity
- service
- plan multi-step
- MCP selected tool
- evidence digest

### 1:30-2:05 - Partner and Google proof

Mostrar JSON expandido:

- `google_integration.model`
- `google_integration.cloud_runtime`
- `mcp_integration.mode`
- Dynatrace tools

Narracion: "The agent is useful in demo mode, and in production it connects to
Dynatrace MCP with a Platform Token stored in Secret Manager."

### 2:05-2:35 - Safety and action

Mostrar action proposals:

- shift canary traffic
- SLO watch
- `approval_required=true`

Narracion: "It does not blindly self-heal. It prepares reversible actions and
keeps the incident commander in control."

### 2:35-2:55 - Evidence and impact

Mostrar `docs/evidence_pack.md` y `evidence/sample_agent_run.json`.

Narracion: "Every run creates evidence for audit and postmortem. The outcome is
lower MTTR, safer remediation, and better learning after incidents."

### 2:55-3:00 - Close

Mostrar hosted URL y repo URL.

Narracion: "This is AegisOps, built for the Dynatrace track of the Google Cloud
Rapid Agent Hackathon."

## Recording checklist

- [ ] Browser zoom 100 percent.
- [ ] No secrets visible in env, terminal, screenshots or address bar.
- [ ] Use sample incident, not customer incident.
- [ ] Keep video under 3:00 if possible.
- [ ] Mention Google Cloud, Gemini and Dynatrace MCP by name.
- [ ] Show actual running app, not only slides.
