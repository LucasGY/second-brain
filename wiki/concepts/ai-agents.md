---
type: concept
title: "AI Agents"
aliases: ["Agentic AI", "AI Agent", "Agentic Agents"]
tags: [concept, ai_tech, architecture]
status: growing
first_seen: 2026-05-03
last_updated: 2026-05-06
---

# Core Definition
AI agents are AI systems that go beyond single-turn responses by planning, calling tools, executing actions, validating outputs, retrying failures, and updating state across a workflow.
> AI Agent 是超越单轮回答的 AI 系统，会在工作流中进行规划、调用工具、执行动作、校验输出、重试失败并更新状态。

## 🛠️ Mechanisms & Architecture
* **Workflow decomposition:** A task is split into planning, retrieval, tool calls, execution, validation, exception handling, and state updates. Source: [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]
  > **工作流拆解：** 一个任务会被拆分为规划、检索、工具调用、执行、校验、异常处理和状态更新。来源：[[20260505_manual_decoding-agentic-economy|解码 Agentic Economy]]

* **Loop structure:** Agents consume more tokens than chatbots because reliable work requires repeated reasoning and validation loops rather than a single model call. Source: [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]
  > **循环结构：** Agent 比 chatbot 消耗更多 token，因为可靠工作需要反复推理和校验循环，而不是单次模型调用。来源：[[20260505_manual_decoding-agentic-economy|解码 Agentic Economy]]

* **Persistence:** Consumer and enterprise agents can shift from user-initiated sessions to always-on monitoring, which materially increases token intensity. Source: [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]
  > **持续性：** 消费者和企业 Agent 可以从用户触发的会话转向 always-on 监控，从而显著提高 token 强度。来源：[[20260505_manual_decoding-agentic-economy|解码 Agentic Economy]]

## ⚔️ Contradictions & Evolution
* **Capability versus governance:** Technical capability is improving faster than enterprise permissioning, auditability, accountability, and workflow redesign, so adoption may follow an S-curve rather than immediate automation. Source: [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]
  > **能力与治理的矛盾：** 技术能力提升速度快于企业权限、审计、责任归属和流程重构，因此 adoption 更可能呈 S 曲线，而不是立即自动化。来源：[[20260505_manual_decoding-agentic-economy|解码 Agentic Economy]]

## 🚀 Implementations & Best Practices
* **Best early domains:** Text-heavy workflows with strong validation loops, especially coding and structured data tasks, are likely to scale earlier than real-time voice or high-latency multimodal workflows.
  > **最早落地领域：** 文本密集且有强验证闭环的工作流，尤其是编码和结构化数据任务，可能早于实时语音或高延迟多模态工作流规模化。

* **Operational control:** Production agents should be evaluated by ROI, workflow reliability, permissions, audit logs, and token consumption rather than demo quality alone.
  > **运营控制：** 生产环境 Agent 应按 ROI、工作流可靠性、权限、审计日志和 token 消耗评估，而不能只看 demo 效果。

## 📚 Source Mentions
* [[20260503_manual_nat-friedman-daniel-gross-stripe-sessions-ai-agents|Nat Friedman and Daniel Gross on AI Agents]]
* [[20260505_manual_decoding-agentic-economy|Decoding the Agentic Economy]]

## 🕸️ Relationships

### Related Concepts
[[ai-inference-economics|AI Inference Economics]], [[ai-capex|AI CapEx]]
> [[ai-inference-economics|AI 推理经济学]]、[[ai-capex|AI 资本开支]]

### Related Entities
[[microsoft|Microsoft]], [[amazon|Amazon]], [[alphabet|Alphabet]], [[meta|Meta]], [[cloudflare|Cloudflare]]
> [[microsoft|Microsoft]]、[[amazon|Amazon]]、[[alphabet|Alphabet]]、[[meta|Meta]]、[[cloudflare|Cloudflare]]
