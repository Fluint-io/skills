#!/usr/bin/env python3
"""Generate the Grok packaging from the Claude plugins. Run after changing any skill.

- .grok-plugin/marketplace.json: a copy of .claude-plugin/marketplace.json, for Grok Build,
  which probes the Grok-named file first.
- grok/skills/<name>.md: one self-contained file per skill for grok.com and the Grok apps,
  which save skills from a single file and have no plugin namespaces or reference folders.
  Each play's reference files are appended to its body, and Claude-only wording is rewritten.

Usage: bin/build-grok.py          write the files
       bin/build-grok.py --check  exit 1 if the committed files are stale
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONNECT = "add it at grok.com/connectors (New Connector, then Custom, URL `https://mcp.fluint.io/mcp`)"


def grokify(text):
    text = re.sub(r"(?<![\w-])/?fluint:olli\b", "the olli skill", text)
    # Grok has no plugin namespaces; the plays keep their loop-* names there.
    text = re.sub(r"\bfluint:\*", "loop-*", text)
    text = re.sub(r"\bfluint:([a-z][a-z-]*)", r"loop-\1", text)
    text = re.sub(r"in\s+Claude Code run `/mcp` and\s+authenticate `loop`", "in Grok " + CONNECT, text)
    text = re.sub(r"\(`/mcp`, then\s+authenticate `loop`\)", "(at grok.com/connectors: New Connector, then Custom, URL `https://mcp.fluint.io/mcp`)", text)
    text = re.sub(r"https://raw\.githubusercontent\.com/Fluint-io/skills/main/INSTALL\.md", "https://app.fluint.io/install", text)
    text = re.sub(r"use the matching play's method through the Skill\s+tool", "use the matching loop-* skill's method", text)
    return text


def bundle(skill_dir, name):
    text = (skill_dir / "SKILL.md").read_text()
    text = re.sub(r"^name: .*$", f"name: {name}", text, count=1, flags=re.M)
    refs = sorted((skill_dir / "references").glob("*.md")) if (skill_dir / "references").is_dir() else []
    if refs:
        text = text.rstrip("\n") + "\n\n---\n\n# Reference files\n\nThe `references/...` files this skill reads are included below, in full.\n"
        for r in refs:
            text += f"\n## references/{r.name}\n\n" + r.read_text().strip("\n") + "\n"
    return grokify(text)


def outputs():
    out = {".grok-plugin/marketplace.json": (ROOT / ".claude-plugin/marketplace.json").read_text()}
    out["grok/skills/olli.md"] = bundle(ROOT / "plugins/fluint/skills/olli", "olli")
    for d in sorted((ROOT / "plugins/fluint/skills").iterdir()):
        if d.name != "olli" and (d / "SKILL.md").exists():
            out[f"grok/skills/loop-{d.name}.md"] = bundle(d, f"loop-{d.name}")
    return out


def main():
    check = "--check" in sys.argv
    out = outputs()
    stale = []
    existing = set(p.relative_to(ROOT).as_posix() for p in (ROOT / "grok/skills").glob("*.md")) if (ROOT / "grok/skills").is_dir() else set()
    for path, content in out.items():
        p = ROOT / path
        if not p.exists() or p.read_text() != content:
            stale.append(path)
            if not check:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(content)
    for orphan in existing - set(out):
        stale.append(orphan)
        if not check:
            (ROOT / orphan).unlink()
    if check and stale:
        print("Grok packaging is stale; run bin/build-grok.py:\n  " + "\n  ".join(stale))
        sys.exit(1)
    print(("checked " if check else "wrote ") + f"{len(out)} files" + (f", {len(stale)} changed" if stale else ", none changed"))


if __name__ == "__main__":
    main()
