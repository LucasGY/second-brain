# ENTITY_STANDARDS.md

## Purpose
An entity page is the canonical long-term page for one concrete thing:
a person, company, tool, model, organization, product, project, paper, or dataset.

It explains:
- what the entity is
- why it matters in this wiki
- what meaningful changes and durable significance should be preserved

## Required Sections
Every entity page MUST contain these sections in this order:

1. YAML frontmatter
2. Definition
3. Evolution Timeline
4. Strategic / Technical Significance
5. Source Mentions
6. Relationships

## Writing Rules
- Focus on one concrete thing.
- Preserve durable, reusable knowledge.
- Prefer stable facts over transient chatter.
- Use Obsidian wikilinks for related pages.
- When a page filename is a normalized slug (for example `wechat-cli.md`) but the display name contains spaces, case changes, or punctuation (for example `WeChat CLI`), always write links in canonical form: `[[wechat-cli|WeChat CLI]]`.

## Update Rules
- Add a timeline entry only if a source materially changes or enriches understanding of the entity.
- Put routine `raw/feeds/` updates in `Evolution Timeline`, newest first.
- Put `Evolution Timeline` immediately below `Definition` so recent changes are visible before deeper synthesis.
- Update `Definition` or `Strategic / Technical Significance` only when stable understanding changes, especially from `raw/manual/` sources or major `raw/feeds/` updates.
- Every timeline entry MUST be bilingual: English first, then Simplified Chinese on the next line.
- Every timeline entry MUST cite at least one source page with a canonical wikilink.
- Low-signal feed mentions should usually be omitted from `Evolution Timeline`; add them to `Source Mentions` only if they are worth retaining as evidence.

## Anti-Patterns
Do not:
- copy-paste source summaries
- append every minor mention
- turn the page into a changelog with no stable structure
- explain broad abstract theories unless directly relevant
- maintain generic encyclopedia facts that do not help this wiki's research memory
- rewrite durable significance because of a routine feed item

## Bilingual Format

English first, Chinese in `>` blockquote immediately below. See CLAUDE.md Section 3 for the rule. Timeline entry pattern:

```markdown
* **[YYYY-MM-DD]:** [English]. Source: [[source-slug|Title]]
  > **[YYYY-MM-DD]：** [中文]。来源：[[source-slug|标题]]
```

## Example Template

```markdown
---
type: entity
title: "[Entity Exact Name]"
aliases: [] # List alternative names or acronyms here, e.g., ["Obsidian.md"]
tags: [entity] # Add 2-3 specific tags, e.g., #tool, #company
first_seen: YYYY-MM-DD
last_updated: YYYY-MM-DD
key_sources: []
---

# Definition
[[Obsidian]] is a local-first markdown knowledge management tool used here as the primary interface for browsing and editing the wiki.
> [[obsidian|Obsidian]] 是一款本地优先的 Markdown 知识管理工具，用作本 wiki 的主要浏览和编辑界面。

## 📅 Evolution Timeline
[Append-only log. Newest entries at top. When ingesting news, launches, release notes, version changes, or market/news developments from `raw/feeds/`, append the new information to the TOP of this list. Never delete old timeline entries unless explicitly re-ingesting with human approval.]
* **[YYYY-MM-DD]:** [Brief English description of the update]. Source: [[source-page-slug|Readable Source Title]]
  > **[YYYY-MM-DD]：** [对应的简体中文更新描述]。来源：[[source-page-slug|可读来源标题]]
* **[YYYY-MM-DD]:** [Brief English description of the update]. Source: [[source-page-slug|Readable Source Title]]
  > **[YYYY-MM-DD]：** [对应的简体中文更新描述]。来源：[[source-page-slug|可读来源标题]]

## Strategic / Technical Significance
- [Brief English synthesis of why this entity matters to the wiki's research questions, technical architecture, market thesis, or workflow.]
  > [对应的简体中文综合说明：这个实体为什么对本 wiki 的研究问题、技术架构、市场判断或工作流重要。]

## 📚 Source Mentions
[A bulleted list of all source pages in `wiki/sources/` that heavily discuss or analyze this entity. Every time you touch this entity from an ingest, add the source link here.]
* [[20260410_manual_deepseek_moe_architecture|DeepSeek MoE Architecture]]
* [[20251215_feeds_ai_coding_assistants_review|AI Coding Assistants Review]]

## 🕸️ Relationships

### Related Entities
[[Entity1]], [[Entity2]]

### Related Concepts
[[Concept1]], [[Concept2]]
```
