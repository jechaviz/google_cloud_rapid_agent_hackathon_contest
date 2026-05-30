# Google + MCP integration

## Google Cloud

- Runtime: Cloud Run web app, compatible con despliegue rapido para judges.
- AI: Gemini via `google-genai`, model configurable por `GOOGLE_GENAI_MODEL`.
- Secrets: usar Secret Manager para `GEMINI_API_KEY`, `DYNATRACE_MCP_TOKEN` y
  `DYNATRACE_MCP_URL`.
- Observability: Cloud Logging/Cloud Run metrics como fuente de release y
  runtime checks.
- Agent Builder/ADK path: el diseno mantiene herramientas y pasos separados para
  migrar a ADK Agent Engine si se decide usar runtime administrado.

## Dynatrace MCP

Endpoint esperado:

```text
https://ENV.apps.dynatrace.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp
```

Variables:

```powershell
$env:DYNATRACE_MCP_URL="https://ENV.apps.dynatrace.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp"
$env:DYNATRACE_MCP_TOKEN="..."
```

Permisos minimos segun docs Dynatrace:

- `mcp-gateway:servers:invoke`
- `mcp-gateway:servers:read`
- permisos de lectura para logs/problems/timeseries que se demuestren en video

## Flujo de agente

1. Intake: recibe severidad, servicio, sintomas, cambio sospechoso e impacto.
2. MCP discovery: lista herramientas Dynatrace y elige problem/investigate/DQL.
3. Observacion: trae contexto de problema, blast radius y causalidad.
4. Google reasoning: Gemini resume riesgo y sugiere acciones bajo constraints.
5. Remediacion: genera propuestas reversibles con approval gate.
6. Evidencia: produce digest, artefactos esperados y postmortem seed.

## Demo sin credenciales

Si no hay token Dynatrace o Gemini, el agente usa contexto demo determinista.
Esto permite que judges validen UX y flujo completo sin acceder a sistemas
privados. La evidencia debe distinguir claramente `mode=demo` de `mode=gemini`
o `mode=dynatrace_mcp`.
