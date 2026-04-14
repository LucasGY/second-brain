# ENTITY_STANDARDS.md

## Purpose
An entity page is the canonical long-term page for one concrete thing:
a person, company, tool, model, organization, product, project, paper, or dataset.

It explains:
- what the entity is
- why it matters in this wiki
- what durable facts and meaningful changes should be preserved

## Required Sections
Every entity page MUST contain these sections in this order:

1. YAML frontmatter
2. Definition
3. Key Facts
5. Recent Developments
7. Source Mentions
4. Relationships

## Writing Rules
- Focus on one concrete thing.
- Preserve durable, reusable knowledge.
- Prefer stable facts over transient chatter.
- Use Obsidian wikilinks for related pages.

## Update Rules
- Add a recent development only if a source materially changes or enriches understanding of the entity.
- Put routine source-driven updates in `Recent Developments`.
- Update `Definition` or `Key Facts` only when stable understanding changes.
- Every development note MUST cite at least one source page with a wikilink.

## Anti-Patterns
Do not:
- copy-paste source summaries
- append every minor mention
- turn the page into a changelog with no stable structure
- explain broad abstract theories unless directly relevant

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

## Key Facts
- Local-first markdown note system.
- Supports wikilinks and graph-based navigation.
- Works well as a frontend for a persistent compiled wiki.
- Useful as a human-readable editing interface for LLM-maintained notes.

## 📅 Evolution Timeline
[This is an APPEND-ONLY log. When ingesting news or version updates from `raw/feeds/`, append the new information to the TOP of this list. NEVER delete old timeline entries.]
* **[YYYY-MM-DD]:** [Brief description of the update]. Source: [[Source_Page_Link]]
* **[YYYY-MM-DD]:** [Brief description of the update]. Source: [[Source_Page_Link]]


## 📚 Source Mentions
[A bulleted list of all source pages in `wiki/sources/` that heavily discuss or analyze this entity. Every time you touch this entity from an ingest, add the source link here.]
* [[20260410_inbox_DeepSeek_MoE_Architecture]]
* [[20251215_wx_AI_Coding_Assistants_Review]]

## 🕸️ Relationships

### Related Entities
[[Entity1]], [[Entity2]]

### Related Concepts
[[Concept1]], [[Concept2]]
```