---
title: Harness Engineering
type: concept
status: active
created: 2026-04-10
updated: 2026-04-10
source_count: 1
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

## Evidence

- [OpenAI Harness Engineering and Million-Line Agentic Software](../sources/2026-04-09-openai-harness-engineering.md):
  source note describing the "no human code" experiment, post-merge review,
  and the Symphony workflow.

## Connections

- [[OpenAI Harness Engineering and Million-Line Agentic Software]]: source note
  grounding the term in a concrete engineering practice.
- [[Programming Eats Knowledge Work]]: harnesses are one mechanism that turns
  more work into programmable workflows.
- [[AI-Native Microteams]]: small teams benefit disproportionately when the
  harness captures operating knowledge.
- [[From Coding Automation to Research Automation]]: similar logic may apply to
  research environments, not just coding environments.

## Open Questions

- What are the minimal components of a good harness for non-engineering work?
- How should teams audit harness quality when agents are allowed broad access?
- Which parts of harness design are reusable across organizations versus deeply
  local?
