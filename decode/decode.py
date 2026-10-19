#!/usr/bin/env python3
"""Apply a key (JSON) to the signs (signs.txt) and print the literal plaintext.

    python3 decode.py ../data/key-whole-stream.json ../data/signs.txt            # one stream
    python3 decode.py ../data/key-whole-stream.json ../data/signs.txt --by-line  # one row per line

Python 3 standard library only. signs.txt has one manuscript line per row: the line number,
a tab, then the items of the line separated by spaces. An item is either a cipher sign (a
two-digit group such as 86, a lone digit such as 0, or a letter sign such as k or gLoh) or a
run of clear text written in the letter, in square brackets.

The key's "table" gives each sign its letter. The decode is a plain lookup: nothing is chosen
or guessed here.

- Stream mode prints the cipher letters only, as one string; clear text is left out; a sign
  with no value in the key prints as [?name].
- By-line mode prints each line as "NN text": cipher letters in lower case, clear text in
  capitals inside brackets, a sign with no value as "?".
"""
import argparse
import json
import re

ITEM = re.compile(r"\[[^\]]*\]|\S+")


def read_signs(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            if raw.strip() and not raw.startswith("#"):
                line, _, items = raw.rstrip("\n").partition("\t")
                rows.append((int(line), ITEM.findall(items)))
    return rows


def letter(table, sign):
    entry = table.get(sign) or {}
    return entry.get("v")


def stream(rows, key):
    table = key["table"]
    out = []
    for _, items in rows:
        for it in items:
            if it.startswith("["):
                continue
            v = letter(table, it)
            out.append(f"[?{it}]" if v is None else v)
    return "".join(out)


def by_line(rows, key):
    table = key["table"]
    out = []
    for n, items in rows:
        parts = []
        for it in items:
            if it.startswith("["):
                parts.append(f" [{it[1:-1].upper()}] ")
            else:
                v = letter(table, it)
                parts.append("?" if v is None else v)
        out.append(f"{n:2d} {''.join(parts).strip()}")
    return "\n".join(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("key")
    ap.add_argument("signs")
    ap.add_argument("--by-line", action="store_true")
    a = ap.parse_args()
    with open(a.key, encoding="utf-8") as f:
        key = json.load(f)
    rows = read_signs(a.signs)
    print(by_line(rows, key) if a.by_line else stream(rows, key))
