from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agentic_incident_ops.agent import run_incident_agent
from agentic_incident_ops.fixtures import sample_incident
from agentic_incident_ops.redaction import redact


class IncidentAgentTests(unittest.TestCase):
    def test_sample_run_has_devpost_requirements(self) -> None:
        result = run_incident_agent(sample_incident().to_dict())

        self.assertEqual(result["track"], "agentic_incident_ops")
        self.assertEqual(result["partner_track"], "Dynatrace")
        self.assertIn("Cloud Run", result["google_integration"]["cloud_runtime"])
        self.assertGreaterEqual(len(result["plan"]), 4)
        self.assertTrue(all(action["approval_required"] for action in result["action_proposals"]))
        self.assertIn("digest_sha256", result["evidence"])

    def test_redaction_masks_tokens_and_email(self) -> None:
        text = "Bearer abc.secret token=xyz email jane@example.com"
        redacted = redact(text)

        self.assertNotIn("abc.secret", redacted)
        self.assertNotIn("xyz", redacted)
        self.assertNotIn("jane@example.com", redacted)


if __name__ == "__main__":
    unittest.main()
