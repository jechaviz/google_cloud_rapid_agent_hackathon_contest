from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


FIELD_HINTS = {
    "project_name": ["Project name", "Title"],
    "tagline": ["Tagline", "Elevator pitch"],
    "description": ["Description", "Tell us about"],
    "project_url": ["Hosted project", "Website", "Project URL"],
    "repo_url": ["Repository", "Source code", "Code URL"],
    "video_url": ["Video", "Demo video"],
    "partner_track": ["Track", "Partner"],
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare or fill the Devpost submission form from a JSON draft."
    )
    parser.add_argument("--draft", default="submission/devpost_submission.json")
    parser.add_argument(
        "--url",
        default="https://devpost.com/submit-to/29711-google-cloud-rapid-agent-hackathon/manage/submissions",
    )
    parser.add_argument("--profile", default=str(Path.home() / ".aegisops-devpost-profile"))
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--submit", action="store_true")
    args = parser.parse_args()

    draft = json.loads(Path(args.draft).read_text(encoding="utf-8"))
    if args.submit and os.getenv("CONFIRM_DEVPOST_SUBMIT") != "YES":
        raise SystemExit("Refusing final submit. Set CONFIRM_DEVPOST_SUBMIT=YES to continue.")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit("Install automation extras first: pip install -e .[automation] && playwright install") from exc

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            args.profile,
            headless=args.headless,
            viewport={"width": 1440, "height": 1200},
        )
        page = context.new_page()
        page.goto(args.url, wait_until="domcontentloaded")

        for key, value in draft.items():
            if value is None:
                continue
            fill_best_effort(page, FIELD_HINTS.get(key, [key]), str(value))

        evidence_dir = Path("evidence")
        evidence_dir.mkdir(exist_ok=True)
        page.screenshot(path=str(evidence_dir / "devpost_form_prefill.png"), full_page=True)

        if args.submit:
            page.get_by_role("button", name="Submit").click(timeout=5000)
            page.screenshot(path=str(evidence_dir / "devpost_submitted.png"), full_page=True)
        else:
            print("Draft filled where selectors matched. Final submit was not clicked.")

        context.close()


def fill_best_effort(page, labels: list[str], value: str) -> bool:
    for label in labels:
        try:
            page.get_by_label(label, exact=False).fill(value, timeout=1200)
            return True
        except Exception:
            pass
        try:
            page.get_by_placeholder(label, exact=False).fill(value, timeout=1200)
            return True
        except Exception:
            pass
    return False


if __name__ == "__main__":
    main()
