from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agent import run_incident_agent
from .fixtures import sample_incident


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the AegisOps incident agent.")
    parser.add_argument("--sample", action="store_true", help="Run the built-in sample incident.")
    parser.add_argument("--input", type=Path, help="Path to incident JSON.")
    parser.add_argument("--output", type=Path, help="Write result JSON to this path.")
    args = parser.parse_args()

    if args.input:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
    else:
        payload = sample_incident().to_dict()

    result = run_incident_agent(payload)
    text = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
