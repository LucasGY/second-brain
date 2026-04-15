---
type: concept
title: "Tacit Knowledge Compilation"
aliases: ["dark knowledge compilation"]
tags: [concept, workflow, knowledge_management]
status: seed
first_seen: 2026-04-15
last_updated: 2026-04-15
summary_en: Tacit Knowledge Compilation is the process of turning undocumented conversational knowledge into structured, reusable artifacts that can participate in search, synthesis, and long-term organizational memory.
summary_zh: Tacit Knowledge Compilation 指的是把未文档化的对话型知识转化为结构化、可复用产物的过程，使其能够参与搜索、综合分析和长期组织记忆。
---
# Core Definition
[[Tacit Knowledge Compilation]] is a workflow for extracting valuable but undocumented operational knowledge from conversations, then converting it into structured formats that can be indexed, synthesized, and maintained over time.
[[Tacit Knowledge Compilation]] 是一种工作流：从对话中提取有价值却未被文档化的操作性知识，再把它转成可索引、可综合、可长期维护的结构化格式。

## 🛠️ Mechanisms & Architecture
- The source workflow begins with locked conversational storage, converts it into structured export formats, and then applies LLM-assisted extraction to identify entities, relationships, and recurring themes.
  该来源中的流程，从被锁定的对话存储开始，先把它转换为结构化导出格式，再用 LLM 辅助抽取实体、关系与重复出现的主题。
- In the current wiki state, [[WeChat CLI]] serves as the extraction bridge and [[Graphify]] serves as the compilation layer that turns transcripts into graph-linked knowledge artifacts. Source: [[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]
  在当前知识库状态下，[[WeChat CLI]] 充当提取桥梁，[[Graphify]] 则充当编译层，把对话文本转成图谱化的知识产物。来源：[[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]
- The end state is not just full-text search; it is semantic retrieval over a normalized memory surface.
  最终目标不只是全文搜索，而是在一个被归一化的记忆表面上实现语义检索。

## ⚔️ Contradictions & Evolution
- Tacit knowledge is often more decision-relevant than official documentation, but it is also noisier, more ambiguous, and more socially sensitive.
  暗知识往往比正式文档更贴近真实决策，但它也更嘈杂、更模糊，并且在社交层面更敏感。
- This creates a permanent tradeoff between knowledge capture and privacy protection: the more conversational detail a system preserves, the more carefully it must manage consent, legal boundaries, and model exposure.
  这会形成一种长期权衡：系统保留的对话细节越多，就越需要谨慎处理同意机制、法律边界以及模型暴露风险。

## 🚀 Implementations & Best Practices
- Start with personal or small-team retrospectives before scaling to broader chat archives.
  应先从个人或小团队复盘开始，再逐步扩大到更广泛的聊天档案。
- Preserve timestamps, speakers, and message types during export because these metadata fields are often necessary for later synthesis.
  导出时应保留时间戳、发言人和消息类型，因为这些元数据通常是后续综合分析所必需的。
- Pair ingestion with explicit privacy review, especially when any downstream stage depends on a hosted LLM service. Source: [[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]
  摄取流程应配套明确的隐私审查，尤其是在下游阶段依赖托管式 LLM 服务时。来源：[[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]

## 📚 Source Mentions
- [[Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki]]

## 🕸️ Relationships

### Related Concepts
[[LLM Wiki]]

### Related Entities
[[WeChat CLI]], [[Graphify]]
