#!/usr/bin/env python3
"""MCP server for writing durable notes into the second-brain wiki."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import subprocess

import yaml
from mcp.server.fastmcp import FastMCP

import wiki_tools


ROOT = pathlib.Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
ANALYSES_DIR = WIKI_DIR / "analyses"
ALLOWED_PAGE_DIRS = {
    "sources": WIKI_DIR / "sources",
    "entities": WIKI_DIR / "entities",
    "concepts": WIKI_DIR / "concepts",
    "analyses": WIKI_DIR / "analyses",
}
MAX_READ_CHARS = 50000


def slugify(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    if not slug:
        raise ValueError("A non-empty title or slug is required.")
    return slug[:90].strip("-")


def ensure_bilingual_pair(english: str, chinese: str, field: str) -> None:
    if not english.strip() or not chinese.strip():
        raise ValueError(f"{field} requires both English and Simplified Chinese text.")


def zh_blockquote(text: str) -> str:
    return "\n".join(f"> {line}" if line else ">" for line in text.strip().splitlines())


def safe_page_path(slug: str) -> pathlib.Path:
    clean_slug = slugify(slug)
    candidates = [
        directory / f"{clean_slug}.md" for directory in ALLOWED_PAGE_DIRS.values()
    ]
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(f"No wiki page found for slug '{clean_slug}'.")


def append_log_update(title: str, touched: list[str]) -> None:
    today = dt.date.today().isoformat()
    touched_links = ", ".join(f"[[{slug}]]" for slug in touched) if touched else "N/A"
    entry = (
        f"\n## [{today}] UPDATE | {title}\n"
        f"* **Action:** Saved durable knowledge through the Second Brain MCP server.\n"
        f"* **Source Created:** N/A (MCP conversation capture)\n"
        f"* **Touched:** {touched_links}\n"
    )
    wiki_tools.LOG_PATH.open("a", encoding="utf-8").write(entry)


def rebuild_index() -> None:
    subprocess.run(
        [
            "/root/.openclaw/.venv/bin/python",
            str(ROOT / "scripts" / "wiki_tools.py"),
            "rebuild-index",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


INSTRUCTIONS = """
Use this server when the user explicitly wants to search, read, or save durable
knowledge in the local Second Brain wiki at /root/.openclaw/second-brain.
All saved wiki content must be bilingual: English first, then Simplified Chinese
in a Markdown blockquote on the next line. Do not use this server for temporary
scratch notes or unsourced claims that the user has not asked to keep.
"""

mcp = FastMCP(
    "second-brain",
    instructions=INSTRUCTIONS,
    host="0.0.0.0",
    port=8765,
    streamable_http_path="/mcp",
    sse_path="/sse",
)


@mcp.tool()
def search_wiki(query: str, limit: int = 10) -> list[dict[str, str]]:
    """Search the maintained wiki pages. Use this before creating new notes or links."""
    if not query.strip():
        raise ValueError("query cannot be empty")
    pages = wiki_tools.load_pages()
    terms = [term.lower() for term in re.findall(r"\w+", query)]
    scored: list[tuple[int, dict[str, object]]] = []
    for page in pages:
        haystack = " ".join(
            [
                str(page["title"]),
                str(page["summary_en"]),
                str(page["summary_zh"]),
                str(page["text"]),
            ]
        ).lower()
        score = sum(haystack.count(term) for term in terms)
        if score:
            scored.append((score, page))
    scored.sort(key=lambda item: (-item[0], str(item[1]["title"]).lower()))
    return [
        {
            "score": str(score),
            "slug": str(page["stem"]),
            "type": str(page["type"]),
            "title": str(page["title"]),
            "path": f"wiki/{pathlib.Path(page['rel']).as_posix()}",
            "summary_en": str(page["summary_en"]),
            "summary_zh": str(page["summary_zh"]),
        }
        for score, page in scored[: max(1, min(limit, 25))]
    ]


@mcp.tool()
def read_wiki_page(slug: str) -> dict[str, str]:
    """Read a wiki page by canonical slug, such as openai, ai-agents, or a source slug."""
    path = safe_page_path(slug)
    text = path.read_text(encoding="utf-8")
    truncated = len(text) > MAX_READ_CHARS
    if truncated:
        text = text[:MAX_READ_CHARS] + "\n\n[TRUNCATED]\n"
    return {
        "slug": path.stem,
        "path": path.relative_to(ROOT).as_posix(),
        "truncated": str(truncated).lower(),
        "content": text,
    }


@mcp.tool()
def list_recent_sources(limit: int = 10) -> list[dict[str, str]]:
    """List recently modified source pages for context before saving new knowledge."""
    source_dir = WIKI_DIR / "sources"
    paths = sorted(source_dir.glob("*.md"), key=lambda path: path.stat().st_mtime, reverse=True)
    results = []
    for path in paths[: max(1, min(limit, 30))]:
        text = path.read_text(encoding="utf-8")
        frontmatter = wiki_tools.parse_frontmatter(text)
        results.append(
            {
                "slug": path.stem,
                "title": wiki_tools.page_title(path, text, frontmatter),
                "path": path.relative_to(ROOT).as_posix(),
            }
        )
    return results


@mcp.tool()
def save_knowledge_note(
    title_en: str,
    title_zh: str,
    summary_en: str,
    summary_zh: str,
    body_en: str,
    body_zh: str,
    related_slugs: list[str] | None = None,
    tags: list[str] | None = None,
) -> dict[str, str]:
    """Save durable conversation knowledge as a bilingual analysis page.

    Use this when the user says a finding, synthesis, decision, or explanation is
    worth keeping in the second brain. This creates a new page under
    wiki/analyses/ and updates wiki/index.md and wiki/log.md.
    """
    ensure_bilingual_pair(title_en, title_zh, "title")
    ensure_bilingual_pair(summary_en, summary_zh, "summary")
    ensure_bilingual_pair(body_en, body_zh, "body")

    ANALYSES_DIR.mkdir(parents=True, exist_ok=True)

    today = dt.date.today().isoformat()
    slug = f"{today.replace('-', '')}_mcp_{slugify(title_en)}"
    path = ANALYSES_DIR / f"{slug}.md"
    counter = 2
    while path.exists():
        path = ANALYSES_DIR / f"{slug}-{counter}.md"
        counter += 1

    clean_tags = [slugify(tag) for tag in tags or ["synthesis"]]
    related = []
    for item in related_slugs or []:
        try:
            related.append(safe_page_path(item).stem)
        except FileNotFoundError:
            related.append(slugify(item))

    related_links = ", ".join(f"[[{item}]]" for item in related) if related else "N/A"
    frontmatter = yaml.safe_dump(
        {
            "type": "analysis",
            "title": title_en,
            "aliases": [title_zh],
            "date_created": today,
            "source": "MCP conversation capture",
            "tags": clean_tags,
            "summary_en": summary_en,
            "summary_zh": summary_zh,
        },
        allow_unicode=True,
        sort_keys=False,
    ).strip()
    content = f"""---
{frontmatter}
---

