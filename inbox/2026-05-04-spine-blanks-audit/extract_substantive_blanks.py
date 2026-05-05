#!/usr/bin/env python3
"""Extract substantive [SOURCE REQUIRED] / [DECISION REQUIRED] / [LOGIC TO BE CONFIRMED]
markers from the clean-build repo, excluding:
  - definition tables (lines that DEFINE the marker syntax)
  - SOP boilerplate listing the markers as a vocabulary
  - 90_archive/

A line is "substantive" if the marker appears in context where it represents
an actual unknown — i.e. a thing has been NAMED with the marker attached,
not the marker syntax being defined or listed as part of an SOP vocabulary.

Heuristic: skip lines where the marker is wrapped in backticks AND no
other content gives it subject-matter (i.e. the line is a vocab entry).
"""
import os, re, json
from pathlib import Path

REPO = Path("/tmp/tmp.xjxTifV629/clean-build")
MARKERS = ["SOURCE REQUIRED", "DECISION REQUIRED", "LOGIC TO BE CONFIRMED"]

# Patterns that indicate a definition / vocab-listing / SOP boilerplate line
SKIP_PATTERNS = [
    re.compile(r"^\s*[-*]\s*`?\[(?:SOURCE REQUIRED|DECISION REQUIRED|LOGIC TO BE CONFIRMED)\]`?\s*[—-]"),  # bullet-with-definition
    re.compile(r"\|\s*`?\[(?:SOURCE REQUIRED|DECISION REQUIRED|LOGIC TO BE CONFIRMED)\]`?\s*\|"),  # table cell defining
    re.compile(r"`\[(?:LOGIC TO BE CONFIRMED|SOURCE REQUIRED|DECISION REQUIRED)\]`(?:\s*[/,]\s*`\[(?:LOGIC TO BE CONFIRMED|SOURCE REQUIRED|DECISION REQUIRED)\]`){1,}"),  # listing all three together
    re.compile(r"^\s*-\s*`\[(?:LOGIC TO BE CONFIRMED|SOURCE REQUIRED|DECISION REQUIRED)\]`\s*$"),  # bullet vocab
    re.compile(r"\bMark with appropriate token\b", re.I),
    re.compile(r"\bsmallest correct token\b", re.I),
    re.compile(r"\buncertainty tokens?\b", re.I),
    re.compile(r"\bTokens\*?\*?\s*[:`]", re.I),
    re.compile(r"\bbibliography integrity\b", re.I),
    re.compile(r"\bmark `?\[(?:SOURCE REQUIRED|DECISION REQUIRED|LOGIC TO BE CONFIRMED)\]`?\s*(?:and|or|,|—|-)", re.I),
    re.compile(r"`?\[(?:LOGIC TO BE CONFIRMED|SOURCE REQUIRED|DECISION REQUIRED)\]`?,\s*`?\[(?:LOGIC TO BE CONFIRMED|SOURCE REQUIRED|DECISION REQUIRED)\]`?"),  # listing two
    re.compile(r"\btreat (?:as|it) `?\[SOURCE REQUIRED\]`?", re.I),
    re.compile(r"\bdo not (?:treat|launder|invent)\b", re.I),
    re.compile(r"^\s*<[^>]+>\s*$"),  # XML/MDC tags
]

def is_skip_line(line: str) -> bool:
    for pat in SKIP_PATTERNS:
        if pat.search(line):
            return True
    return False

def collect():
    results = {m: [] for m in MARKERS}
    for root, dirs, files in os.walk(REPO):
        # Exclude 90_archive and .git
        dirs[:] = [d for d in dirs if d not in ("90_archive", ".git", "node_modules")]
        for fn in files:
            if not (fn.endswith(".md") or fn.endswith(".mdc")):
                continue
            path = Path(root) / fn
            rel = str(path.relative_to(REPO))
            try:
                lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            except Exception:
                continue
            for i, line in enumerate(lines):
                for marker in MARKERS:
                    if f"[{marker}]" in line:
                        if is_skip_line(line):
                            continue
                        # Pull 2 lines of context above and below for human judgement
                        start = max(0, i - 1)
                        end = min(len(lines), i + 2)
                        ctx = lines[start:end]
                        results[marker].append({
                            "file": rel,
                            "line_no": i + 1,
                            "line": line.rstrip(),
                            "context": ctx,
                        })
                        break
    return results

if __name__ == "__main__":
    out = collect()
    for m in MARKERS:
        print(f"\n========== [{m}] : {len(out[m])} substantive hits ==========")
        for hit in out[m]:
            print(f"\n--- {hit['file']}:{hit['line_no']} ---")
            print(hit["line"])
    # Also dump JSON
    with open("/home/user/workspace/sam-substantive-blanks.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"\n\nTotal: {sum(len(v) for v in out.values())}")
    print(f"  SOURCE REQUIRED: {len(out['SOURCE REQUIRED'])}")
    print(f"  DECISION REQUIRED: {len(out['DECISION REQUIRED'])}")
    print(f"  LOGIC TO BE CONFIRMED: {len(out['LOGIC TO BE CONFIRMED'])}")
