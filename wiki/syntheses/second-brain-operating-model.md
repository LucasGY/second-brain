---
title: Second Brain Operating Model
title_zh: 第二大脑操作模型
type: synthesis
status: active
created: 2026-04-06
updated: 2026-04-11
source_count: 1
summary_en: This repository implements the LLM Wiki pattern as a local markdown workflow anchored by raw sources, wiki pages, and AGENTS.md.
summary_zh: 这个仓库把 LLM Wiki 模式实现成一个本地 Markdown 工作流，核心由 raw 来源、wiki 页面和 AGENTS.md 组成。
source_files:
  - raw/inbox/2026-04-04-karpathy-llm-wiki-links.md
wiki_links:
  - LLM Wiki Pattern
  - Karpathy - LLM Wiki Pattern
---

# Second Brain Operating Model

_第二大脑操作模型_


## Summary
This repository implements the LLM Wiki pattern as a local markdown workflow:
`raw/` holds immutable inputs, `wiki/` holds maintained knowledge pages, and
`AGENTS.md` defines the maintenance behavior.

这个仓库把 LLM Wiki 模式实现成一个本地 Markdown 工作流：`raw/` 存放不可变输入，
`wiki/` 存放持续维护的知识页面，而 `AGENTS.md` 定义维护行为。

## Operating Loop
- Add source files to `raw/inbox/`.
- Ingest each source into a page under `wiki/sources/`.
- Update related concept, entity, analysis, and synthesis pages.
- Rebuild `wiki/index.md`.
- Append a record to `wiki/log.md`.
- Run lint periodically and repair the detected gaps.

- 把来源文件放进 `raw/inbox/`。
- 将每个来源摄入为 `wiki/sources/` 下的页面。
- 更新相关概念页、实体页、分析页和综合页。
- 重新生成 `wiki/index.md`。
- 在 `wiki/log.md` 里追加记录。
- 定期运行 lint 并修复发现的问题。

## Why This Matters
- Durable synthesis becomes browseable outside the chat transcript.
- Repeated questions become cheaper because the wiki is already organized.
- The maintenance process is explicit and inspectable in git.

- 持久化综合内容可以脱离聊天记录被浏览和复用。
- 重复提问的成本会降低，因为 wiki 已经被预先组织好。
- 整个维护过程在 git 中是显式且可审查的。

## Connections
- [[LLM Wiki Pattern]]: upstream conceptual model.
- [[Karpathy - LLM Wiki Pattern]]: primary seed source for this repo.

- [[LLM Wiki Pattern]]：上游概念模型。
- [[Karpathy - LLM Wiki Pattern]]：本仓库的首个种子来源。
