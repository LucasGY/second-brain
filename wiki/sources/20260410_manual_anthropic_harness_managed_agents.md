---
type: source
date_ingested: 2026-04-15
authors: [Datawhale]
source_url: "https://mp.weixin.qq.com/s/66SDrz5_MlBAPwL0xtMFyw"
source_path: "raw/manual/wechat/2026-04-10-重磅！Anthropic官方Harness发布了！.md"
tags: [ai_tech, agentic_ai]
---
# 重磅！Anthropic官方Harness发布了！

## 📌 TL;DR
Anthropic launched Claude Managed Agents, turning the abstract "Agent = Model + Harness" formula into a production-ready managed service that handles sandboxing, orchestration, permission scoping, and long-running sessions.

Anthropic 发布了 Claude Managed Agents，将"Agent = Model + Harness"这一抽象公式转化为生产就绪的托管服务，集成了沙箱隔离、编排逻辑、权限作用域控制和长时运行会话。

---

## 🎯 Core Technical Problem
Building production-grade AI Agents requires substantial infrastructure work—sandboxed code execution, checkpoint mechanisms, credential management, scoped permission controls, and end-to-end tracing—that consumes months before any visible functionality emerges.

构建生产级 AI Agent 需要大量基础设施工作：沙箱化代码执行、检查点机制、凭证管理、作用域权限控制、端到端追踪——这些在出现任何可见功能之前就需要耗费数月。

## 💡 Key Takeaways & Innovations
* **Innovation 1: Managed Agent Runtime.** A complete managed service where developers define tasks, tools, and guardrails; Anthropic's infrastructure handles execution with built-in orchestration harness.
  **创新1：托管 Agent 运行时。** 完整的托管服务：开发者定义任务、工具和护栏，Anthropic 基础设施负责运行，内置编排 harness 处理所有逻辑。
* **Performance Gain:** In internal testing, Managed Agents achieved up to 10 percentage points higher task success rate on structured file generation tasks compared to standard prompting loops, with the largest gains on the hardest problems.
  **性能提升：** 在内部测试中，Managed Agents 在结构化文件生成任务上相比标准提示循环提升了最多10个百分点，在最难的问题上提升幅度最大。

## 🛠️ Mechanisms & Architecture
Claude Managed Agents comprises four core capabilities:

**1. Production-Grade Agent Runtime**
* Safe sandbox, authentication, and tool execution all handled by the platform.
* Developers don't build this infrastructure themselves.
* 安全沙箱、身份验证、工具执行全部由平台处理，开发者无需自建基础设施。

**2. Long-Running Sessions**
* Agents can autonomously work for hours with persistent progress and output.
* Sessions survive disconnections without losing state.
* Agent 可以自主工作数小时，进度和输出持久化保存，连接断开也不会丢失状态。

**3. Multi-Agent Coordination**
* Agents can spawn and direct other agents, parallelizing complex work.
* A parent agent spawns multiple sub-agents for different sub-tasks, then aggregates results.
* Agent 可以生成并指挥其他 Agent，将复杂工作并行化处理，汇总各子 Agent 结果。

**4. Trusted Governance**
* Scoped permissions, identity management, and execution tracing built-in.
* Systematic solution to enterprise concerns about agent overreach.
* 作用域权限、身份管理、执行追踪均已内置，企业最担心的越权问题有了系统性解决方案。

### The Three Design Patterns Behind Claude Managed Agents

**Pattern 1: Use Tools Claude Already Knows**
* Claude achieved 49% on SWE-bench Verified with only two tools: bash and text editor.
* These aren't purpose-built for agents but are deeply understood by Claude and improve with model iteration.
* Claude 在 SWE-bench Verified 上仅用两个工具（bash 和文本编辑器）就达到 49% 成绩。这些工具并非专为 Agent 设计，但 Claude 深度理解它们，且会随模型迭代改进。
* Agent Skills, programmatic tool calling, and memory tools are all built from bash and text editor tool combinations.
* Agent Skills、编程式工具调用、内存工具均由 bash 和文本编辑器工具组合而成。

