# AegisOps Incident Agent

Track interno: `agentic_incident_ops`
Partner Devpost propuesto: `Dynatrace`

AegisOps es un agente de respuesta a incidentes para equipos SRE/DevOps. Toma
un incidente, consulta contexto operativo por MCP, razona con Gemini en Google
Cloud, propone acciones de contencion y genera evidencia lista para auditoria y
postmortem. El modo demo corre sin credenciales; el modo produccion conecta
Gemini y Dynatrace MCP con secretos reales.

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
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
python -m agentic_incident_ops --sample
uvicorn agentic_incident_ops.web:app --reload --port 8080
```

Si usas `uv`, el camino corto es:

```powershell
uv run python -m unittest discover
uv run python -m agentic_incident_ops --sample
uv run uvicorn agentic_incident_ops.web:app --reload --port 8080
```

Luego abre http://127.0.0.1:8080 y ejecuta la demo desde el formulario.

## Modo con Gemini y MCP

Copia `.env.example` a `.env` o configura variables de entorno equivalentes:

```powershell
$env:GEMINI_API_KEY="..."
$env:GOOGLE_GENAI_MODEL="gemini-3.5-flash"
$env:DYNATRACE_MCP_URL="https://ENV.apps.dynatrace.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp"
$env:DYNATRACE_MCP_TOKEN="..."
```

El agente no ejecuta acciones mutables sin aprobacion humana. En este MVP las
acciones peligrosas se emiten como propuestas con `approval_required: true`.

## Estructura

- `src/agentic_incident_ops/`: agente MVP, UI FastAPI y adaptadores.
- `docs/`: plan Devpost, checklist de reglas, video outline, backlog y evidencia.
- `submission/`: borrador de campos para Devpost.
- `scripts/`: demo local, deploy Cloud Run y automatizacion de formulario.
- `tests/`: smoke tests sin credenciales.

## Deploy Cloud Run

```powershell
.\scripts\deploy_cloud_run.ps1 -ProjectId YOUR_PROJECT_ID -Region us-central1
```

El script usa Cloud Run, Secret Manager por variables y mantiene el servicio web
como URL de judging.

## Devpost

El paquete de entrega vive en:

- `TASK_DEVPOST_PROD_100.md`
- `docs/rules_checklist.md`
- `docs/evidence_pack.md`
- `docs/video_outline.md`
- `docs/daily_backlog.md`
- `submission/devpost_form_draft.md`

La automatizacion de submission esta en `scripts/devpost_submission_automation.py`.
Por seguridad, prepara y llena formularios en una sesion autorizada, pero no hace
click final de submit salvo que se ejecute con `--submit` y la variable
`CONFIRM_DEVPOST_SUBMIT=YES`.
