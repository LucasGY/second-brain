# Analysis Page Standards (`wiki/analyses/`)

**Target Directory:** `wiki/analyses/`
**Purpose:** Analysis pages are cross-source synthesis documents, decision maps, dashboards, interactive-artifact wrappers, and durable research outputs. They are not raw source summaries; they compile multiple signals into a reusable analytical object.

---

## 1. When to Create an Analysis Page

Create an analysis page when the output is any of the following:
- a strategic map, investment memo, comparative analysis, or cross-source synthesis
- an HTML artifact wrapper or dashboard-ready artifact note
- a decision tree, timeline, flowchart, framework, or durable research deliverable
- a user-requested synthesis that should remain queryable in the wiki

Do not use `wiki/analyses/` for raw document ingestion; source summaries belong in `wiki/sources/`.

---

## 2. File Naming Convention

- **Format:** `YYYYMMDD_[source_type]_[short_title].md`
- **Source types:** Use `manual`, `feeds`, `mcp`, or another stable source class when appropriate.
- The filename stem is the canonical `slug` and MUST be used as the wikilink target.
- Example: `20260616_manual_amazon-2025-shareholder-letter-strategic-map.md`

---

## 3. Required YAML Frontmatter

Every analysis page MUST use this canonical field set so dashboard loaders do not need to infer titles or artifacts.

```yaml
---
type: analysis
slug: "YYYYMMDD_source-type_short-title"
title: "Human-readable English title kept for backward compatibility"
title_en: "Human-readable English title"
title_zh: "面向中文读者的人类可读标题"
aliases: []
date_created: YYYY-MM-DD
last_updated: YYYY-MM-DD
source: "raw/... or MCP conversation capture"
tags: []
summary_en: "One-sentence English summary."
summary_zh: "一句话中文摘要。"
artifact_html: "matching-artifact-file.html"
---
```

### Field Rules

| Field | Required | Rule |
|---|---:|---|
| `type` | Yes | Always `analysis`. |
| `slug` | Yes | Must exactly match the Markdown filename stem. |
| `title` | Yes | English title retained for older loaders and Obsidian display. Prefer same value as `title_en`. |
| `title_en` | Yes | Canonical English title for bilingual frontend/dashboard display. |
| `title_zh` | Yes | Canonical Simplified Chinese title for bilingual frontend/dashboard display. |
| `aliases` | Yes | Include alternate names, prior titles, and useful Chinese/English variants. |
| `date_created` | Yes | Creation date in `YYYY-MM-DD`. |
| `last_updated` | Yes | Last material update date in `YYYY-MM-DD`. |
| `source` | Yes | Raw path, source page, MCP capture label, or synthesis basis. |
| `tags` | Yes | Use existing wiki tags where possible; include `html-artifact` when an HTML artifact exists. |
| `summary_en` | Yes | One concise sentence describing the analysis. |
| `summary_zh` | Yes | Simplified Chinese translation of `summary_en`. |
| `artifact_html` | Conditional | Required when the analysis has a standalone HTML artifact. Store only the filename, e.g. `20260616_manual_amazon-2025-shareholder-letter-strategic-map.html`, not a URL. |

### Artifact Field Rules

- If the page embeds or references an HTML artifact, `artifact_html` MUST be present.
- `artifact_html` MUST point to the file in `wiki/html/` by filename only.
- Do not force dashboard loaders to infer artifact filenames from note slugs, iframe URLs, or Custom Frames blocks.
- If future artifact types are added, use explicit fields such as `artifact_pdf`, `artifact_png`, or `artifact_data`, following the same filename-only rule.

---

## 4. Required Body Structure

Analysis pages SHOULD use these sections in this order, adapting names only when the analysis type clearly needs a better label:

````markdown
# English Title
> 中文标题

## HTML Artifact
English paragraph explaining what the artifact preserves or renders.
> 对应中文说明。

<iframe src="https://www.lucasgou.cloud/second-brain-html/[artifact_html]" ...></iframe>

```custom-frames
frame: Second Brain HTML
style: height: 860px;
urlSuffix: /[artifact_html]
```

Direct artifact URL: https://www.lucasgou.cloud/second-brain-html/[artifact_html]
> 直接访问 artifact：https://www.lucasgou.cloud/second-brain-html/[artifact_html]

## Summary
English synthesis paragraph.
> 中文综合段落。

## Source Context
English source/basis paragraph.
> 中文来源说明。

## Related
[[canonical-slug|Readable English]], [[canonical-slug|中文显示名]]
> 相关页面：[[canonical-slug|中文显示名]]
````

If there is no HTML artifact, omit the `HTML Artifact` section and use analysis-specific sections such as `Thesis`, `Evidence`, `Implications`, `Risks`, and `Open Questions`.

---

## 5. Bilingual Writing Rules

- Every heading body, paragraph, bullet, and table explanation must be English first, followed immediately by Simplified Chinese in a `>` blockquote on the next line.
- Keep wikilink targets in canonical English slugs; translate display text with piped wikilinks when useful.
- Prefer concise synthesis over copying source text.

---

## 6. Dashboard Loader Contract

Dashboard and frontend loaders may rely on these invariants:
- `title_en` and `title_zh` are always present on analysis pages.
- HTML-backed analysis pages always declare `artifact_html` explicitly.
- `artifact_html` is a filename under `wiki/html/`, not a full URL.
- `slug` matches the Markdown filename stem.
- `summary_en` and `summary_zh` are safe to display as short card descriptions.
