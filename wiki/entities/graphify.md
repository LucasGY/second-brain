---
type: entity
title: "Graphify"
aliases: []
tags: [entity, tool, knowledge_graph]
first_seen: 2026-04-15
last_updated: 2026-04-15
key_sources: ["Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki"]
summary_en: Graphify is presented here as an AI-assistant skill that converts Markdown-based conversational data into an interactive knowledge graph and related analytical artifacts.
summary_zh: 在当前知识库里，Graphify 被呈现为一种 AI 助手 skill，用于把基于 Markdown 的对话数据转换成可交互的知识图谱及相关分析产物。
---
# Definition
[[graphify|Graphify]] is a graph-construction layer for AI-assisted workflows that reads wiki-compatible text, extracts entities and relationships with LLM support, clusters them into communities, and emits interactive graph artifacts.
[[graphify|Graphify]] 是 AI 辅助工作流中的一层图谱构建能力：它读取兼容 wiki 的文本，借助 LLM 抽取实体与关系，再完成社区聚类并输出可交互的图谱产物。

## Key Facts
- The tool is positioned as a skill usable from coding assistants such as Claude Code, Gemini CLI, and Codex.
  该工具被定位为可在 Claude Code、Gemini CLI、Codex 等编码助手中调用的 skill。
- In this wiki, its importance comes from compiling exported conversations into graph structure rather than leaving them as raw chronological transcripts.
  在本知识库里，它的重要性在于把导出的对话编译成图结构，而不是让它们继续停留在原始的时间线文本里。
- The described output includes an interactive HTML graph, a graph report, and a queryable graph JSON artifact. Source: [[20260415_manual_wechat_cli_wechat_to_llm_wiki|Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]
  文中描述的输出包括可交互 HTML 图谱、图谱报告以及可查询的 graph JSON 文件。来源：[[20260415_manual_wechat_cli_wechat_to_llm_wiki|Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]

## Recent Developments
- 2026-04-15: The current wiki state treats Graphify as the downstream compiler that turns WeChat-exported Markdown into entity graphs, community structure, and semantic retrieval surfaces for an [[llm-wiki|LLM Wiki]] workflow. Source: [[20260415_manual_wechat_cli_wechat_to_llm_wiki|Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]
  2026-04-15：当前知识库把 Graphify 视为下游编译器，用来把微信导出的 Markdown 转换成实体图谱、社区结构以及服务于 [[llm-wiki|LLM Wiki]] 工作流的语义检索层。来源：[[20260415_manual_wechat_cli_wechat_to_llm_wiki|Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]

## Source Mentions
- [[20260415_manual_wechat_cli_wechat_to_llm_wiki|Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]

## Relationships
### Related Entities
[[wechat-cli|WeChat CLI]]

### Related Concepts
[[tacit-knowledge-compilation|Tacit Knowledge Compilation]], [[llm-wiki|LLM Wiki]]
