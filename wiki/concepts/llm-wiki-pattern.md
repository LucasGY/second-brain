---
title: LLM Wiki Pattern
type: concept
status: active
created: 2026-04-06
updated: 2026-04-06
source_count: 1
source_files:
  - raw/inbox/2026-04-04-karpathy-llm-wiki-links.md
wiki_links:
  - Karpathy - LLM Wiki Pattern
  - Second Brain Operating Model
---

# LLM Wiki Pattern

## Summary

The LLM Wiki pattern treats the knowledge base as a persistent compiled artifact:
raw material is ingested once, synthesized into markdown pages, and then updated
incrementally as new information arrives.

## Key Points

- It is an alternative to pure query-time RAG.
- The wiki compounds because knowledge is stored in reusable, linked pages.
- Cross-references and contradictions are maintained ahead of time.
- The maintenance burden shifts from the human to the LLM.
- Query outputs can themselves become new wiki assets.

## Evidence

- [Karpathy - LLM Wiki Pattern](../sources/2026-04-04-llm-wiki.md): source note
  for the pattern description.

## Connections

- [[Second Brain Operating Model]]: local implementation in this repository.

## Open Questions

- How much structure should be enforced in frontmatter versus allowed to emerge?
- When should a concept split into several narrower pages?
