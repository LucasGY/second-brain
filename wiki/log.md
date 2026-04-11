# Wiki Log

Append-only operational history for ingest, query, and lint work.

## [2026-04-06] bootstrap | Initialized second-brain scaffold

- Added the raw/wiki/scripts architecture.
- Added `AGENTS.md` with ingest/query/lint rules.
- Added wiki maintenance tooling and starter pages.

## [2026-04-06] ingest | Karpathy LLM Wiki pattern

- Captured the X post and gist as a local raw source note.
- Added a source note, a concept page, and a synthesis page.
- Anchored the repository's operating model to the persistent-wiki pattern.

## [2026-04-07] ingest | Xiaoyuzhou transcript on OpenClaw and AI work

- Ingested the podcast transcript into a durable source note.
- Added concept pages for `Programming Eats Knowledge Work` and `AI-Native Microteams`.
- Added an analysis page connecting agent workflows to career strategy.

## [2026-04-10] ingest | OpenAI harness engineering and automated research

- Ingested two new Xiaoyuzhou transcripts covering OpenAI's no-human-code workflow and Jakub Pachocki's automated researcher roadmap.
- Added concept pages for `Harness Engineering` and `Automated Researchers`.
- Added an analysis page connecting coding automation to research automation.
- Updated existing concept and overview pages to reflect the broader autonomy arc and current inbox backlog.

## [2026-04-10] structure | Modular AI entrypoints

- Added synthesis hubs for `AI News`, `AI Technologies`, and `AI Equities`.
- Updated the overview to encourage routing future ingest through topic modules first.
- Established a cleaner split between news flow, technical abstractions, and public-market/company tracking.

## [2026-04-11] note | Bilingual wiki rollout

- Updated AGENTS.md to require bilingual pages with English first and Chinese below. Updated scripts/wiki_tools.py so index and search consume summary_en/summary_zh. Converted existing wiki pages to bilingual display format and rebuilt wiki/index.md. Ran lint: no broken wikilinks and no orphan pages; remaining lint items are uncatalogued raw sources in raw/inbox/.

## [2026-04-11] ingest | X feed normalization into sources and entities

- Grouped two high-volume `raw/inbox/x.com/` feeds into durable bilingual source notes instead of leaving them as raw captures only.
- Added first entity pages for `OpenAI`, `Google`, `Anthropic`, `TSMC`, and `NVIDIA`.
- Updated AI news, technologies, equities, and overview pages so X-derived material now participates in the wiki graph.

## [2026-04-11] ingest | Thread-based synthesis structure

- Updated AGENTS.md with operational synthesis rules inspired by https://skill.capduck.com and rewrote wiki/syntheses/ai-news.md around situation assessment, active threads, signals, watchpoints, and next milestones.
