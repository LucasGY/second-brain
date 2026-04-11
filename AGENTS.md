# AGENTS.md

This repository is a markdown-first second brain. The LLM maintains the wiki;
humans curate sources, steer analysis, and ask questions.

## Mission

Transform raw source material into a persistent, interlinked knowledge base that
compounds over time instead of re-deriving the same synthesis on every query.

## Architecture

There are three layers:

1. `raw/`
   - Immutable source documents.
   - The LLM may read these files but must not rewrite them.
   - New source files usually start in `raw/inbox/`.
2. `wiki/`
   - Markdown knowledge base owned by the LLM.
   - This is where summaries, concepts, entities, analyses, and syntheses live.
3. `AGENTS.md`
   - The operating schema.
   - Defines structure, naming, workflows, and quality rules.

## Folder conventions

- `wiki/overview.md`
  - Big-picture orientation to the domain.
- `wiki/index.md`
  - Navigation catalog of all wiki pages.
- `wiki/log.md`
  - Append-only chronological history of ingest, query, and lint operations.
- `wiki/sources/`
  - One page per ingested source.
- `wiki/entities/`
  - Named people, orgs, products, projects, places, or systems.
- `wiki/concepts/`
  - Themes, abstractions, mechanisms, frameworks, and recurring ideas.
- `wiki/analyses/`
  - Focused question-driven writeups and comparisons.
- `wiki/syntheses/`
  - Higher-level views that integrate multiple sources or analyses.

## Page format

Use YAML frontmatter on wiki pages when possible:

```yaml
---
title: Example Page
title_zh: 示例页面
type: concept
status: active
created: 2026-04-06
updated: 2026-04-06
source_count: 2
summary_en: One short paragraph that explains the page.
summary_zh: 一段简短中文摘要，和英文内容对应。
source_files:
  - raw/inbox/example-source.md
wiki_links:
  - Another Page
---
```

Then use this body structure when it fits:

```md
# Example Page

## Summary
One short paragraph that explains the page.
一段简短中文摘要，和英文内容对应。

## Key Points
- ...
- ...

## Evidence
- [Source Name](../sources/source-name.md): what it supports
- [Source Name](../sources/source-name.md): 这条证据支持什么

## Connections
- [[Related Page]]: why it matters
- [[Related Page]]: 这个连接为什么重要

## Open Questions
- ...
- ...
```

For dynamic synthesis pages, prefer a more operational structure:

```md
# Dynamic Topic

## Summary
One short paragraph.
一段简短摘要。

## Situation Assessment
- Main directional judgment.
- Main directional judgment in Chinese.

## Situation Summary
### Platform / Company / Theme A
- What matters now.
- 现在重要的点。

## Active Threads
### Thread Name
Short framing paragraph.
简短说明。

- Signals:
  - recent signal
  - 最近信号
- Watch:
  - what would change the assessment
  - 哪个变化会改变当前判断
- Likelihood / Impact / Next milestone:
  - medium / high / specific next checkpoint
  - 中 / 高 / 下一个具体检查点

## Top Events
- highest-signal developments worth preserving
- 最值得保留的高信号动态

## Connections
- ...
- ...
```

The goal is not to copy a news dashboard, but to compress noisy updates into
durable threads, signals, decision points, and next checkpoints.

## Bilingual policy

- Wiki display content should be bilingual by default.
- Keep English first and Chinese immediately below it in the same section.
- Do not add explicit language markers such as `English`, `中文`, `EN`, or
  `CN` inside normal page content unless they are actually necessary for
  disambiguation.
- Prefer clean visual stacking: one English paragraph or list, then the
  corresponding Chinese paragraph or list directly beneath it.
- Preserve one canonical page title for filenames, frontmatter `title`, `#`
  headings, and wikilinks. English is the default canonical title unless there
  is a strong reason to do otherwise.
- Add `title_zh` when a stable Chinese title exists.
- Add `summary_en` and `summary_zh` in frontmatter whenever practical so
  generated indexes can stay bilingual.
- English and Chinese should be semantically aligned. Translate the meaning,
  not necessarily the sentence shape.
- When updating an existing page, keep both languages in sync instead of only
  editing one half.

