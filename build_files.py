#!/usr/bin/env python3
"""
Build the Files page data from files/pdf/ and files/md/.

    python3 build_files.py

Writes content/files.json, which files.html lists and doc.html reads.
PDFs are linked directly so they open in the browser's own viewer; Markdown
files are converted to HTML here so doc.html can show them as a page.

Title  Markdown: front matter `title:`, else a leading "# heading",
       else the filename.  PDF: the filename.
Date   a YYYY-MM-DD filename prefix, else Markdown front matter `date:`,
       else the file's modification date.

Uses the same stdlib-only Markdown converter as build_posts.py.
"""

import datetime
import json
import pathlib
import posixpath
import re
import sys

from build_posts import auto_excerpt, markdown_to_html, parse_front_matter, unquote

ROOT = pathlib.Path(__file__).resolve().parent
PDF_DIR = ROOT / "files" / "pdf"
MD_DIR = ROOT / "files" / "md"
OUT = ROOT / "content" / "files.json"

DATE_PREFIX = re.compile(r"^(\d{4}-\d{2}-\d{2})[-_ ]?(.*)$")
LEADING_H1 = re.compile(r"^#\s+(.+)$")
ABSOLUTE = re.compile(r"^([a-z][a-z0-9+.-]*:|/|#)", re.I)


def rebase_images(html, md_path):
    """Make image paths written relative to the note work from doc.html.

    Editors like Typora, Obsidian and VS Code resolve `![](images/fig.png)`
    against the note's own folder, but doc.html lives at the site root.
    Paths that are already absolute, or already start at content/ or files/,
    are left alone.
    """
    base = md_path.parent.relative_to(ROOT).as_posix()

    def fix(m):
        src = m.group(1)
        if ABSOLUTE.match(src) or src.startswith(("content/", "files/")):
            return m.group(0)
        return 'src="%s"' % posixpath.normpath(posixpath.join(base, src))

    return re.sub(r'src="([^"]+)"', fix, html)


def human_size(n):
    for unit in ("B", "KB", "MB"):
        if n < 1024:
            return "%d %s" % (n, unit) if unit == "B" else "%.1f %s" % (n, unit)
        n /= 1024.0
    return "%.1f GB" % n


def split_name(path):
    """'2026-09-25-my_notes.md' -> ('2026-09-25', 'my_notes')"""
    stem = path.stem
    m = DATE_PREFIX.match(stem)
    if m:
        return m.group(1), (m.group(2) or m.group(1))
    return "", stem


def pretty(name):
    return re.sub(r"[-_]+", " ", name).strip() or name


def first_of(path, *candidates):
    for c in candidates:
        if c:
            return c
    return datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()


def list_dir(folder, suffixes):
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.iterdir()
                  if p.is_file() and p.suffix.lower() in suffixes
                  and not p.name.startswith("."))


def build_pdf(path):
    date, name = split_name(path)
    return {
        "title": pretty(name),
        "date": first_of(path, date),
        "size": human_size(path.stat().st_size),
        "path": path.relative_to(ROOT).as_posix(),
    }


def build_md(path):
    meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
    date, name = split_name(path)

    title = unquote(meta.get("title", ""))
    if not title:
        # Promote a leading "# heading" to the title, and drop it from the body
        # so doc.html does not show the same line twice.
        lines = body.split("\n")
        for i, line in enumerate(lines):
            if line.strip():
                m = LEADING_H1.match(line.strip())
                if m:
                    title = m.group(1).strip()
                    body = "\n".join(lines[i + 1:])
                break
    title = title or pretty(name)

    html = rebase_images(markdown_to_html(body).strip(), path)
    return {
        "id": unquote(meta.get("slug", "")) or name,
        "title": title,
        "date": first_of(path, date, unquote(meta.get("date", ""))),
        "size": human_size(path.stat().st_size),
        "path": path.relative_to(ROOT).as_posix(),
        "excerpt": unquote(meta.get("excerpt", "")) or auto_excerpt(html),
        "html": html,
    }


def newest_first(items):
    return sorted(items, key=lambda d: (d["date"], d["title"]), reverse=True)


def main():
    pdfs = [build_pdf(p) for p in list_dir(PDF_DIR, {".pdf"})]
    docs, seen = [], {}
    for p in list_dir(MD_DIR, {".md", ".markdown"}):
        d = build_md(p)
        if d["id"] in seen:
            sys.exit("Two Markdown files map to the id %r: %s and %s — rename one, "
                     "or give one a `slug:` in its front matter."
                     % (d["id"], seen[d["id"]], p.name))
        seen[d["id"]] = p.name
        docs.append(d)

    OUT.write_text(json.dumps({"pdf": newest_first(pdfs), "markdown": newest_first(docs)},
                              ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("content/files.json  %d PDF, %d Markdown" % (len(pdfs), len(docs)))
    for d in newest_first(pdfs):
        print("  PDF  %s  %-8s  %s" % (d["date"], d["size"], d["title"]))
    for d in newest_first(docs):
        print("  MD   %s  %-8s  %s" % (d["date"], d["size"], d["title"]))


if __name__ == "__main__":
    main()