# {title_en}
{zh_blockquote(title_zh)}

## Summary
{summary_en.strip()}
{zh_blockquote(summary_zh)}

## Knowledge
{body_en.strip()}
{zh_blockquote(body_zh)}

## Related
{related_links}
> 相关页面：{related_links}
"""
    path.write_text(content, encoding="utf-8")
    rebuild_index()
    append_log_update(title_en, [path.stem])
    return {
        "status": "created",
        "slug": path.stem,
        "path": path.relative_to(ROOT).as_posix(),
    }


@mcp.tool()
def get_wiki_operating_rules() -> dict[str, str]:
    """Return the key write rules this MCP server follows for the wiki."""
    return {
        "raw": "Never modify raw/. Raw files are immutable source documents.",
        "bilingual": "Generated wiki content must be English first, then Simplified Chinese in a blockquote on the next line.",
        "slugs": "Use lowercase canonical slugs for filenames and wikilink targets.",
        "writes": "Conversation captures are saved under wiki/analyses/ and logged as UPDATE entries.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="MCP transport to serve.",
    )
    parser.add_argument("--host", default="0.0.0.0", help="HTTP host for sse/http transports.")
    parser.add_argument("--port", type=int, default=8765, help="HTTP port for sse/http transports.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    mcp.settings.host = args.host
    mcp.settings.port = args.port
    mcp.run(transport=args.transport)


if __name__ == "__main__":
    main()
