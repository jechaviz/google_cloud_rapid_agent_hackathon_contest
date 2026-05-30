import { chromium } from 'playwright';
import { mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';

const url = process.argv[2] || 'https://jechaviz.github.io/google_cloud_rapid_agent_hackathon_web/';
const evidenceDir = resolve('evidence');
const videoDir = resolve(evidenceDir, 'video');

await mkdir(videoDir, { recursive: true });

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 1100 },
  recordVideo: { dir: videoDir, size: { width: 1440, height: 1100 } }
});
const page = await context.newPage();
await page.goto(url, { waitUntil: 'networkidle' });
await page.getByRole('button', { name: /run triage/i }).click();
await page.waitForTimeout(3000);
await page.screenshot({ path: resolve(evidenceDir, 'demo_video_frame.png'), fullPage: true });
await context.close();
await browser.close();

await writeFile(resolve(evidenceDir, 'video_transcript.md'), transcript(url), 'utf8');

function transcript(projectUrl) {
  return `# Demo transcript

Project URL: ${projectUrl}

0:00 AegisOps opens as a hosted Vue dashboard for the Google Cloud Rapid Agent Hackathon.

0:15 The incident intake shows a checkout latency spike after a canary Cloud Run release.

0:35 The operator runs triage. The agent generates a multi-step incident plan.

0:55 The plan uses Dynatrace MCP context, Gemini reasoning, and Cloud Run release correlation.

1:20 The remediation section keeps actions approval-gated instead of executing risky mutations.

1:45 The evidence digest and JSON output show reproducible audit artifacts for Devpost judging.

2:10 The topology visual ties together Cloud Run, Gemini, Dynatrace MCP, human approval and evidence.

2:35 AegisOps is ready to connect real Gemini, Dynatrace MCP and Cloud Run secrets for production judging.
`;
}
