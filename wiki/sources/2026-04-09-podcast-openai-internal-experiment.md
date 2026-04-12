---
title: "OpenAI Internal Experiment: 1M LOC in 5 Months with 0% Human Code"
author: "Ryan Lopopolo"
date: "2026-04-09"
source: "https://www.xiaoyuzhoufm.com/episode/69d75624b977fb2c477d8089"
podcast: "跨国串门儿计划 (Latent Space)"
tags: [AI, OpenAI, Coding, Agents, Harness_Engineering]
---

# OpenAI Internal Experiment: 1M LOC in 5 Months with 0% Human Code

## Summary | 摘要

Ryan Lopopolo from OpenAI Frontier shares an extreme experiment: 3-person team, no human code written, produced 1 million lines of code in 5 months, 10x faster than traditional methods. Key insights on Harness Engineering, multi-agent collaboration, and the future of software engineering.

OpenAI Frontier的Ryan Lopopolo分享了一个极端实验：3人团队，不写一行代码，5个月内产出100万行代码，比传统方法快10倍。关于Harness工程、多智能体协作和软件工程未来的关键洞见。

## Key Insights | 关键洞见

### The Extreme Constraint | 极端约束
- **Constraint**: No human writes any code
- **Result**: 1M lines of code, ~1500 PRs, 10x faster
- **Team**: 3 people
- **Duration**: 5 months

### Post-Merge Review | 合并后审查
- Model is highly parallelizable
- Only scarce resource: Human attention
- Most code review happens after merge
- Human attention is the only truly scarce resource

### From Developer to System Architect | 从开发者到系统架构师
- No longer deeply involved in code-level details
- Role like "CTO of a 500-person organization"
- System thinking: Where did agents make mistakes? How to automate away problems?

### Harness Engineering Principles | Harness工程原则
- Build "assembly stations" for agents
- Make errors persistent through documentation
- Skills system for knowledge retention
- "Ghost repos" for software specification distribution

### Symphony Framework | Symphony框架
- Model chose Elixir for orchestration
- BEAM VM's process monitoring perfect for AI task orchestration
- "Don't cage the agent" - give full access to domain
- Trust comes from letting agents prove their work

### Dependency Internalization | 依赖内部化
- **"End of junk plugins"**: If code is free, internalizing dependencies has low friction
- Can strip out generic parts and focus on specific needs
- Enables deeper security review

### Model Limitations | 模型局限
- Cannot jump from new product idea to prototype in one step
- Deepest refactoring still requires human time
- Models and humans are "isomorphic" in capability
- Gap: Getting mental context into model's context

## Statistics | 统计数据
- 1M+ lines of code
- ~1500 PRs
- 3-person team
- 5 months duration
- 10x productivity gain

## Related Entities
- [[OpenAI]]
- [[Codex]]

## Related Concepts
- [[Harness_Engineering]]
- [[AI_Agents]]

## Citation
Source: [跨国串门儿计划](https://www.xiaoyuzhoufm.com/episode/69d75624b977fb2c477d8089)
