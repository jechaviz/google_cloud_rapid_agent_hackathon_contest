param(
  [int]$Port = 8080
)

$ErrorActionPreference = "Stop"

python -m agentic_incident_ops --sample --output evidence/sample_agent_run.json
uvicorn agentic_incident_ops.web:app --host 127.0.0.1 --port $Port
