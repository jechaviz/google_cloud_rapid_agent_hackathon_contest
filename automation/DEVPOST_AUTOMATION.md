# Devpost automation

Primary automation: `automation/waibav_submission_ready.playbook.yml`

Fallback script: `scripts/devpost_submission_automation.py`

Purpose: prepare the Google Cloud Rapid Agent Hackathon Devpost package from
`submission/devpost_submission.json`, verify local/hosted evidence, and keep the
final external submit behind a human gate.

## Safety gates

- Uses a persistent browser profile so the operator can log in normally.
- Does not store credentials in repo.
- Captures a pre-submit screenshot in `evidence/devpost_form_prefill.png`.
- Does not click final submit unless both are true:
  - CLI flag `--submit`
  - environment variable `CONFIRM_DEVPOST_SUBMIT=YES`
- If Devpost shows CAPTCHA, login challenge, payment prompt, or unexpected
  confirmation, stop and let a human complete that step.

## Dry run

```powershell
v run C:\git\v_projects\waibav validate automation\waibav_submission_ready.playbook.yml prod
v run C:\git\v_projects\waibav audit automation\waibav_submission_ready.playbook.yml prod
v run C:\git\v_projects\waibav run automation\waibav_submission_ready.playbook.yml prod
```

The Python script is kept as a fallback for a workstation with Python,
Playwright, and a reviewed browser profile already configured.

## Final submit

Use only after human review:

```powershell
$env:CONFIRM_DEVPOST_SUBMIT="YES"
python scripts/devpost_submission_automation.py --submit
```

Use the logged-in Edge/Gmail session only for the authorized account
`jesus.cgalaviz@gmail.com`. CAPTCHA, payment, unexpected permissions, and final
submit confirmation stay as manual handoff gates.

## Fields source

- `submission/devpost_submission.json`
- `submission/devpost_form_draft.md`

Selectors are best-effort because Devpost fields can change. After every dry
run, inspect the browser and screenshot manually.
