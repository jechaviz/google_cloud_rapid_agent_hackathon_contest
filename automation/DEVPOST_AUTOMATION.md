# Devpost automation

Script: `scripts/devpost_submission_automation.py`

Purpose: prepare and fill the Google Cloud Rapid Agent Hackathon Devpost form
from `submission/devpost_submission.json`.

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
pip install -e .[automation]
playwright install chromium
python scripts/devpost_submission_automation.py
```

## Final submit

Use only after human review:

```powershell
$env:CONFIRM_DEVPOST_SUBMIT="YES"
python scripts/devpost_submission_automation.py --submit
```

## Fields source

- `submission/devpost_submission.json`
- `submission/devpost_form_draft.md`

Selectors are best-effort because Devpost fields can change. After every dry
run, inspect the browser and screenshot manually.
