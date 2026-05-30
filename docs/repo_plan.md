# Repo plan

## Estructura objetivo

- `README.md`: pitch, quickstart, deploy y Devpost handoff.
- `src/agentic_incident_ops/`: paquete Python del agente.
- `src/agentic_incident_ops/web.py`: hosted web app para judges.
- `src/agentic_incident_ops/agent.py`: orquestacion multi-step.
- `src/agentic_incident_ops/mcp_dynatrace.py`: cliente Dynatrace MCP.
- `src/agentic_incident_ops/llm.py`: wrapper Gemini con fallback demo.
- `scripts/deploy_cloud_run.ps1`: deploy Google Cloud Run.
- `scripts/devpost_submission_automation.py`: llenado seguro de Devpost.
- `docs/`: reglas, evidencia, video, backlog, integracion.
- `submission/`: campos Devpost y JSON automatizable.
- `evidence/`: salidas generadas, screenshots y recibos.

## Branching y release

- Branch de trabajo: `main` hasta que exista remoto; usar `devpost-prod-100` si
  se abre PR.
- Tag final sugerido: `devpost-2026-final`.
- Freeze interno: 2026-06-10 20:00 America/Mexico_City.
- Submit interno recomendado: 2026-06-11 12:00 America/Mexico_City.

## Gates

- Gate 1: tests unitarios pasan.
- Gate 2: UI local corre y genera JSON.
- Gate 3: imagen Docker construye.
- Gate 4: Cloud Run URL responde `/healthz`.
- Gate 5: Devpost draft tiene hosted URL, repo URL y video URL.
- Gate 6: evidence pack no contiene secretos.

## Riesgos

- Creditos Google Cloud limitados: pedir o confirmar billing antes de
  2026-06-04.
- Dynatrace token: usar Platform Token con permisos minimos, nunca commitearlo.
- Devpost login/CAPTCHA: automatizacion debe operar en sesion autorizada y
  pasar a humano si aparece challenge.
- Video tarde: grabar version rough el 2026-06-04 y reemplazar solo si mejora.
