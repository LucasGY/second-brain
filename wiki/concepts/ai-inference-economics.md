---
type: concept
title: "AI Inference Economics"
aliases: ["Inference Unit Economics", "Token Economics", "AI Token Economics"]
tags: [concept, finance, ai_tech]
status: seed
first_seen: 2026-05-06
last_updated: 2026-05-06
---

# Core Definition
AI inference economics describes the relationship between token demand, token pricing, compute cost per token, infrastructure utilization, and gross margin for model providers, cloud platforms, and downstream software vendors.
> AI 推理经济学描述 token 需求、token 定价、每 token 算力成本、基础设施利用率和毛利率之间的关系，适用于模型提供商、云平台和下游软件厂商。

## 🛠️ Mechanisms & Architecture
* **Price-cost spread:** If token prices stabilize while compute cost per token falls, incremental inference usage can become margin-accretive. Source: [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]
  > **价差机制：** 如果 token 价格企稳而每 token 算力成本下降，新增推理使用就可能变成毛利增厚。来源：[[20260505_manual_decoding-agentic-economy|解码 Agentic Economy]]

* **Cost drivers:** Cost per token depends on accelerator performance, model optimization, routing, caching, memory bandwidth, utilization, and power/data-center constraints. Source: [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]
  > **成本驱动：** 每 token 成本取决于加速器性能、模型优化、路由、缓存、内存带宽、利用率和电力/数据中心约束。来源：[[20260505_manual_decoding-agentic-economy|解码 Agentic Economy]]

* **Demand multiplier:** Agentic workflows increase token demand because tasks require planning, context retrieval, tool use, validation, retries, and state updates. Source: [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]
  > **需求乘数：** Agentic 工作流会提高 token 需求，因为任务需要规划、上下文检索、工具使用、校验、重试和状态更新。来源：[[20260505_manual_decoding-agentic-economy|解码 Agentic Economy]]

## ⚔️ Contradictions & Evolution
* **Margin expansion versus price war:** Goldman Sachs argues token economics are improving, but the thesis can break if competitive pressure pushes token prices down faster than compute costs. Source: [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]
  > **毛利扩张与价格战：** 高盛认为 token 经济性正在改善，但如果竞争压力导致 token 价格下降快于算力成本，命题就会被破坏。来源：[[20260505_manual_decoding-agentic-economy|解码 Agentic Economy]]

## 🚀 Implementations & Best Practices
* **Track the spread:** Monitor LLM API prices, cost per 1M tokens, hyperscaler AI gross margins, and utilization before assuming AI CapEx is earning adequate returns.
  > **跟踪价差：** 在假设 AI 资本开支产生足够回报之前，应跟踪 LLM API 价格、每 100 万 token 成本、hyperscaler AI 毛利和利用率。

* **Segment by workflow:** Evaluate agent ROI by modality, latency, validation burden, and implementation complexity rather than token volume alone.
  > **按工作流分层：** 评估 Agent ROI 时应看模态、延迟、校验负担和实施复杂度，而不能只看 token 量。

## 📚 Source Mentions
* [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]

## 🕸️ Relationships

### Related Concepts
[[ai-agents|AI Agents]], [[ai-capex|AI CapEx]], [[heterogeneous-inference|Heterogeneous Inference]]
> [[ai-agents|AI Agent]]、[[ai-capex|AI 资本开支]]、[[heterogeneous-inference|异构推理]]

### Related Entities
[[nvidia|Nvidia]], [[broadcom|Broadcom]], [[amd|AMD]], [[amazon|Amazon]], [[alphabet|Alphabet]], [[microsoft|Microsoft]]
> [[nvidia|Nvidia]]、[[broadcom|Broadcom]]、[[amd|AMD]]、[[amazon|Amazon]]、[[alphabet|Alphabet]]、[[microsoft|Microsoft]]
