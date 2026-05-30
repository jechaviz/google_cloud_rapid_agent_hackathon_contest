# Evidence folder

Generated evidence belongs here. Commit only sanitized artifacts.

Expected files:

- `v_agent_run.json`
- `v_eval.json`
- `v_agent_run_gemini.json`
- `v_eval_gemini.json`
- `secure_external_enablement.json`
- `local_vue_dashboard.png`
- `local_vue_index.html`
- `local_v_health.txt`
- `local_v_post_run.json`
- `profile/redacted_source_manifest.json`
- `profile/application_packet.json`
- `profile_secure_inputs.template.json`
- `automation/waibav_submission_receipt.json`
- `cloud_run_health.txt`
- `cloud_run_service.txt`
- `dynatrace_mcp_tools.txt`
- `video_transcript.md`
- `devpost_form_prefill.png`

Before commit, scan for secrets:

```powershell
Get-ChildItem evidence -File | Where-Object Name -ne 'README.md' | Select-String -Pattern "Bearer|token|api_key|@"
```
