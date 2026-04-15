---
type: entity
title: "Claude Managed Agents"
aliases: ["Managed Agents", "Claude Managed"]
tags: [entity, product, agentic_ai]
first_seen: 2026-04-15
last_updated: 2026-04-15
key_sources: [[20260410_manual_anthropic_harness_managed_agents]]
---

# Definition
Claude Managed Agents is Anthropic's managed agent runtime that provides a composable API suite for building and deploying cloud-hosted agents. It handles sandboxed execution, orchestration, permission scoping, and long-running sessions, allowing developers to focus on defining tasks, tools, and guardrails rather than infrastructure.

Claude Managed Agents 是 Anthropic 的托管 Agent 运行时，提供可组合的 API 套件用于构建和部署云托管 Agent。它处理沙箱执行、编排逻辑、权限作用域控制和长时运行会话，让开发者专注于定义任务、工具和护栏，而非基础设施。

## Key Facts
- **Core Capabilities:**
  1. Production-grade agent runtime with safe sandbox, authentication, and tool execution
  2. Long-running sessions with persistent progress and output
  3. Multi-agent coordination with parent/child agent spawning
  4. Trusted governance with scoped permissions and execution tracing
- **Pricing:** $0.08 per active session-hour plus standard token fees
- **Internal Testing:** Up to 10 percentage points higher task success rate vs standard prompting loops

- **核心能力：**
  1. 生产级 Agent 运行时，安全沙箱、身份验证、工具执行
  2. 长时运行会话，进度和输出持久化
  3. 多 Agent 协调，父/子 Agent 派生
  4. 可信治理，作用域权限和执行追踪
- **定价：** 每活跃会话小时 0.08 美元，加标准 token 费用
- **内部测试：** 相比标准提示循环任务成功率提升最多 10 个百分点

## Case Studies
* **Notion:** Integrated Claude directly into workspace for team delegation (private alpha).
* **Sentry:** Paired their debugging agent Seer with Claude-driven agents for patch writing and PR opening. Completed integration in weeks.
* **Asana:** Built AI Teammates that work alongside humans in Asana projects.
* **Rakuten:** Deployed enterprise agents in product, sales, marketing, and finance within one week each.
* **Vibecode:** Uses Managed Agents as default integration; customers launch same infrastructure "at least 10x faster."

## 📅 Evolution Timeline
[Append-only log. Newest entries at top.]

* **[2026-04-10]:** Official launch by Anthropic. Source: [[20260410_manual_anthropic_harness_managed_agents]]

## 📚 Source Mentions
* [[20260410_manual_anthropic_harness_managed_agents]]

## 🕸️ Relationships

### Related Entities
[[anthropic|Anthropic]], [[claude|Claude]], [[notion|Notion]], [[sentry|Sentry]], [[asana|Asana]], [[vibecode|Vibecode]], [[rakuten|Rakuten]]

### Related Concepts
[[harness-engineering|Harness Engineering]], [[multi-agent-coordination|Multi-Agent Coordination]], [[agentic-workflow|Agentic Workflow]]
