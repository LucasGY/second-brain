---
title: Harness Engineering
title_zh: Harness Engineering
type: concept
status: active
created: 2026-04-10
updated: 2026-04-11
source_count: 1
summary_en: Harness engineering is the practice of designing the environment around an AI agent so substantial work can be done reliably.
summary_zh: Harness engineering 是围绕 AI 智能体设计环境的一种实践，目的是让大规模工作可以稳定完成。
source_files:
  - raw/inbox/小宇宙+#492.OpenAI 内部实验揭秘：不亲手写一行代码，5个月如何产出百万行代码？+2026-04-09.md
wiki_links:
  - OpenAI Harness Engineering and Million-Line Agentic Software
  - Programming Eats Knowledge Work
  - AI-Native Microteams
  - From Coding Automation to Research Automation
---

# Harness Engineering

## Summary
Harness engineering is the practice of designing the environment around an AI
agent so the agent can perform substantial work reliably: tools, repos,
prompts, review loops, documentation pathways, and operational constraints
matter as much as the base model.

Harness engineering 是围绕 AI 智能体设计环境的一种实践，目标是让智能体能够稳
定完成有分量的工作：工具、仓库、提示词、审查回路、文档路径和操作约束，与底层模
型本身同样重要。

## Key Points
- The objective shifts from directly writing code to building the system
  through which code gets produced, tested, reviewed, and improved.
- Extreme constraints such as "humans do not write code" can expose where the
  real workflow bottlenecks are and force durable automation.
- Human attention becomes focused on supervision, prioritization, and exception
  handling instead of constant implementation.
- Good harnesses persist knowledge by updating documentation, norms, and
  operational memory when incidents or fixes occur.
- The approach implies that agent performance is partly an infrastructure and
  organizational design problem, not just a model-quality problem.

- 目标从“直接写代码”转向“构建一套系统”，让代码在其中被生成、测试、审查和改
  进。
- 像“人类不写代码”这样的极端约束，会暴露真实工作流瓶颈，并倒逼出可持续的自动
  化。
- 人类注意力会更多投入监督、优先级判断和异常处理，而不是持续亲自实现。
- 好的 harness 会在事故或修复发生时，及时更新文档、规范和操作记忆，从而把知识沉
  淀下来。
- 这套方法意味着：智能体表现不只是模型质量问题，也部分是基础设施和组织设计问
  题。

## Evidence
- [OpenAI Harness Engineering and Million-Line Agentic Software](../sources/2026-04-09-openai-harness-engineering.md):
  source note describing the "no human code" experiment, post-merge review,
  and the Symphony workflow.

- [OpenAI Harness Engineering and Million-Line Agentic Software](../sources/2026-04-09-openai-harness-engineering.md)：
  描述“人不写代码”实验、merge 后审查和 Symphony 工作流的来源页。

## Connections
- [[OpenAI Harness Engineering and Million-Line Agentic Software]]: source note
  grounding the term in a concrete engineering practice.
- [[Programming Eats Knowledge Work]]: harnesses are one mechanism that turns
  more work into programmable workflows.
- [[AI-Native Microteams]]: small teams benefit disproportionately when the
  harness captures operating knowledge.
- [[From Coding Automation to Research Automation]]: similar logic may apply to
  research environments, not just coding environments.

- [[OpenAI Harness Engineering and Million-Line Agentic Software]]：把该术语落到
  具体工程实践中的来源页。
- [[Programming Eats Knowledge Work]]：harness 是把更多工作转成可编程工作流的一
  种机制。
- [[AI-Native Microteams]]：当 harness 能捕获操作知识时，小团队会获得不成比例
  的收益。
- [[From Coding Automation to Research Automation]]：类似逻辑可能不只适用于编程
  环境，也适用于研究环境。

## Open Questions
- What are the minimal components of a good harness for non-engineering work?
- How should teams audit harness quality when agents are allowed broad access?
- Which parts of harness design are reusable across organizations versus deeply
  local?

- 面向非工程工作，一个好的 harness 最少需要哪些组件？
- 当智能体被授予广泛权限时，团队应如何审计 harness 的质量？
- harness 设计里哪些部分可以跨组织复用，哪些部分高度本地化？
