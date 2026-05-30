# Devpost form draft

## Project name

AegisOps Incident Agent

## Tagline

Gemini and Dynatrace MCP agent for approval-gated incident response.

## Partner track

Dynatrace

## Project URL

https://jechaviz.github.io/google_cloud_rapid_agent_hackathon_web/

## Repository URL

TODO_PUBLIC_REPO_URL

## Video URL

TODO_VIDEO_URL

## Description

AegisOps is a web-based incident operations agent for SRE and DevOps teams. It
takes an active incident, collects structured context, uses Dynatrace MCP for
observability intelligence, reasons with Gemini on Google Cloud, and prepares
approval-gated remediation steps with an evidence pack for audit and postmortem.

The demo starts with a checkout latency incident after a canary release. The
agent classifies severity and impact, selects a Dynatrace MCP investigation
tool, correlates the suspected Cloud Run revision, proposes a reversible traffic
shift, and generates a SHA-256 evidence digest. The default mode keeps all
mutating actions gated by human approval.

## Technologies used

- Google Cloud Run
- Gemini via Google GenAI SDK
- Google Cloud Secret Manager deployment path
- Dynatrace MCP server
- Vlang
- Vue3 CDN + SFC + UnoCSS
- Playwright for authorized Devpost form automation

## Data sources

- Sample incident payload included in this repo for public judging.
- Optional Dynatrace MCP telemetry from an authorized Dynatrace environment.
- Optional Google Cloud Run metrics/log references from the deployed service.

## Findings and learnings

The most important incident response improvement is not fully autonomous
rollback. It is reliable context gathering, safe action framing, and evidence
capture while the incident commander stays in control. MCP makes observability
context tool-native for agents, and Cloud Run gives a practical path to a
judgable hosted product.

## What is next

- Add real Cloud Logging queries as a Google Cloud tool.
- Add post-incident review generation.
- Add Slack/PagerDuty handoff behind the same approval gate.
- Add ADK Agent Engine deployment once live MCP credentials are stable.
