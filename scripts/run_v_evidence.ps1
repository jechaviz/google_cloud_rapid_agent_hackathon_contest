$ErrorActionPreference = "Stop"

$contestRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$productRoot = "C:\git\v_projects\google_cloud_rapid_agent_hackathon"

Push-Location $productRoot
try {
  v test .
  v run cmd\agent --sample --output (Join-Path $contestRoot "evidence\v_agent_run.json")
  v run cmd\agent eval --output (Join-Path $contestRoot "evidence\v_eval.json")
} finally {
  Pop-Location
}
