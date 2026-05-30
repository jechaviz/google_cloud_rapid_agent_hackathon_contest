# Evidence folder

Generated evidence belongs here. Commit only sanitized artifacts.

Expected files:

- `sample_agent_run.json`
- `local_ui.png`
- `cloud_run_health.txt`
- `cloud_run_service.txt`
- `dynatrace_mcp_tools.txt`
- `video_transcript.md`
- `devpost_form_prefill.png`

Before commit, scan for secrets:

```powershell
Get-ChildItem evidence -File | Where-Object Name -ne 'README.md' | Select-String -Pattern "Bearer|token|api_key|@"
```
