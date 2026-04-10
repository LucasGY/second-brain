---
title: From Coding Automation to Research Automation
type: analysis
status: active
created: 2026-04-10
updated: 2026-04-10
source_count: 2
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

These two OpenAI-adjacent conversations describe a single capability ladder:
agent systems first take over narrow coding work inside carefully designed
environments, then extend toward longer-horizon reasoning and eventually
research itself.

## Main Argument

The software-engineering story and the automated-research story are not
separate trends. Harness engineering shows how to make agents operationally
useful inside a bounded environment. The automated researcher roadmap extends
the same logic to more ambiguous tasks, where the agent must preserve context,
make intermediate choices, and pursue a goal over much longer intervals.

## Supporting Observations

- In the coding case, the bottleneck moves from writing code to designing the
  surrounding system: tools, prompts, repos, review loops, and documentation.
- In the research case, the bottleneck moves from solving explicit subproblems
  to sustaining autonomy under vague goals and longer feedback cycles.
- Both cases suggest that human labor migrates upward toward direction-setting,
  taste, decomposition, and verification.
- Both also imply that very small teams may become surprisingly powerful if
  they can reliably command large amounts of automated cognitive work.

## Tensions

- Cheap output can hide brittle systems, weak evaluation, and large maintenance
  burdens.
- Greater autonomy increases the value of governance, monitoring, and clear
  definitions of success.
- Research automation is harder to verify than coding automation because the
  feedback loops are slower and the objectives are often less precise.

## Evidence

- [OpenAI Harness Engineering and Million-Line Agentic Software](../sources/2026-04-09-openai-harness-engineering.md):
  concrete workflow for turning agents into software producers.
- [Jakub Pachocki on Automated Researchers, Scientific Discovery, and AGI](../sources/2026-04-10-jakub-pachocki-automated-researchers.md):
  capability roadmap and governance frame for longer-horizon autonomy.

## Connections

- [[Harness Engineering]]: explains the operational layer that makes coding
  automation work.
- [[Automated Researchers]]: explains the target capability frontier beyond
  engineering tasks.
- [[Programming Eats Knowledge Work]]: higher-level thesis that connects both
  episodes.

## Open Questions

- Which intermediate operating models bridge today's coding agents and future
  automated researchers?
- What new metrics are needed when the task is scientific progress rather than
  correct code?
- How should organizations distribute authority when execution and analysis both
  become much cheaper?
