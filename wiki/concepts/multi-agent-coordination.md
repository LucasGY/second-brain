---
type: concept
title: "Multi-Agent Coordination"
aliases: ["Multi-Agent Systems", "Agent Orchestration"]
tags: [concept, architecture, agentic_ai]
status: seed
first_seen: 2026-04-15
last_updated: 2026-04-15
---

# Core Definition
Multi-Agent Coordination is the architectural pattern where one agent can spawn and direct other agents to parallelize complex work, with a parent agent aggregating results from multiple specialized child agents.

Multi-Agent Coordination 是一种架构模式：一个 Agent 可以生成并指挥其他 Agent 来并行化复杂工作，父 Agent 汇总多个专业化子 Agent 的结果。

## 🛠️ Mechanisms & Architecture
* **Parent Agent:** Spawns sub-agents, assigns tasks, aggregates results.
* **Child Agents:** Specialized agents handling specific sub-tasks in parallel.
* **Result Aggregation:** Parent synthesizes outputs from multiple child agents.
* **Communication Protocols:** Structured interfaces for agent-to-agent messaging.
* **父 Agent：** 生成子 Agent、分配任务、汇总结果。
**子 Agent：** 处理特定子任务的专门 Agent，并行运行。
**结果聚合：** 父 Agent 综合多个子 Agent 的输出。
**通信协议：** Agent 间消息传递的结构化接口。

### Implementation in Claude Managed Agents
* Agents can generate and direct other agents.
* Complex work is parallelized across multiple sub-agents.
* Parent agent spawns multiple children for different sub-tasks, then aggregates results.
* Used in production by Notion (dozens of tasks running in parallel), Rakuten (specialized agents per department).

## 🚀 Implementations & Best Practices
* **Leading Implementations:** [[claude-managed-agents|Claude Managed Agents]], AutoGen, CrewAI
* **Best Practices:**
  * Design clear interfaces between parent and child agents.
  * Implement proper result aggregation logic.
  * Handle partial failures gracefully.
* **工程实践：**
  * 设计清晰的父子 Agent 接口。
  * 实现适当的结果聚合逻辑。
  * 优雅处理部分失败情况。

## 📚 Source Mentions
* [[20260410_manual_anthropic_harness_managed_agents]]

## 🕸️ Relationships

### Related Concepts
[[harness-engineering|Harness Engineering]], [[agentic-workflow|Agentic Workflow]]

### Related Entities
[[claude-managed-agents|Claude Managed Agents]], [[anthropic|Anthropic]]
