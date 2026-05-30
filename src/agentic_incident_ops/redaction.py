from __future__ import annotations

import re

TOKEN_PATTERNS = [
    re.compile(r"(?i)(bearer\s+)[a-z0-9._\-]+"),
    re.compile(r"(?i)(api[_-]?key\s*[:=]\s*)[a-z0-9._\-]+"),
    re.compile(r"(?i)(token\s*[:=]\s*)[a-z0-9._\-]+"),
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
]


def redact(value: object) -> str:
    text = str(value)
    for pattern in TOKEN_PATTERNS:
        if pattern.pattern.startswith("[A-Za-z0-9"):
            text = pattern.sub("[redacted-email]", text)
        else:
            text = pattern.sub(lambda match: f"{match.group(1)}[redacted]", text)
    return text