**Pattern 2: Let Claude Decide Autonomously**
* Traditional assumption: Every tool result must pass through Claude's context window to decide next action.
* Problem: Processing tool results consumes tokens, is slow and expensive.
* Solution: Give Claude a code execution tool (bash). Claude writes code to express tool calls and their logic.
* 传统假设：每个工具结果必须经过 Claude 上下文窗口来决定下一步行动。
* 问题：处理工具结果消耗 token，既慢又贵。
* 解决：给 Claude 一个代码执行工具（如 bash）。Claude 可以编写代码来表达工具调用及其之间的逻辑。
* Claude decides which results to process, which to filter, which to pipe directly to the next call—without touching the context window. Only the final code execution output enters Claude's context.
* Claude 自主决定哪些结果需要处理、哪些可以过滤、哪些直接管道传输到下一个调用。只有代码执行的最终输出才进入 Claude 的上下文。
* Orchestration decisions shift from harness to the model itself. A powerful coding model is a powerful general agent.
* 编排决策从 harness 转移到模型本身。强大的编码模型就是强大的通用 Agent。

**Pattern 3: Set Boundaries Carefully**
* Agent harnesses encode assumptions about "what Claude cannot do itself." These assumptions need re-examination as Claude capabilities improve.
* Bash tool gives Claude broad programming leverage but gives the harness only a command string—each operation has the same shape.
* Agent harness 编码了关于"Claude 不能自己做什么"的假设。随着 Claude 能力提升，这些假设需要重新检验。
* bash 工具给 Claude 广泛的编程杠杆，但只给 harness 一个命令字符串——每个操作形状相同。
* Elevating operations to dedicated tools gives the harness type-parameterized operation hooks that can intercept, control, render, or audit.
* 将操作提升为专用工具，给 harness 提供带类型参数的特定操作钩子，可以拦截、控制、渲染或审计。

## 👻 Implicit Assumptions & Limitations
* **Assumption 1:** The pricing model ($0.08 per active session-hour plus token fees) is acceptable to enterprise customers who expect infrastructure-like billing.
  **假设1：** 定价模式（每小时 0.08 美元会话活跃时间加 token 费用）对期望基础设施式计费的企业客户是可接受的。
* **Assumption 2:** Claude's general-purpose tool composition approach outperforms purpose-built tools for specific domains.
  **假设2：** Claude 的通用工具组合方法在特定领域优于专用工具。
* **Limitation:** The managed service approach locks users into Anthropic's infrastructure, reducing portability.
  **局限性：** 托管服务方式将用户锁定在 Anthropic 基础设施上，降低了可移植性。

## 🔗 Actionability / Integration
* **For Product Teams:** Use Managed Agents to handle long-running tasks like document processing, multi-step workflows, and parallel research tasks without building custom orchestration.
  **对产品团队：** 使用 Managed Agents 处理文档处理、多步骤工作流、并行研究等长时任务，无需自建编排逻辑。
* **For Engineering Teams:** The flexibility in harness design allows Claude Code to run on top, or custom controllers optimized for specific tasks.
  **对工程团队：** Harness 设计的灵活性允许 Claude Code 在上层运行，或针对特定任务优化的自定义控制器。
* **For Enterprise:** Built-in permission scoping and execution tracing address security concerns for deploying agents to real systems.
  **对企业：** 内置权限作用域和执行追踪解决了将 Agent 部署到真实系统时的安全问题。

## 🕸️ Knowledge Graph
**Extracted Entities:** [[anthropic|Anthropic]], [[claude-managed-agents|Claude Managed Agents]], [[claude|Claude]], [[langchain|LangChain]], [[notion|Notion]], [[sentry|Sentry]], [[asana|Asana]], [[vibecode|Vibecode]], [[rakuten|Rakuten]]

**Related Concepts:** [[harness-engineering|Harness Engineering]], [[multi-agent-coordination|Multi-Agent Coordination]], [[agentic-workflow|Agentic Workflow]]