## Wiki link rules

- Prefer Obsidian-style wikilinks: `[[Page Name]]`.
- Match the target page title exactly when practical.
- Add links in both directions when a connection is important.
- Prefer updating an existing page over creating a near-duplicate.

## Naming rules

- Use concise, readable filenames with kebab-case.
- Put the canonical human-readable title in frontmatter and the `#` heading.
- Source notes should usually be named `YYYY-MM-DD-short-title.md`.
- Analysis pages should be task-oriented, not generic.

## Allowed operations

## Coverage rule

- Raw markdown in `raw/inbox/` is backlog, not knowledge completion.
- Important raw markdown should be absorbed into the wiki through source notes,
  syntheses, concepts, entities, or analyses.
- High-volume feeds such as `raw/inbox/x.com/` should usually be normalized as
  grouped source notes or thematic summaries, not left as raw captures only.
- If a raw feed repeatedly mentions named companies, products, people, or
  organizations, those patterns should eventually surface under
  `wiki/entities/` when the references become durable.

## Structured synthesis rules

- For fast-moving topics, separate stable assessment from raw event flow.
- Prefer a small number of active threads over long unordered bullet dumps.
- Each thread should answer:
  - what is happening,
  - what signals support it,
  - what to watch next,
  - what event would change the judgment.
- Use evidence strength implicitly through wording such as strong, moderate,
  tentative rather than bluffing certainty.
- Keep top-event sections selective. They should be the highest-signal items,
  not a full activity log.
- When possible, group summaries by actor, company, platform, or market role so
  the reader can quickly scan who sees the situation how.
- Prefer explicit next milestones and decision points over vague "monitor this"
  wording.
- If a page becomes too event-heavy, split durable background into entity or
  concept pages and keep the synthesis page focused on situation tracking.

### Ingest

When given a new raw source:

1. Read the source from `raw/inbox/` or `raw/processed/`.
2. Create or update a bilingual source note in `wiki/sources/`.
3. Update any impacted concept, entity, analysis, synthesis, or overview pages.
4. Add missing wiki links and surface contradictions.
5. If the source is part of a high-volume feed, prefer grouping it into a
   durable source note instead of creating one wiki page per fragment.
6. Rebuild `wiki/index.md`.
7. Append a log entry to `wiki/log.md`.

### Query

When answering a question:

1. Read `wiki/index.md` first.
2. Open only the relevant wiki pages.
3. Synthesize an answer grounded in the wiki.
4. If the answer creates durable knowledge, save it as bilingual content under
   `wiki/analyses/` or `wiki/syntheses/`.
5. Rebuild the index if new pages were added.
6. Append a `query` log entry when the result is saved into the wiki.

### Lint

Periodically check for:

- Broken wikilinks.
- Orphan pages with no inbound links.
- Raw sources that have no source note.
- Duplicate or overlapping pages.
- Stale claims that newer pages or sources may supersede.
- Important concepts that appear repeatedly but lack their own page.

Use `python3 scripts/wiki_tools.py lint` as a first pass, then inspect issues
manually and fix them in the wiki.

## Quality bar

- Preserve uncertainty instead of bluffing.
- Distinguish facts, interpretations, and open questions.
- Note contradictions explicitly.
- Keep summaries compact and cumulative.
- Keep English and Chinese sections meaningfully aligned.
- Prefer natural Chinese over literal word-for-word translation.
- Prefer readable bilingual layout over visibly labeled translation blocks.
- Prefer many small edits across the wiki over siloed one-off notes.
- Every meaningful ingest should update more than one place when warranted.

## Tooling

Useful commands:

```bash
python3 scripts/wiki_tools.py rebuild-index
python3 scripts/wiki_tools.py lint
python3 scripts/wiki_tools.py search "query terms"
python3 scripts/wiki_tools.py log ingest "Title" --details "What changed"
```

## Human / LLM split

- Human responsibilities:
  - Curate sources.
  - Direct focus.
  - Ask questions.
  - Review important edits.
- LLM responsibilities:
  - Summarize.
  - Cross-reference.
  - Maintain structure.
  - Update multiple affected pages.
  - Keep the wiki coherent over time.
