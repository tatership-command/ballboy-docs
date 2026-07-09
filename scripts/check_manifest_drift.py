#!/usr/bin/env python3
"""Compare a candidate ballboy command manifest against the committed baseline.

Prints a markdown drift report: added lines, removed lines, and a checklist
mapping each changed top-level command group to its docs page. Advisory only
— never writes/modifies any file, and always exits 0.

Usage:
    python3 scripts/check_manifest_drift.py <path-to-candidate-manifest.txt>
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = REPO_ROOT / "data" / "command-manifest.txt"
COMMANDS_DIR = REPO_ROOT / "content" / "docs" / "commands"


def load_lines(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line for line in (l.strip() for l in lines) if line]


def command_group(line: str) -> str:
    """The top-level slash-command group for a manifest line, e.g.
    'admin auto_advance' -> 'admin', 'schedule' -> 'schedule'."""
    return line.split(" ", 1)[0]


def build_report(baseline_lines: list[str], candidate_lines: list[str]) -> str:
    baseline_set = set(baseline_lines)
    candidate_set = set(candidate_lines)

    added = sorted(candidate_set - baseline_set)
    removed = sorted(baseline_set - candidate_set)

    if not added and not removed:
        return "NO DRIFT\n\nCommand manifest matches the committed baseline (`data/command-manifest.txt`)."

    lines_out: list[str] = []
    lines_out.append("## Command manifest drift detected\n")

    if added:
        lines_out.append("### Added\n")
        for line in added:
            lines_out.append(f"- `+ {line}`")
        lines_out.append("")

    if removed:
        lines_out.append("### Removed\n")
        for line in removed:
            lines_out.append(f"- `- {line}`")
        lines_out.append("")

    changed_groups: dict[str, list[str]] = {}
    for line in added:
        changed_groups.setdefault(command_group(line), []).append(f"added `{line}`")
    for line in removed:
        changed_groups.setdefault(command_group(line), []).append(f"removed `{line}`")

    lines_out.append("### Checklist\n")
    for group in sorted(changed_groups):
        page = COMMANDS_DIR / f"{group}.md"
        page_display = f"content/docs/commands/{group}.md"
        exists_note = "" if page.exists() else " (page does not exist yet — create it)"
        for change in changed_groups[group]:
            lines_out.append(f"- [ ] Update {page_display} — {change}{exists_note}")

    return "\n".join(lines_out).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path, help="path to a candidate command-manifest.txt")
    parser.add_argument(
        "--baseline",
        type=Path,
        default=BASELINE_PATH,
        help="override the baseline manifest path (default: data/command-manifest.txt)",
    )
    args = parser.parse_args(argv)

    try:
        baseline_lines = load_lines(args.baseline)
        candidate_lines = load_lines(args.candidate)
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(build_report(baseline_lines, candidate_lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
