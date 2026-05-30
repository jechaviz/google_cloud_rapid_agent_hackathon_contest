# Tarea: llevar AegisOps Incident Agent a prod 100 para Devpost

Fecha de creacion: 2026-05-29
Deadline externo: 2026-06-11 14:00 PDT / 2026-06-11 15:00 America/Mexico_City
Track interno: `agentic_incident_ops`
Partner Devpost: `Dynatrace`

## Objetivo

Entregar un agente web funcional para Google Cloud Rapid Agent Hackathon que
resuelva incident response con Gemini, Google Cloud y Dynatrace MCP. Debe estar
listo para judging en Devpost con hosted URL, repo publico, licencia open source,
video de aproximadamente 3 minutos, evidencia reproducible y formulario completo.

## Fuentes verificadas

- Rules: https://rapid-agent.devpost.com/rules
- Overview y requirements: https://rapid-agent.devpost.com/
- Devpost participant guide: https://info.devpost.com/blog/google-cloud-rapid-agent-hackathon
- Dynatrace MCP: https://docs.dynatrace.com/docs/dynatrace-intelligence/dynatrace-mcp
- Google ADK MCP: https://adk.dev/mcp/
- Google Cloud ADK + Cloud Run: https://docs.cloud.google.com/architecture/single-agent-ai-system-adk-cloud-run

## Alcance prod 100

- MVP funcional web: backend V con endpoint `/api/agent/run`, sample incident,
  plan multi-step, propuestas de accion y evidencia JSON.
- Google integration: Gemini REST configurable por `GOOGLE_GENAI_MODEL`, deploy
  Cloud Run, variables para Google Cloud project/location y Secret Manager.
- MCP integration: adaptador Dynatrace MCP remoto por URL/token, con modo demo
  determinista si no hay credenciales.
- Repo plan: estructura, licencia MIT, deploy script, smoke tests y docs de
  operacion.
- Video outline: guion y shot list para demo de hasta 3 minutos.
- Rules checklist: trazabilidad de cada requirement del hackathon.
- Evidence pack: comandos, screenshots esperados, JSON de agente y checklist de
  redaccion.
- Backlog diario: plan del 2026-05-29 al 2026-06-11.
- Submission automation: script Playwright para preparar y llenar Devpost con
  no-submit gate hasta confirmacion explicita.

## Criterios de aceptacion

- `v test .` pasa en el repo de producto.
- `v run cmd\agent --sample` devuelve JSON con:
  - `track=agentic_incident_ops`
  - `partner_track=Dynatrace`
  - `google_integration.cloud_runtime` con Cloud Run
  - `mcp_integration.tools` no vacio
  - acciones con `approval_required=true` por default
  - `evidence.digest_sha256`
- `v run cmd\agent serve --port 8080` levanta API local.
- Dashboard Vue3 CDN + SFC + UnoCSS funciona local y en GitHub Pages.
- `Dockerfile` construye la app para Cloud Run.
- `LICENSE` existe y es visible en root del repo.
- `submission/devpost_submission.json` tiene campos listos para reemplazar URL.
- No hay tokens, screenshots sensibles ni PII innecesaria en evidencia; la cuenta
  autorizada de submission puede aparecer como alias operacional.
- Antes de submit final, Devpost queda revisado manualmente por humano y el
  script solo ejecuta submit con `--submit` y `CONFIRM_DEVPOST_SUBMIT=YES`.

## Decisiones

- Track partner elegido: Dynatrace, porque incident ops necesita problemas,
  DQL/logs, entidades, timeseries, SLOs y trazabilidad de remediacion.
- Primer release: demo sin credenciales para jueces, con opcion de conectar
  Dynatrace real si hay token autorizado.
- Acciones mutables: propuestas, no ejecucion automatica. Esto demuestra agencia
  bajo supervision y evita riesgo operativo.

## Definition of done Devpost

- Hosted URL: Cloud Run publico o demo hospedada equivalente.
- Repo URL: repo publico con `README.md`, `LICENSE`, source code, tests y docs.
- Video URL: publico/no listado, maximo aproximado 3 minutos, muestra app
  funcionando.
- Track selected: `Dynatrace`.
- Formulario Devpost: completado antes de 2026-06-11 14:00 PDT.
