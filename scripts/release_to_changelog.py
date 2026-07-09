#!/usr/bin/env python3
"""Transform a ballboy release-note file into a ballboy-docs changelog page.

Implements the transform documented in CHANGELOG-SYNC.md exactly. Stdlib only.

Usage:
    python3 scripts/release_to_changelog.py <path-to-release-note.md> [--out PATH]

By default the page is written to content/docs/changelog/{version}.md
(relative to the repo root, resolved from this script's location) so the
command works regardless of the caller's current working directory.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CHANGELOG_DIR = REPO_ROOT / "content" / "docs" / "changelog"

EM_DASH = "—"


def parse_release_note(text: str) -> tuple[dict, str]:
    """Split a release-note file into its frontmatter dict and body string."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("release note is missing opening frontmatter delimiter (---)")

    frontmatter: dict[str, str] = {}
    i = 1
    while i < len(lines) and lines[i].strip() != "---":
        line = lines[i]
        if line.strip() and ":" in line:
            key, _, value = line.partition(":")
            frontmatter[key.strip()] = value.strip()
        i += 1
    if i >= len(lines):
        raise ValueError("release note is missing closing frontmatter delimiter (---)")

    body = "\n".join(lines[i + 1 :]).strip("\n")
    return frontmatter, body


def unquote(value: str) -> str:
    """Strip a YAML double-quoted scalar down to its raw string value."""
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        inner = value[1:-1]
        return inner.replace('\\"', '"').replace("\\\\", "\\")
    return value


def escape_yaml_double_quoted(value: str) -> str:
    """Escape a raw string for embedding in a double-quoted YAML scalar."""
    return value.replace("\\", "\\\\").replace('"', '\\"')


def compute_weight(version: str) -> int:
    """weight = 100000 - (major*10000 + minor*100 + patch); see CHANGELOG-SYNC.md."""
    match = re.fullmatch(r"v(\d+)\.(\d+)\.(\d+)", version)
    if not match:
        raise ValueError(f"version {version!r} does not match vMAJOR.MINOR.PATCH")
    major, minor, patch = (int(part) for part in match.groups())
    if minor >= 100 or patch >= 100:
        raise ValueError(
            f"version {version!r} has minor or patch >= 100; widen the weight "
            "formula multipliers per CHANGELOG-SYNC.md before proceeding "
            "(and apply the same scale to every existing page in one migration)"
        )
    return 100000 - (major * 10000 + minor * 100 + patch)


def build_changelog_page(frontmatter: dict, body: str) -> str:
    for required in ("version", "date", "title"):
        if required not in frontmatter:
            raise ValueError(f"release note frontmatter is missing required key: {required}")

    version = frontmatter["version"]
    date = frontmatter["date"]
    source_title = unquote(frontmatter["title"])

    page_title = f"{version} {EM_DASH} {source_title}"
    summary = f"{version}: {source_title}"
    weight = compute_weight(version)

    parts = [
        "---\n",
        f'title: "{escape_yaml_double_quoted(page_title)}"\n',
        f'summary: "{escape_yaml_double_quoted(summary)}"\n',
        f"date: {date}\n",
        f"weight: {weight}\n",
        "---\n",
        "\n",
        f"# {page_title}\n",
        "\n",
        f"_Released {date}_\n",
    ]
    if body:
        parts.append("\n")
        parts.append(body + "\n")
    else:
        parts.append("\n")
    return "".join(parts)


def render(source_path: Path) -> tuple[str, str]:
    """Return (version, rendered_page_text) for the given release-note file."""
    text = source_path.read_text(encoding="utf-8")
    frontmatter, body = parse_release_note(text)
    page = build_changelog_page(frontmatter, body)
    return frontmatter["version"], page


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="path to a ballboy .docs/releases/vX.Y.Z.md file")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="override the output path (default: content/docs/changelog/{version}.md)",
    )
    args = parser.parse_args(argv)

    try:
        version, page = render(args.source)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    out_path = args.out or (CHANGELOG_DIR / f"{version}.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page, encoding="utf-8")
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
