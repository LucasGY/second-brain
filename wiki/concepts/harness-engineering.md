---
type: concept
title: "Harness Engineering"
aliases: ["Agent Harness", "Harness"]
tags: [concept, architecture, agentic_ai]
status: seed
first_seen: 2026-04-15
last_updated: 2026-04-15
---

# Core Definition
Harness Engineering is the discipline of designing and building the infrastructure layer that surrounds AI models to make their intelligence actionable in production environments. The core formula: **Agent = Model + Harness**. The model provides intelligence; the harness makes that intelligence practically usable.

Harness Engineering 是设计和构建围绕 AI 模型的基础设施层的学科，使模型智能能够在生产环境中实际使用。核心公式：**Agent = Model + Harness**。模型提供智能，Harness 让智能可以实际使用。

## 🛠️ Mechanisms & Architecture
A harness comprises multiple interconnected components:

* **System Prompts:** Instructions that define agent behavior and constraints.
* **Tools:** Interfaces for the agent to interact with external systems (file system, bash, APIs).
* **Sandbox:** Isolated execution environment for code and actions.
* **Orchestration Logic:** Decision-making framework for when and how to call tools.
* **Checkpoint Mechanisms:** State persistence for long-running sessions.
* **Permission Scoping:** Access controls limiting agent capabilities.
* **Execution Tracing:** Audit trails for debugging and compliance.

**系统提示词：** 定义 Agent 行为和约束的指令。
**工具：** Agent 与外部系统交互的接口（文件系统、bash、API）。
**沙箱：** 代码和操作的隔离执行环境。
**编排逻辑：** 何时及如何调用工具的决策框架。
**检查点机制：** 长时运行会话的状态持久化。
**权限作用域：** 限制 Agent 能力的访问控制。
**执行追踪：** 用于调试和合规的审计跟踪。

### Three Key Design Patterns

**Pattern 1: Use Models' Known Tools**
* Provide agents with tools they already deeply understand rather than purpose-building for each task.
* Example: Claude's bash and text editor tools are general-purpose but deeply understood, improving with model iteration.
* Example: Agent Skills, programmatic tool calling, and memory tools all built from basic tool combinations.
* 提供 Agent 已经深度理解的工具，而非为每个任务专门构建。
* 例如：Claude 的 bash 和文本编辑器工具是通用的但被深度理解，随模型迭代改进。
* 例如：Agent Skills、编程式工具调用、内存工具均由基础工具组合而成。

**Pattern 2: Let Models Decide Autonomously**
* Shift orchestration decisions from harness to model.
* Give the model code execution capability to express tool calls and their logic.
* Model decides which results to process, filter, or pipe—without touching context window.
* Only final code execution output enters the model's context.
* 将编排决策从 harness 转移到模型。
* 给模型代码执行能力来表达工具调用及其逻辑。
* 模型自主决定哪些结果需要处理、过滤或管道传输——不触及上下文窗口。
* 只有代码执行的最终输出才进入模型的上下文。

**Pattern 3: Set Boundaries Carefully**
* Harness encodes assumptions about what models cannot do themselves.
* These assumptions need re-examination as model capabilities improve.
* Dedicated tools with typed parameters can intercept, control, render, or audit operations.
* Boundaries should be based on safety, user experience, and observability requirements.
* Harness 编码了关于模型不能自己做什么的假设。
* 这些假设需要随着模型能力提升而重新检验。
* 带类型参数的专用工具可以拦截、控制、渲染或审计操作。
* 边界应基于安全、用户体验和可观测性需求设置。

## ⚔️ Contradictions & Evolution
* **Traditional View:** Each tool result must pass through the model's context window for decision-making.
* **Emerging View:** Let the model use code execution to orchestrate tool calls autonomously, only surfacing final outputs to context.
* This shift recognizes that powerful coding models are powerful general agents.
* **传统观点：** 每个工具结果必须经过模型上下文窗口来决策。
* **新兴观点：** 让模型使用代码执行自主编排工具调用，只将最终输出呈现给上下文。
* 这一转变认识到：强大的编码模型就是强大的通用 Agent。

## 🚀 Implementations & Best Practices
* **Leading Implementations:** [[claude-managed-agents|Claude Managed Agents]], LangChain Agents, AutoGPT
* **Anti-Patterns:**
  * Over-engineering harnesses with rigid assumptions that become obsolete as models improve.
  * Routing every tool result through context unnecessarily.
  * Missing permission scoping for enterprise deployments.
* **最佳实践：** 保持 Harness 假设与当前模型能力同步；使用代码执行进行自主编排；谨慎选择专用工具的边界。
* **反模式：** 过度设计包含过时假设的 Harness；不必要地将每个工具结果路由到上下文；企业部署缺少权限作用域。

## 📚 Source Mentions
* [[20260410_manual_anthropic_harness_managed_agents]]

## 🕸️ Relationships

### Related Concepts
[[agentic-workflow|Agentic Workflow]], [[multi-agent-coordination|Multi-Agent Coordination]], [[code-generation|Code Generation]]

### Related Entities
[[anthropic|Anthropic]], [[claude-managed-agents|Claude Managed Agents]], [[langchain|LangChain]]
