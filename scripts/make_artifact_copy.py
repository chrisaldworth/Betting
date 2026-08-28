#!/usr/bin/env python3
"""Write the artifact-ready copy of dashboard.html (head/body wrapper stripped,
title + font link + style + body content only) to the path given as argv[1].

The Artifact publish flow wraps pages in its own document skeleton, so the
published copy must not carry <!doctype>/<html>/<head>/<body> tags. Publishing
the SAME output path keeps the same artifact URL.

Usage: python3 scripts/make_artifact_copy.py /path/to/settling-room.html
Run generate_log.py (or generate_dashboard.py) first so dashboard.html is fresh.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: make_artifact_copy.py OUTPUT_PATH")
    src = (ROOT / "dashboard.html").read_text()
    title = re.search(r"<title>.*?</title>", src, re.S).group(0)
    link = re.search(r'<link rel="stylesheet"[^>]*>', src).group(0)
    style = re.search(r"<style>.*?</style>", src, re.S).group(0)
    body = re.search(r"<body>(.*)</body>", src, re.S).group(1)
    out = Path(sys.argv[1])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(title + "\n" + link + "\n" + style + "\n" + body)
    print(f"artifact copy written to {out}")


if __name__ == "__main__":
    main()
