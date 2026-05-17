#!/usr/bin/env python3
"""MCP server for writing durable notes into the second-brain wiki."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import pathlib
import re
import subprocess

import yaml
from mcp.server.fastmcp import FastMCP

import wiki_tools


ROOT = pathlib.Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
ANALYSES_DIR = WIKI_DIR / "analyses"
HTML_DIR = WIKI_DIR / "html"
PUBLIC_HTML_DIR = pathlib.Path(
    os.environ.get("SECOND_BRAIN_PUBLIC_HTML_DIR", "/var/www/second-brain-html")
)
SYNC_SCRIPT = ROOT / "scripts" / "hourly_git_sync.sh"
SYNC_LOG = pathlib.Path("/tmp/second-brain-mcp-sync.log")
PUBLIC_HTML_BASE_URL = os.environ.get(
    "SECOND_BRAIN_HTML_BASE_URL",
    "https://www.lucasgou.cloud/second-brain-html",
).rstrip("/")
CUSTOM_FRAMES_NAME = os.environ.get("SECOND_BRAIN_CUSTOM_FRAMES_NAME", "Second Brain HTML")
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


def html_paragraphs(text: str) -> str:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text.strip()) if part.strip()]
    if not paragraphs:
        return "<p>No content provided.</p>"
    return "\n".join(
        f"<p style=\"margin:0 0 10px;line-height:1.65;\">{html.escape(part)}</p>"
        for part in paragraphs[:6]
    )


def render_html_note_block(
    title_en: str,
    title_zh: str,
    summary_en: str,
    summary_zh: str,
    body_en: str,
    body_zh: str,
    related_links: str,
    tags: list[str],
) -> str:
    tag_html = "".join(
        "<span style=\"display:inline-flex;align-items:center;padding:3px 8px;"
        "border:1px solid #cbd5e1;border-radius:999px;background:#f8fafc;"
        f"font-size:12px;color:#334155;\">{html.escape(tag)}</span>"
        for tag in tags[:8]
    )
    return f"""
<section class="second-brain-html-note" style="border:1px solid #d0d7de;border-radius:8px;margin:18px 0;padding:18px;background:#ffffff;color:#111827;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <header style="display:grid;gap:8px;border-bottom:1px solid #e5e7eb;padding-bottom:14px;margin-bottom:14px;">
    <div style="font-size:12px;font-weight:700;letter-spacing:0;text-transform:uppercase;color:#64748b;">Second Brain Note</div>
    <h2 style="margin:0;font-size:24px;line-height:1.2;color:#0f172a;">{html.escape(title_en)}</h2>
    <blockquote style="margin:0;padding-left:12px;border-left:3px solid #94a3b8;color:#475569;">{html.escape(title_zh)}</blockquote>
    <div style="display:flex;flex-wrap:wrap;gap:6px;">{tag_html}</div>
  </header>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-bottom:14px;">
    <article style="border:1px solid #e5e7eb;border-radius:8px;padding:12px;background:#f8fafc;">
      <h3 style="margin:0 0 8px;font-size:13px;color:#475569;">Summary</h3>
      <p style="margin:0;line-height:1.6;">{html.escape(summary_en)}</p>
      <blockquote style="margin:8px 0 0;padding-left:10px;border-left:3px solid #cbd5e1;color:#475569;">{html.escape(summary_zh)}</blockquote>
    </article>
    <article style="border:1px solid #e5e7eb;border-radius:8px;padding:12px;background:#f8fafc;">
      <h3 style="margin:0 0 8px;font-size:13px;color:#475569;">Related</h3>
      <p style="margin:0;line-height:1.6;">{html.escape(related_links)}</p>
      <blockquote style="margin:8px 0 0;padding-left:10px;border-left:3px solid #cbd5e1;color:#475569;">相关页面：{html.escape(related_links)}</blockquote>
    </article>
  </div>
  <details open style="border:1px solid #e5e7eb;border-radius:8px;padding:12px;background:#fff;">
    <summary style="cursor:pointer;font-weight:700;color:#0f172a;">Knowledge Body / 知识正文</summary>
    <div style="margin-top:12px;">
      {html_paragraphs(body_en)}
      <blockquote style="margin:12px 0 0;padding-left:12px;border-left:3px solid #94a3b8;color:#475569;">
        {html_paragraphs(body_zh)}
      </blockquote>
    </div>
  </details>
