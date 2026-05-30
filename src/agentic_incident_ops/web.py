from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

from .agent import run_incident_agent
from .fixtures import sample_incident


def create_app():
    app = FastAPI(title="AegisOps Incident Agent", version="0.1.0")

    @app.get("/healthz")
    def healthz() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return _html()

    @app.get("/api/sample")
    def api_sample() -> dict[str, Any]:
        return sample_incident().to_dict()

    @app.post("/api/agent/run")
    async def api_run(request: Request) -> JSONResponse:
        payload = await request.json()
        return JSONResponse(run_incident_agent(payload))

    return app


app = create_app()


def _html() -> str:
    sample_json = sample_incident().to_dict()
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AegisOps Incident Agent</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #17202a;
      --muted: #5f6f7f;
      --line: #d8e0e8;
      --surface: #ffffff;
      --band: #f4f7fb;
      --blue: #2563eb;
      --green: #15803d;
      --amber: #b45309;
      --red: #b91c1c;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--ink);
      background: var(--band);
    }}
    header {{
      padding: 28px clamp(18px, 4vw, 56px) 18px;
      background: #101827;
      color: #fff;
      border-bottom: 4px solid #35a853;
    }}
    header h1 {{
      margin: 0 0 8px;
      font-size: clamp(28px, 4vw, 44px);
      line-height: 1.08;
      letter-spacing: 0;
    }}
    header p {{
      margin: 0;
      max-width: 920px;
      color: #d8e2f0;
      font-size: 16px;
      line-height: 1.5;
    }}
    main {{
      display: grid;
      grid-template-columns: minmax(300px, 440px) minmax(0, 1fr);
      gap: 20px;
      padding: 20px clamp(18px, 4vw, 56px) 40px;
    }}
    section {{ min-width: 0; }}
    .panel {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
      box-shadow: 0 8px 22px rgba(17, 24, 39, 0.06);
    }}
    h2 {{
      margin: 0 0 12px;
      font-size: 18px;
      letter-spacing: 0;
    }}
    label {{
      display: block;
      margin: 12px 0 6px;
      font-size: 13px;
      font-weight: 700;
      color: var(--muted);
    }}
    input, textarea, select {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 10px 11px;
      font: inherit;
      background: #fff;
      color: var(--ink);
    }}
    textarea {{ min-height: 96px; resize: vertical; }}
    button {{
      margin-top: 14px;
      width: 100%;
      border: 0;
      border-radius: 6px;
      padding: 11px 14px;
      font: inherit;
      font-weight: 800;
      color: #fff;
      background: var(--blue);
      cursor: pointer;
    }}
    button:disabled {{ opacity: .64; cursor: wait; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
      margin-bottom: 16px;
    }}
    .metric {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      min-height: 88px;
    }}
    .metric b {{ display: block; font-size: 12px; color: var(--muted); }}
    .metric span {{ display: block; margin-top: 8px; font-size: 20px; font-weight: 850; }}
    .output {{ display: grid; gap: 12px; }}
    .step {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-left: 4px solid var(--green);
      border-radius: 8px;
      padding: 14px;
    }}
    .step h3 {{ margin: 0 0 6px; font-size: 16px; }}
    .step p {{ margin: 4px 0; color: var(--muted); line-height: 1.45; }}
    pre {{
      overflow: auto;
      white-space: pre-wrap;
      word-break: break-word;
      background: #0f172a;
      color: #dceafe;
      border-radius: 8px;
      padding: 14px;
      min-height: 180px;
    }}
    .badge {{
      display: inline-block;
      border-radius: 999px;
      padding: 4px 8px;
      margin-right: 6px;
      font-size: 12px;
      font-weight: 800;
      color: #fff;
      background: var(--amber);
    }}
    @media (max-width: 900px) {{
      main {{ grid-template-columns: 1fr; }}
      .grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>AegisOps Incident Agent</h1>
    <p>Gemini-powered incident response with Dynatrace MCP context, approval-gated remediation, and evidence packaging for Devpost judging.</p>
  </header>
  <main>
    <section class="panel">
      <h2>Incident Intake</h2>
      <label for="title">Title</label>
      <input id="title" value="{sample_json['title']}">
      <label for="service">Service</label>
      <input id="service" value="{sample_json['service']}">
      <label for="severity">Severity</label>
      <select id="severity">
        <option>SEV-1</option>
        <option selected>SEV-2</option>
        <option>SEV-3</option>
        <option>SEV-4</option>
      </select>
      <label for="symptoms">Symptoms</label>
      <textarea id="symptoms">{chr(10).join(sample_json['symptoms'])}</textarea>
      <label for="change">Suspected change</label>
      <textarea id="change">{sample_json['suspected_change']}</textarea>
      <label for="impact">Business impact</label>
      <textarea id="impact">{sample_json['business_impact']}</textarea>
      <button id="run">Run triage</button>
    </section>
    <section>
      <div class="grid">
        <div class="metric"><b>Track</b><span>Dynatrace</span></div>
        <div class="metric"><b>Runtime</b><span>Cloud Run</span></div>
        <div class="metric"><b>Action Gate</b><span>Human</span></div>
      </div>
      <div class="panel output" id="result">
        <h2>Agent Run</h2>
        <p><span class="badge">ready</span>Submit an incident to generate the plan, actions, and evidence digest.</p>
        <pre id="json"></pre>
      </div>
    </section>
  </main>
  <script>
    const runButton = document.getElementById('run');
    const result = document.getElementById('result');
    function payload() {{
      return {{
        title: document.getElementById('title').value,
        service: document.getElementById('service').value,
        severity: document.getElementById('severity').value,
        symptoms: document.getElementById('symptoms').value,
        suspected_change: document.getElementById('change').value,
        business_impact: document.getElementById('impact').value
      }};
    }}
    function render(data) {{
      const steps = data.plan.map(step => `
        <div class="step">
          <h3>${{step.name}}</h3>
          <p>${{step.intent}}</p>
          <p><b>Tool:</b> ${{step.tool}}</p>
        </div>`).join('');
      result.innerHTML = `
        <h2>${{data.summary}}</h2>
        ${{steps}}
        <pre>${{JSON.stringify(data, null, 2)}}</pre>`;
    }}
    runButton.addEventListener('click', async () => {{
      runButton.disabled = true;
      runButton.textContent = 'Running triage';
      try {{
        const response = await fetch('/api/agent/run', {{
          method: 'POST',
          headers: {{'Content-Type': 'application/json'}},
          body: JSON.stringify(payload())
        }});
        render(await response.json());
      }} finally {{
        runButton.disabled = false;
        runButton.textContent = 'Run triage';
      }}
    }});
  </script>
</body>
</html>"""
