# Evidence pack

Objetivo: dejar recibos reproducibles para judges y para el formulario Devpost.
No subir secretos, tokens, emails reales, nombres de clientes ni PII.

## Artefactos obligatorios

- `evidence/v_agent_run.json`: salida del agente V en modo demo.
- `evidence/v_eval.json`: evaluador V con gates Devpost.
- `evidence/local_vue_dashboard.png`: screenshot de UI local con plan generado.
- `evidence/local_vue_index.html`: HTML del dashboard capturado para inspeccion.
- `evidence/local_v_health.txt`: salud del servidor V local.
- `evidence/local_v_post_run.json`: respuesta local de `/api/agent/run`.
- `evidence/profile/redacted_source_manifest.json`: manifest de perfil sin secretos.
- `evidence/profile/application_packet.json`: paquete de aplicacion derivado del perfil.
- `evidence/profile_secure_inputs.template.json`: campos secretos esperados como refs.
- `evidence/automation/waibav_submission_receipt.json`: readiness WAIBAv.
- `evidence/automation/waibav_submission_trace.jsonl`: trace WAIBAv sin secretos.
- `evidence/cloud_run_health.txt`: respuesta de `/healthz` en hosted URL.
- `evidence/cloud_run_service.txt`: salida redacted de `gcloud run services describe`.
- `evidence/dynatrace_mcp_tools.txt`: tool list o screenshot redacted.
- `evidence/video_transcript.md`: transcript final de demo.
- `evidence/demo_video_frame.png`: generated screenshot frame, not committed if
  binary line budget exceeds policy.
- `evidence/demo_video.webm`: generated demo clip, kept local or uploaded to a
  video host before Devpost submit.
- `evidence/devpost_form_prefill.png`: screenshot del draft antes del submit.

## Comandos

```powershell
.\scripts\run_v_evidence.ps1
v run C:\git\v_projects\google_cloud_rapid_agent_hackathon\cmd\agent serve --port 8080
v run C:\git\websites\google_cloud_rapid_agent_hackathon\tools\static_server.v C:\git\websites\google_cloud_rapid_agent_hackathon 8902
npx --yes -p playwright node scripts\record_demo.mjs
v run C:\git\v_projects\waibav run automation\waibav_submission_ready.playbook.yml prod
```

Cloud Run:

```powershell
gcloud run services describe aegisops-incident-agent --region us-central1 --format json > evidence/cloud_run_service.raw.json
```

If local `gcloud` is unavailable, run the product repo workflow
`Deploy Cloud Run` with `GCP_SA_KEY` and `GCP_PROJECT_ID` secrets.

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
- Automation proof: WAIBAv readiness receipt and Veloclaw policy receipts.

## No-submit evidence

El script de Devpost captura `evidence/devpost_form_prefill.png` despues de
llenar campos que pudo detectar. El click final de submit queda bloqueado salvo
con `--submit` y `CONFIRM_DEVPOST_SUBMIT=YES`.