</section>
""".strip()


def render_standalone_html_artifact(
    title_en: str,
    title_zh: str,
    summary_en: str,
    summary_zh: str,
    body_en: str,
    body_zh: str,
    related_links: str,
    tags: list[str],
) -> str:
    tag_html = "".join(
        f"<span class=\"tag\">{html.escape(tag)}</span>"
        for tag in tags[:12]
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title_en)}</title>
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #f8fafc;
      --panel: #ffffff;
      --text: #111827;
      --muted: #64748b;
      --line: #d0d7de;
      --soft: #eef2f7;
      --accent: #2563eb;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #0f172a;
        --panel: #111827;
        --text: #e5e7eb;
        --muted: #94a3b8;
        --line: #334155;
        --soft: #1e293b;
        --accent: #60a5fa;
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 22px;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.6;
    }}
    main {{
      max-width: 1120px;
      margin: 0 auto;
      display: grid;
      gap: 16px;
    }}
    header, section {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
    }}
    .kicker {{
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0;
      text-transform: uppercase;
    }}
    h1 {{
      margin: 8px 0;
      font-size: clamp(24px, 4vw, 40px);
      line-height: 1.12;
    }}
    h2 {{ margin: 0 0 10px; font-size: 18px; }}
    blockquote {{
      margin: 10px 0 0;
      padding-left: 12px;
      border-left: 3px solid var(--line);
      color: var(--muted);
    }}
    .tags {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 14px; }}
    .tag {{
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 3px 9px;
      background: var(--soft);
      color: var(--muted);
      font-size: 12px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
    }}
    .card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px;
    }}
    .body-grid {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
      gap: 16px;
    }}
    @media (max-width: 760px) {{
      body {{ padding: 12px; }}
      .body-grid {{ grid-template-columns: 1fr; }}
    }}
    .related {{
      color: var(--accent);
      word-break: break-word;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 13px;
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <div class="kicker">Second Brain HTML Artifact</div>
      <h1>{html.escape(title_en)}</h1>
      <blockquote>{html.escape(title_zh)}</blockquote>
      <div class="tags">{tag_html}</div>
    </header>
    <section class="grid">
      <article class="card">
        <h2>Summary</h2>
        <p>{html.escape(summary_en)}</p>
        <blockquote>{html.escape(summary_zh)}</blockquote>
      </article>
      <article class="card">
        <h2>Related</h2>
        <p class="related">{html.escape(related_links)}</p>
        <blockquote>相关页面：{html.escape(related_links)}</blockquote>
      </article>
    </section>
    <section>
      <h2>Knowledge Body / 知识正文</h2>
      <div class="body-grid">
        <article>{html_paragraphs(body_en)}</article>
        <article><blockquote>{html_paragraphs(body_zh)}</blockquote></article>
      </div>
    </section>
  </main>
</body>
</html>
"""


def safe_page_path(slug: str) -> pathlib.Path:
    raw_slug = slug.strip().removesuffix(".md")
    clean_slug = slugify(raw_slug)
    candidate_stems = [raw_slug]
    if clean_slug != raw_slug:
        candidate_stems.append(clean_slug)
    candidates = []
    for directory in ALLOWED_PAGE_DIRS.values():
        for stem in candidate_stems:
            if "/" not in stem and "\\" not in stem and stem not in {"", ".", ".."}:
                candidates.append(directory / f"{stem}.md")
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(f"No wiki page found for slug '{clean_slug}'.")


