# Evidence pack

Objetivo: dejar recibos reproducibles para judges y para el formulario Devpost.
No subir secretos, tokens, emails reales, nombres de clientes ni PII.

## Artefactos obligatorios

- `evidence/sample_agent_run.json`: salida del agente en modo demo.
- `evidence/local_ui.png`: screenshot de UI local con plan generado.
- `evidence/cloud_run_health.txt`: respuesta de `/healthz` en hosted URL.
- `evidence/cloud_run_service.txt`: salida redacted de `gcloud run services describe`.
- `evidence/dynatrace_mcp_tools.txt`: tool list o screenshot redacted.
- `evidence/video_transcript.md`: transcript final de demo.
- `evidence/devpost_form_prefill.png`: screenshot del draft antes del submit.

## Comandos

```powershell
python -m unittest discover
python -m agentic_incident_ops --sample --output evidence/sample_agent_run.json
uvicorn agentic_incident_ops.web:app --host 127.0.0.1 --port 8080
```

Cloud Run:

```powershell
gcloud run services describe aegisops-incident-agent --region us-central1 --format json > evidence/cloud_run_service.raw.json
```

Redactar cualquier valor sensible antes de commit:

```powershell
Select-String -Path evidence\* -Pattern "Bearer|token|api_key|@"
```

## Evidencia narrativa

- Problema: incident responders pierden tiempo juntando telemetria, cambio
  reciente, blast radius y acciones seguras.
- Agent value: AegisOps concentra contexto, propone remediacion reversible y
  genera evidencia/postmortem desde el primer run.
- Google proof: Gemini model y Cloud Run runtime documentados en output.
- MCP proof: Dynatrace MCP mode, endpoint redacted, tools y selected tool.
- Safety proof: `approval_required=true` por defecto y redaction test.

## No-submit evidence

El script de Devpost captura `evidence/devpost_form_prefill.png` despues de
llenar campos que pudo detectar. El click final de submit queda bloqueado salvo
con `--submit` y `CONFIRM_DEVPOST_SUBMIT=YES`.
