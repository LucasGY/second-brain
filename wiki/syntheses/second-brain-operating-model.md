---
title: Second Brain Operating Model
type: synthesis
status: active
created: 2026-04-06
updated: 2026-04-06
source_count: 1
source_files:
  - raw/inbox/2026-04-04-karpathy-llm-wiki-links.md
wiki_links:
  - LLM Wiki Pattern
  - Karpathy - LLM Wiki Pattern
---

# Second Brain Operating Model

## Summary

This repository implements the LLM Wiki pattern as a local markdown workflow:
`raw/` holds immutable inputs, `wiki/` holds maintained knowledge pages, and
`AGENTS.md` defines the maintenance behavior.

## Operating Loop

- Add source files to `raw/inbox/`.
- Ingest each source into a page under `wiki/sources/`.
- Update related concept, entity, analysis, and synthesis pages.
- Rebuild `wiki/index.md`.
- Append a record to `wiki/log.md`.
- Run lint periodically and repair the detected gaps.

## Why This Matters

- Durable synthesis becomes browseable outside the chat transcript.
- Repeated questions become cheaper because the wiki is already organized.
- The maintenance process is explicit and inspectable in git.

## Connections

- [[LLM Wiki Pattern]]: upstream conceptual model.
- [[Karpathy - LLM Wiki Pattern]]: primary seed source for this repo.
