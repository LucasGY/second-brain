---
title: "Steipete: Perplexity Built on Browser Use - Tech Debt Revealed"
author: "Peter Steinberger"
date: "2026-04-09"
source: "https://x.com/steipete/status/2042554346060075120"
tags: [AI, Perplexity, Browser_Use, Open_Source, Tech_Debt]
---

# Steipete: Perplexity Built on Browser Use - Tech Debt Revealed

## Summary | 摘要

Magnus Müller reveals Perplexity is built on Browser Use open-source library, with a sanity check prompt ("capital of France") hardcoded in. Users reported random "Paris" answers for unrelated queries - a bug from the integration oversight.

Magnus Müller揭示Perplexity建立在Browser Use开源库上，带有一个硬编码的完整性检查提示（"法国首都"）。用户报告了不相关查询随机回答"巴黎"的问题——这是集成疏忽导致的bug。

## Key Points | 关键要点

### Discovery | 发现
- **Tech stack**: Perplexity built on Browser Use | 技术栈：Perplexity建立在Browser Use上
- **Hardcoded check**: "Capital of France" = "Paris" | 硬编码检查："法国首都"="巴黎"
- **Bug**: Random Paris answers for unrelated queries | bug：不相关查询随机回答巴黎

### Technical Details | 技术细节
- **Source**: browser_use/agent/service.py | 源码：browser_use/agent/service.py
- **Purpose**: Sanity check in _verify_llm_connection | 目的：_verify_llm_connection中的完整性检查
- **Issue**: Sent on every Agent() instantiation | 问题：每次Agent()实例化时发送

### Industry Implications | 行业影响
- **Open source**: Building on without proper integration | 开源：在没有适当集成的情况下构建
- **Manus comparison**: Similar to Manus situation | Manus比较：类似于Manus情况
- **Transparency**: Could have asked for help | 透明度：本可以请求帮助

## Related Entities
- [[OpenAI]]

## Related Concepts
- [[AI_Agents]]
- [[Productivity]]

## Citation
Source: [Steipete Tweet](https://x.com/steipete/status/2042554346060075120)
