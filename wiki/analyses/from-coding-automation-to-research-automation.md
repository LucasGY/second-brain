---
title: From Coding Automation to Research Automation
title_zh: 从编码自动化到研究自动化
type: analysis
status: active
created: 2026-04-10
updated: 2026-04-11
source_count: 2
summary_en: Coding automation and automated research appear as stages on a single capability ladder built on stronger agent autonomy.
summary_zh: 编码自动化和自动化研究看起来像同一条能力阶梯上的不同阶段，核心都依赖更强的智能体自治能力。
source_files:
  - raw/inbox/小宇宙+#492.OpenAI 内部实验揭秘：不亲手写一行代码，5个月如何产出百万行代码？+2026-04-09.md
  - raw/inbox/小宇宙+#493.OpenAI 首席科学家：从自动化研究员到科学发现与AGI 蓝图+2026-04-10.md
wiki_links:
  - OpenAI Harness Engineering and Million-Line Agentic Software
  - Jakub Pachocki on Automated Researchers, Scientific Discovery, and AGI
  - Harness Engineering
  - Automated Researchers
  - Programming Eats Knowledge Work
---

# From Coding Automation to Research Automation

## Summary
### English
These two OpenAI-adjacent conversations describe a single capability ladder:
agent systems first take over narrow coding work inside carefully designed
environments, then extend toward longer-horizon reasoning and eventually
research itself.

### 中文
这两场与 OpenAI 相关的对话描述的是同一条能力阶梯：智能体系统先在精心设计的环
境里接管狭义编码工作，然后再延伸到更长周期的推理，最终走向研究本身。

## Main Argument
### English
The software-engineering story and the automated-research story are not
separate trends. Harness engineering shows how to make agents operationally
useful inside a bounded environment. The automated researcher roadmap extends
the same logic to more ambiguous tasks, where the agent must preserve context,
make intermediate choices, and pursue a goal over much longer intervals.

### 中文
软件工程自动化和研究自动化不是两条彼此分离的趋势。Harness engineering 说明了
如何让智能体在受限环境中真正具有操作价值；自动化研究员路线图则把同一套逻辑延展
到更模糊的任务上，在那里智能体必须保留上下文、做中间决策，并在更长周期里追逐目
标。

## Supporting Observations
### English
- In the coding case, the bottleneck moves from writing code to designing the
  surrounding system: tools, prompts, repos, review loops, and documentation.
- In the research case, the bottleneck moves from solving explicit subproblems
  to sustaining autonomy under vague goals and longer feedback cycles.
- Both cases suggest that human labor migrates upward toward direction-setting,
  taste, decomposition, and verification.
- Both also imply that very small teams may become surprisingly powerful if
  they can reliably command large amounts of automated cognitive work.

### 中文
- 在编码场景里，瓶颈从写代码转向设计周边系统：工具、提示词、仓库、审查回路和文
  档。
- 在研究场景里，瓶颈从解决明确子问题转向在模糊目标和更长反馈周期下维持自治。
- 两者都暗示，人类劳动会继续上移到方向设定、品味、任务拆解和验证。
- 两者也都说明，只要能稳定调度大量自动化认知劳动，极小团队也可能拥有惊人的力量。

## Tensions
### English
- Cheap output can hide brittle systems, weak evaluation, and large maintenance
  burdens.
- Greater autonomy increases the value of governance, monitoring, and clear
  definitions of success.
- Research automation is harder to verify than coding automation because the
  feedback loops are slower and the objectives are often less precise.

### 中文
- 廉价输出可能掩盖脆弱系统、薄弱评估和巨大的维护负担。
- 自治能力越强，治理、监控和成功定义的清晰度就越重要。
- 研究自动化比编码自动化更难验证，因为反馈回路更慢，目标也往往不够精确。

## Evidence
### English
- [OpenAI Harness Engineering and Million-Line Agentic Software](../sources/2026-04-09-openai-harness-engineering.md):
  concrete workflow for turning agents into software producers.
- [Jakub Pachocki on Automated Researchers, Scientific Discovery, and AGI](../sources/2026-04-10-jakub-pachocki-automated-researchers.md):
  capability roadmap and governance frame for longer-horizon autonomy.

### 中文
- [OpenAI Harness Engineering and Million-Line Agentic Software](../sources/2026-04-09-openai-harness-engineering.md)：
  把智能体变成软件生产者的具体工作流。
- [Jakub Pachocki on Automated Researchers, Scientific Discovery, and AGI](../sources/2026-04-10-jakub-pachocki-automated-researchers.md)：
  面向更长周期自治能力的路线图和治理框架。

## Connections
### English
- [[Harness Engineering]]: explains the operational layer that makes coding
  automation work.
- [[Automated Researchers]]: explains the target capability frontier beyond
  engineering tasks.
- [[Programming Eats Knowledge Work]]: higher-level thesis that connects both
  episodes.

### 中文
- [[Harness Engineering]]：解释让编码自动化真正运转起来的操作层。
- [[Automated Researchers]]：解释超越工程任务之后的目标能力前沿。
- [[Programming Eats Knowledge Work]]：连接这两期内容的更高层命题。

## Open Questions
### English
- Which intermediate operating models bridge today's coding agents and future
  automated researchers?
- What new metrics are needed when the task is scientific progress rather than
  correct code?
- How should organizations distribute authority when execution and analysis both
  become much cheaper?

### 中文
- 连接今天编码智能体和未来自动化研究员之间，还会出现哪些中间操作模型？
- 当任务变成科学进展而不是正确代码时，需要什么新的衡量指标？
- 当执行和分析都变得更便宜后，组织应如何重新分配权力？
