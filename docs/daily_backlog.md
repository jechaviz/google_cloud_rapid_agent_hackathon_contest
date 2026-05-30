# Daily backlog

Current date: 2026-05-29.
External deadline: 2026-06-11 14:00 PDT / 15:00 America/Mexico_City.

## 2026-05-29 - Scaffold and task

- [x] Verify hackathon rules and deadline.
- [x] Pick partner track: Dynatrace.
- [x] Create MVP agent scaffold.
- [x] Create Devpost task package.
- [ ] Run local smoke tests and generate first evidence JSON.

## 2026-05-30 - Local product polish

- [ ] Install deps in venv.
- [ ] Run UI locally and capture `evidence/local_ui.png`.
- [ ] Tighten UI copy and sample incident.
- [ ] Add README screenshot if useful.

## 2026-05-31 - Gemini connection

- [ ] Configure `GEMINI_API_KEY` or Vertex path.
- [ ] Verify Gemini response in `agent_reasoning.mode=gemini`.
- [ ] Capture redacted evidence.
- [ ] Update video script with exact model used.

## 2026-06-01 - Dynatrace MCP connection

- [ ] Create/obtain Dynatrace Platform Token.
- [ ] Confirm permissions: `mcp-gateway:servers:read` and invoke.
- [ ] Set `DYNATRACE_MCP_URL` and `DYNATRACE_MCP_TOKEN`.
- [ ] Capture tool list and one safe problem/DQL response.

## 2026-06-02 - Cloud Run deploy

- [ ] Create/confirm Google Cloud project.
- [ ] Store secrets in Secret Manager.
- [ ] Run `scripts/deploy_cloud_run.ps1`.
- [ ] Capture `/healthz` and hosted URL.

## 2026-06-03 - Evidence and tests

- [ ] Run tests.
- [ ] Regenerate evidence JSON.
- [ ] Redaction scan.
- [ ] Confirm repo license visibility.

## 2026-06-04 - Credits and rough video

- [ ] Confirm Google credits/billing before credit request deadline.
- [ ] Record rough video.
- [ ] Upload rough video unlisted.
- [ ] Fill Devpost draft URLs if available.

## 2026-06-05 - Judge UX pass

- [ ] Ask a fresh reviewer to run README quickstart.
- [ ] Fix confusing UI or setup steps.
- [ ] Make description shorter and sharper.
- [ ] Update evidence checklist.

## 2026-06-06 - Production hardening

- [ ] Confirm Cloud Run cold start acceptable.
- [ ] Add request size guard if needed.
- [ ] Confirm error messages do not leak tokens.
- [ ] Verify mobile layout for Devpost judges.

## 2026-06-07 - Final video

- [ ] Record final demo.
- [ ] Produce transcript.
- [ ] Upload final public/unlisted video.
- [ ] Add video URL to submission JSON.

## 2026-06-08 - Submission automation dry run

- [ ] Install Playwright extras.
- [ ] Run Devpost automation without `--submit`.
- [ ] Capture `evidence/devpost_form_prefill.png`.
- [ ] Manually inspect every field.

## 2026-06-09 - Final repo release

- [ ] Push public repo.
- [ ] Confirm About/license detection.
- [ ] Tag `devpost-2026-final-rc1`.
- [ ] Smoke test from clean clone if time permits.

## 2026-06-10 - Freeze

- [ ] Freeze code by 20:00 America/Mexico_City.
- [ ] Only docs/URL corrections after freeze.
- [ ] Final redaction scan.
- [ ] Prepare final submit checklist.

## 2026-06-11 - Submit

- [ ] Submit by 12:00 America/Mexico_City target.
- [ ] Absolute cutoff: 15:00 America/Mexico_City.
- [ ] Capture confirmation screenshot.
- [ ] Record submitted URL and timestamp in evidence.
