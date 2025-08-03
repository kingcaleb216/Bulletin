#!/usr/bin/env python3
import re
import sys
from pathlib import Path

# ==== PASTE YOUR TEXT BETWEEN THE TRIPLE QUOTES BELOW ====
TEXT = r"""
1Vindicate me, O God, and defend my cause
against an ungodly people,
from the deceitful and unjust man
deliver me!
2For you are the God in whom I take refuge;
why have you rejected me?
Why do I go about mourning
because of the oppression of the enemy?

3Send out your light and your truth;
let them lead me;
let them bring me to your holy hill
and to your dwelling!
4Then I will go to the altar of God,
to God my exceeding joy,
and I will praise you with the lyre,
O God, my God.

5Why are you cast down, O my soul,
and why are you in turmoil within me?
Hope in God; for I shall again praise him,
my salvation and my God.
"""
# =========================================================

VERSE_START = re.compile(r'^\s*(\d+)(.*)$')      # "1Be gracious..." -> (1, "Be gracious...")
PUNCT_FOOTNOTE = re.compile(r'([,;:])([a-z])\b') # ";b" -> ";"

def parse_verses(text: str):
    verses = []
    cur_num = None
    cur_txt = []

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        m = VERSE_START.match(line)
        if m:
            if cur_num is not None:
                verses.append((cur_num, " ".join(cur_txt).strip()))
            cur_num = int(m.group(1))
            rest = m.group(2).lstrip()
            cur_txt = [rest] if rest else []
        else:
            if cur_num is None:
                continue
            cur_txt.append(line)

    if cur_num is not None:
        verses.append((cur_num, " ".join(cur_txt).strip()))
    return verses

def clean_text(s: str) -> str:
    s = re.sub(r'\s+', ' ', s).strip()
    s = PUNCT_FOOTNOTE.sub(r'\1', s)  # strip single-letter footnotes after punctuation
    return s

def to_html(verses):
    parts = []
    for num, txt in verses:
        txt = clean_text(txt)
        parts.append(f'<p><b>{num}</b> {txt}</p>')
    return "\n\n            ".join(parts)

def main():
    if TEXT.strip() and TEXT.strip() != "PASTE YOUR PSALM OR PASSAGE HERE":
        inp = TEXT
    elif len(sys.argv) > 1:
        inp = Path(sys.argv[1]).read_text(encoding="utf-8")
    else:
        inp = sys.stdin.read()

    verses = parse_verses(inp)
    html = to_html(verses)
    print(html)

if __name__ == "__main__":
    main()
