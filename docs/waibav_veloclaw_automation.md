# WAIBAv and Veloclaw automation

This package uses the local V automation ecosystem to make the Devpost delivery
repeatable without storing credentials in source control.

## WAIBAv

Playbook:

```powershell
v run C:\git\v_projects\waibav validate automation\waibav_submission_ready.playbook.yml prod
v run C:\git\v_projects\waibav plan automation\waibav_submission_ready.playbook.yml prod
v run C:\git\v_projects\waibav audit automation\waibav_submission_ready.playbook.yml prod
v run C:\git\v_projects\waibav run automation\waibav_submission_ready.playbook.yml prod
```

Generated receipts:

- `evidence/automation/waibav_submission_receipt.json`
- `evidence/automation/waibav_submission_trace.jsonl`
- `evidence/automation/TASK_STATUS.md`

The playbook checks the local profile source, profile-derived secure input
template, V product repo, Vue demo repo, V evaluation evidence, Devpost draft,
and hosted dashboard URL. It also records a mock browser-open contract for the
judging URL so the flow can be replayed in CI/dry-run mode.

## Veloclaw

Veloclaw is used as the policy and receipt layer around automation. Recommended
state location for this contest:

```powershell
$state = "C:\git\v_projects\contests\worth_it\google_cloud_rapid_agent_hackathon\evidence\veloclaw_state"
v run C:\git\v_projects\veloclaw policy-check --state $state --capability "run:waiba@automation[env=prod,playbook=automation/waibav_submission_ready.playbook.yml]"
v run C:\git\v_projects\veloclaw git-snapshot --state $state --repo C:\git\v_projects\google_cloud_rapid_agent_hackathon
v run C:\git\v_projects\veloclaw git-snapshot --state $state --repo C:\git\websites\google_cloud_rapid_agent_hackathon
```

Generated Veloclaw state is local evidence. Commit only redacted, useful
receipts, and keep raw credentials or browser session data out of the repo.

## Credential policy

- Account creation and form filling use `jesus.cgalaviz@gmail.com` only when the
  user has authorized that flow.
- Passwords and provider secrets stay in VImport vault refs.
- CAPTCHA, payment, unexpected permissions, and final submit prompts are human
  handoff gates.
