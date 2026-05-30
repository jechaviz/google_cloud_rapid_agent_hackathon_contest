# AegisOps Incident Agent

Track interno: `agentic_incident_ops`
Partner Devpost propuesto: `Dynatrace`

AegisOps es un agente de respuesta a incidentes para equipos SRE/DevOps. Toma un
incidente, consulta contexto operativo por MCP, razona con Gemini en Google
Cloud, propone acciones de contencion y genera evidencia lista para auditoria y
postmortem. El core oficial es Vlang; el dashboard demo vive separado en Vue3
CDN + SFC + UnoCSS.

## Por que este proyecto

El hackathon pide un agente funcional que vaya mas alla del chat, use Google
Cloud/Gemini, integre un partner MCP y entregue un proyecto web con repo publico,
video corto y formulario Devpost. Este repo queda organizado para entrar en el
track Dynatrace porque incident response necesita observabilidad, causalidad,
logs, SLOs y guardrails de remediacion.

Fuentes verificadas el 2026-05-29:

- Devpost rules: https://rapid-agent.devpost.com/rules
- Devpost overview: https://rapid-agent.devpost.com/
- Dynatrace MCP docs: https://docs.dynatrace.com/docs/dynatrace-intelligence/dynatrace-mcp
- Google ADK MCP docs: https://adk.dev/mcp/
- Google Cloud ADK + Cloud Run architecture: https://docs.cloud.google.com/architecture/single-agent-ai-system-adk-cloud-run

## Quickstart local

```powershell
cd C:\git\v_projects\google_cloud_rapid_agent_hackathon
v test .
v run cmd\agent --sample
v run cmd\agent serve --port 8080
```

Para abrir el dashboard local:

```powershell
v run C:\git\websites\google_cloud_rapid_agent_hackathon\tools\static_server.v C:\git\websites\google_cloud_rapid_agent_hackathon 8902
```

Luego abre http://127.0.0.1:8902. El dashboard hospedado para jueces esta en
https://jechaviz.github.io/google_cloud_rapid_agent_hackathon_web/.

## Modo con Gemini y MCP

Configura variables de entorno equivalentes o usa refs de VImport vault:

```powershell
$env:GEMINI_API_KEY="..."
$env:GOOGLE_GENAI_MODEL="gemini-2.5-flash"
$env:DYNATRACE_MCP_URL="https://ENV.apps.dynatrace.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp"
$env:DYNATRACE_MCP_TOKEN="..."
```

El agente no ejecuta acciones mutables sin aprobacion humana. En este MVP las
acciones peligrosas se emiten como propuestas con `approval_required: true`.

## Estructura

- Producto V: `C:\git\v_projects\google_cloud_rapid_agent_hackathon`
- Dashboard web: `C:\git\websites\google_cloud_rapid_agent_hackathon`
- `docs/`: plan Devpost, checklist de reglas, video outline, backlog y evidencia.
- `submission/`: borrador de campos para Devpost.
- `automation/`: playbooks WAIBAv para readiness y no-submit gates.
- `scripts/`: wrappers de evidence/submission, video y automatizacion de formulario.

## Deploy Cloud Run

```powershell
.\scripts\run_v_evidence.ps1
v run C:\git\v_projects\google_cloud_rapid_agent_hackathon\cmd\agent serve --port 8080
```

Para deploy productivo:

```powershell
cd C:\git\v_projects\google_cloud_rapid_agent_hackathon
.\scripts\deploy_cloud_run.ps1 -ProjectId YOUR_PROJECT_ID -Region us-central1
```

## Devpost

El paquete de entrega vive en:

- `TASK_DEVPOST_PROD_100.md`
- `docs/rules_checklist.md`
- `docs/evidence_pack.md`
- `docs/video_outline.md`
- `docs/daily_backlog.md`
- `docs/waibav_veloclaw_automation.md`
- `submission/devpost_form_draft.md`
- `evidence/v_agent_run.json`
- `evidence/v_eval.json`
- `evidence/v_agent_run_gemini.json`
- `evidence/secure_external_enablement.json`

La automatizacion de submission esta en `scripts/devpost_submission_automation.py`.
Por seguridad, prepara y llena formularios en una sesion autorizada, pero no hace
click final de submit salvo que se ejecute con `--submit` y la variable
`CONFIRM_DEVPOST_SUBMIT=YES`.
