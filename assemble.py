#!/usr/bin/env python3
"""Rebuild the one-paste profile files from their parts.

    python3 seraphs-crypt/assemble.py

profile-bio.html is the source of truth for content; profile-css*.txt for
styling. This regenerates:

    profile-bio.txt            <- identical copy of profile-bio.html
    profile-complete-lean.txt  <- <style>lean css</style> + bio   (About Me)
    profile-complete.txt       <- <style>full css</style> + bio   (reference)

Each output keeps the "PASTE THIS INTO" header that tells you which JanitorAI
field it belongs in. See PASTE-HERE.md.
"""

import pathlib
import re

HERE = pathlib.Path(__file__).parent
BAR = "=" * 74


def strip_header(text):
    """Remove a leading PASTE-THIS-INTO banner, HTML or CSS flavoured."""
    for pattern in (r"\A<!--\s*=+.*?=+\s*-->\s*", r"\A/\*\s*=+.*?=+\s*\*/\s*"):
        match = re.match(pattern, text, re.DOTALL)
        if match and "PASTE THIS INTO:" in match.group(0):
            return text[match.end():]
    return text


def header(kind, title, lines):
    body = "\n".join([f"   {title}", f"   {BAR}"] + [f"   {l}" if l else "" for l in lines])
    if kind == "html":
        return f"<!-- {BAR}\n{body}\n     {BAR} -->\n\n"
    return f"/* {BAR}\n{body}\n   {BAR} */\n\n"


def read(name):
    return strip_header((HERE / name).read_text(encoding="utf-8"))


bio = read("profile-bio.html")

TARGETS = [
    ("profile-bio.txt", None, [
        "THE SERAPH'S CRYPT — BIO ONLY  (no site-wide styling)",
        ["PASTE THIS INTO:  JanitorAI -> Settings -> About Me",
         "",
         "Inline styles only — no <style> block, so this survives any sanitizer.",
         "It styles the bio itself but leaves the rest of the page alone.",
         "",
         "Want the page styled too? Paste profile-complete-lean.txt instead.",
         "Identical copy lives at profile-bio.html."]]),
    ("profile-complete-lean.txt", "profile-css-lean.txt", [
        "THE SERAPH'S CRYPT — ONE-PASTE PROFILE  (styling + bio)",
        ["PASTE THIS INTO:  JanitorAI -> Settings -> About Me",
         "",
         "Do NOT paste this into the CSS Editor. Line 1 below is <style>,",
         "which is HTML, not CSS — the editor would reject the whole sheet",
         "and nothing would be styled.",
         "",
         "This is the file you want. See PASTE-HERE.md."]]),
    ("profile-complete.txt", "profile-css.txt", [
        "THE SERAPH'S CRYPT — ONE-PASTE PROFILE  (heavy / reference only)",
        ["PASTE THIS INTO:  JanitorAI -> Settings -> About Me",
         "",
         "Do NOT paste this into the CSS Editor — line 1 is <style>, which is",
         "HTML, not CSS.",
         "",
         "PREFER profile-complete-lean.txt INSTEAD. The stylesheet below is",
         "built on .character-card__* class names that JanitorAI does not use,",
         "so most of it matches nothing and does nothing. Kept for reference."]]),
]

for name, css_name, (title, lines) in TARGETS:
    parts = [header("html", title, lines)]
    if css_name:
        parts += ["<style>\n", read(css_name).strip(), "\n</style>\n\n"]
    parts.append(bio)
    (HERE / name).write_text("".join(parts), encoding="utf-8")
    print(f"wrote {name}")
