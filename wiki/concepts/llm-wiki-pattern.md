---
title: LLM Wiki Pattern
title_zh: LLM Wiki 模式
type: concept
status: active
created: 2026-04-06
updated: 2026-04-11
source_count: 1
summary_en: The LLM Wiki pattern treats the knowledge base as a persistent compiled artifact that is updated incrementally.
summary_zh: LLM Wiki 模式把知识库视为一种持久化的编译产物，随着新信息到来做增量更新。
source_files:
  - raw/inbox/2026-04-04-karpathy-llm-wiki-links.md
wiki_links:
  - Karpathy - LLM Wiki Pattern
  - Second Brain Operating Model
---

# LLM Wiki Pattern

_LLM Wiki 模式_


## Summary
The LLM Wiki pattern treats the knowledge base as a persistent compiled artifact:
raw material is ingested once, synthesized into markdown pages, and then updated
incrementally as new information arrives.

LLM Wiki 模式把知识库视为一种持久化的“编译产物”：原始材料被摄入一次，整理成
Markdown 页面，并在新信息出现时持续做增量更新。

## Source Files

- [2026-04-04-karpathy-llm-wiki-links.md](<../../raw/inbox/2026-04-04-karpathy-llm-wiki-links.md>)

## Key Points
- It is an alternative to pure query-time RAG.
- The wiki compounds because knowledge is stored in reusable, linked pages.
- Cross-references and contradictions are maintained ahead of time.
- The maintenance burden shifts from the human to the LLM.
- Query outputs can themselves become new wiki assets.

- 它可以替代纯 query-time 的 RAG 方式。
- 知识被存进可复用、可链接的页面里，因此 wiki 会持续复利增长。
- 交叉引用和矛盾关系会被提前维护，而不是等提问时才临时拼接。
- 维护负担从人转移到 LLM。
- 查询结果本身也可以沉淀成新的 wiki 资产。

## Evidence
- [Karpathy - LLM Wiki Pattern](../sources/2026-04-04-llm-wiki.md): source note
  for the pattern description.

- [Karpathy - LLM Wiki Pattern](../sources/2026-04-04-llm-wiki.md)：该模式说明的
  来源页。

## Connections
- [[Second Brain Operating Model]]: local implementation in this repository.

- [[Second Brain Operating Model]]：该模式在本仓库中的本地化实现。

## Open Questions
- How much structure should be enforced in frontmatter versus allowed to emerge?
- When should a concept split into several narrower pages?

- frontmatter 应该强制多少结构，多少内容可以在实践中自然长出来？
- 一个概念应当在什么时点拆分成更窄的多个页面？