def safe_mcp_analysis_path(slug: str) -> pathlib.Path:
    raw_slug = slug.strip().removesuffix(".md")
    clean_slug = slugify(raw_slug)
    candidate_stems = [raw_slug]
    if clean_slug != raw_slug:
        candidate_stems.append(clean_slug)
    path = None
    for stem in candidate_stems:
        if "/" in stem or "\\" in stem or stem in {"", ".", ".."}:
            continue
        candidate = ANALYSES_DIR / f"{stem}.md"
        if candidate.exists():
            path = candidate
            break
    if path is None:
        raise FileNotFoundError(f"No MCP analysis note found for slug '{slug}'.")
    text = path.read_text(encoding="utf-8")
    frontmatter = wiki_tools.parse_frontmatter(text)
    if frontmatter.get("source") != "MCP conversation capture" and "_mcp_" not in path.stem:
        raise PermissionError("Only MCP-created analysis notes can be updated.")
    return path


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


def append_log_edit(title: str, touched: list[str]) -> None:
    today = dt.date.today().isoformat()
    touched_links = ", ".join(f"[[{slug}]]" for slug in touched) if touched else "N/A"
    entry = (
        f"\n## [{today}] UPDATE | {title}\n"
        f"* **Action:** Updated an MCP-created knowledge note through the Second Brain MCP server.\n"
        f"* **Source Created:** N/A (MCP conversation capture edit)\n"
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


def trigger_git_sync() -> str:
    if os.environ.get("SECOND_BRAIN_MCP_AUTO_SYNC", "1") != "1":
        return "disabled"
    if not SYNC_SCRIPT.exists():
        return "missing_sync_script"

    env = os.environ.copy()
    env.setdefault("SECOND_BRAIN_SYNC_COMMIT_PREFIX", "mcp sync")
    with SYNC_LOG.open("ab") as log_handle:
        subprocess.Popen(
            [str(SYNC_SCRIPT)],
            cwd=ROOT,
            env=env,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    return "triggered"


def write_html_artifact(path: pathlib.Path, content: str) -> tuple[str, str]:
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    PUBLIC_HTML_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    public_path = PUBLIC_HTML_DIR / path.name
    public_path.write_text(content, encoding="utf-8")
    public_path.chmod(0o644)
    artifact_rel_path = path.relative_to(ROOT).as_posix()
    artifact_url = f"{PUBLIC_HTML_BASE_URL}/{path.name}"
    return artifact_rel_path, artifact_url


def resolve_related_links(related_slugs: list[str] | None) -> str:
    related = []
    for item in related_slugs or []:
        try:
            related.append(safe_page_path(item).stem)
        except FileNotFoundError:
            related.append(slugify(item))
    return ", ".join(f"[[{item}]]" for item in related) if related else "N/A"


def compose_knowledge_note(
    title_en: str,
    title_zh: str,
    summary_en: str,
    summary_zh: str,
    body_en: str,
    body_zh: str,
    related_links: str,
    tags: list[str],
    date_created: str,
    artifact_rel_path: str,
    artifact_url: str,
    date_updated: str | None = None,
) -> str:
    frontmatter_data = {
        "type": "analysis",
        "title": title_en,
        "aliases": [title_zh],
        "date_created": date_created,
        "source": "MCP conversation capture",
        "tags": tags,
        "summary_en": summary_en,
        "summary_zh": summary_zh,
    }
    if date_updated:
        frontmatter_data["date_updated"] = date_updated
    frontmatter = yaml.safe_dump(
        frontmatter_data,
        allow_unicode=True,
        sort_keys=False,
    ).strip()
    return f"""---
{frontmatter}
---

# {title_en}
{zh_blockquote(title_zh)}

## HTML Artifact
Open the interactive HTML artifact in Obsidian through Custom Frames.
> 通过 Custom Frames 在 Obsidian 中打开交互式 HTML artifact。

```custom-frames
frame: {CUSTOM_FRAMES_NAME}
style: height: 760px;
urlSuffix: /{pathlib.Path(artifact_rel_path).name}
```

Direct artifact URL: {artifact_url}
> 直接访问 artifact：{artifact_url}

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
    related_links = resolve_related_links(related_slugs)
    artifact_path = HTML_DIR / f"{path.stem}.html"
    artifact_rel_path, artifact_url = write_html_artifact(
        artifact_path,
        render_standalone_html_artifact(
            title_en,
            title_zh,
            summary_en,
            summary_zh,
            body_en,
            body_zh,
            related_links,
            clean_tags,
        ),
    )
    content = compose_knowledge_note(
        title_en,
        title_zh,
        summary_en,
        summary_zh,
        body_en,
        body_zh,
        related_links,
        clean_tags,
        today,
        artifact_rel_path,
        artifact_url,
    )
    path.write_text(content, encoding="utf-8")
    rebuild_index()
    append_log_update(title_en, [path.stem])
    sync_status = trigger_git_sync()
    return {
        "status": "created",
        "slug": path.stem,
        "path": path.relative_to(ROOT).as_posix(),
        "artifact_path": artifact_rel_path,
        "artifact_url": artifact_url,
        "sync": sync_status,
    }


@mcp.tool()
def update_knowledge_note(
    slug: str,
    title_en: str,
    title_zh: str,
    summary_en: str,
    summary_zh: str,
    body_en: str,
    body_zh: str,
    related_slugs: list[str] | None = None,
    tags: list[str] | None = None,
) -> dict[str, str]:
    """Replace an MCP-created analysis note with updated bilingual content.

    This is intentionally scoped to notes created by save_knowledge_note under
    wiki/analyses/. It regenerates the embedded HTML block, preserves the
    original date_created, sets date_updated, rebuilds the index, appends a log
    entry, and triggers git sync.
    """
    ensure_bilingual_pair(title_en, title_zh, "title")
    ensure_bilingual_pair(summary_en, summary_zh, "summary")
    ensure_bilingual_pair(body_en, body_zh, "body")

    path = safe_mcp_analysis_path(slug)
    existing_text = path.read_text(encoding="utf-8")
    existing_frontmatter = wiki_tools.parse_frontmatter(existing_text)
    date_created = existing_frontmatter.get("date_created") or dt.date.today().isoformat()
    today = dt.date.today().isoformat()
    clean_tags = [slugify(tag) for tag in tags or ["synthesis"]]
    related_links = resolve_related_links(related_slugs)
    artifact_path = HTML_DIR / f"{path.stem}.html"
    artifact_rel_path, artifact_url = write_html_artifact(
        artifact_path,
        render_standalone_html_artifact(
            title_en,
            title_zh,
            summary_en,
            summary_zh,
            body_en,
            body_zh,
            related_links,
            clean_tags,
        ),
    )
    content = compose_knowledge_note(
        title_en,
        title_zh,
        summary_en,
        summary_zh,
        body_en,
        body_zh,
        related_links,
        clean_tags,
        date_created,
        artifact_rel_path,
        artifact_url,
        today,
    )
    path.write_text(content, encoding="utf-8")
    rebuild_index()
    append_log_edit(title_en, [path.stem])
    sync_status = trigger_git_sync()
    return {
        "status": "updated",
        "slug": path.stem,
        "path": path.relative_to(ROOT).as_posix(),
        "artifact_path": artifact_rel_path,
        "artifact_url": artifact_url,
        "sync": sync_status,
    }


@mcp.tool()
def get_wiki_operating_rules() -> dict[str, str]:
    """Return the key write rules this MCP server follows for the wiki."""
    return {
        "raw": "Never modify raw/. Raw files are immutable source documents.",
        "bilingual": "Generated wiki content must be English first, then Simplified Chinese in a blockquote on the next line.",
        "slugs": "Use lowercase canonical slugs for filenames and wikilink targets.",
        "writes": "Conversation captures are saved under wiki/analyses/ and logged as UPDATE entries.",
        "html_artifacts": f"Each note also writes a standalone HTML artifact under wiki/html/ for the Custom Frames frame named '{CUSTOM_FRAMES_NAME}'.",
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
