---
type: concept
title: "LLM Wiki"
aliases: ["persistent wiki", "Karpathy LLM Wiki"]
tags: [concept, knowledge_management, llm]
status: seed
first_seen: 2026-04-15
last_updated: 2026-04-15
summary_en: LLM Wiki is a pattern in which an LLM compiles raw material into a maintained, interlinked markdown knowledge base rather than re-deriving answers from source chunks on every query.
summary_zh: LLM Wiki 是一种模式：让 LLM 把原始材料编译成持续维护、相互链接的 Markdown 知识库，而不是在每次提问时都从原始片段重新推导答案。
---
# Core Definition
[[LLM Wiki]] is a persistent knowledge-compilation pattern in which an LLM maintains structured notes between the user and raw sources, so that useful understanding becomes durable wiki state instead of ephemeral chat output.
[[LLM Wiki]] 是一种持久化的知识编译模式：由 LLM 在用户与原始资料之间维护结构化笔记，使得有用的理解沉淀为持久的 wiki 状态，而不是转瞬即逝的聊天输出。

## 🛠️ Mechanisms & Architecture
- The pattern inserts an intermediate knowledge layer between raw documents and question answering, so later queries operate on curated pages instead of repeatedly scanning unstructured source text.
  这种模式在原始文档与问答之间插入了一层中间知识层，使后续查询优先作用于整理过的页面，而不是反复扫描无结构原文。
- In the current wiki state, this article expands the pattern from code and documents into private messaging archives by first exporting chat history to Markdown and then compiling it into graph-linked artifacts through [[Graphify]]. Source: [[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]
  在当前知识库状态下，这篇文章把该模式从代码与文档扩展到了私有消息档案：先把聊天记录导出为 Markdown，再通过 [[Graphify]] 编译成带图结构的知识产物。来源：[[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]
- Markdown acts as the interoperability layer because it preserves enough structure for both human review and LLM-driven downstream compilation.
  Markdown 在这里充当互操作层，因为它既保留了足够结构，便于人工检查，也便于 LLM 驱动的下游编译。

## ⚔️ Contradictions & Evolution
- A basic tension inside [[LLM Wiki]] is whether the system should stay narrowly document-centric or expand to conversational and tacit sources that are richer but more private and noisier.
  [[LLM Wiki]] 的一个基本张力在于：系统应当停留在文档中心的范围内，还是扩展到更丰富、但也更私密且更嘈杂的对话型与暗知识来源。
- This source pushes the concept toward broader ingestion by arguing that undocumented discussion often contains the highest-value operational knowledge, but it also introduces stronger privacy, compliance, and trust-boundary concerns.
  这个来源推动该概念朝更广泛摄取的方向发展，因为它认为未文档化的讨论往往包含最高价值的操作性知识；但与此同时，它也引入了更强的隐私、合规与信任边界问题。

## 🚀 Implementations & Best Practices
- Use a durable export format such as Markdown as the handoff point between extraction and compilation.
  应使用 Markdown 这类持久导出格式，作为“数据提取”和“知识编译”之间的交接点。
- Prefer local-first extraction for sensitive sources, and make the cloud boundary explicit before sending any private material to external LLM services.
  对敏感来源应优先采用本地优先提取，并在把私密材料发送给外部 LLM 服务之前，显式划清云端边界。
- Treat chat-derived wiki content as higher-noise but high-value material that may need stronger review before becoming durable knowledge. Source: [[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]
  应把聊天衍生的 wiki 内容视为“噪声更高但价值也更高”的材料，在沉淀为持久知识前往往需要更强的审核。来源：[[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]

## 📚 Source Mentions
- [[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]

## 🕸️ Relationships

### Related Concepts
[[Tacit Knowledge Compilation]]

### Related Entities
[[WeChat CLI]], [[Graphify]]
