---
title: "Perplexity Built on Browser Use - Technical Debt Revealed"
author: "Peter Steinberger"
date: "2026-04-09"
source: "https://x.com/steipete/status/2042554346060075120"
tags: [AI, Perplexity, OpenSource, Tech_Debt]
---

# Perplexity Built on Browser Use - Technical Debt Revealed

## Summary | 摘要

Magnus Müller discovered that Perplexity is built on the Browser Use open-source library. Users had reported last April that Perplexity was randomly searching for "capital of France" and answering "Paris" for unrelated prompts. This exact prompt was hardcoded in Browser Use as a sanity check.

Magnus Müller发现Perplexity基于Browser Use开源库构建。用户去年4月曾报告Perplexity随机搜索"法国首都"并对无关问题回答"巴黎"。这个精确的提示词在Browser Use中被硬编码为完整性检查。

## Key Findings | 关键发现

### Technical Issue | 技术问题
- Perplexity built on Browser Use open-source library
- "Capital of France" hardcoded as sanity check in Browser Use
- Found in `browser_use/agent/service.py` lines 1272–1296
- Perplexity forgot to disable this check

### User Reports | 用户报告
- Users reported random "capital of France" searches
- Perplexity answered "Paris" for unrelated prompts
- This persisted since April 2025

### Comparison | 对比
- Similar situation to Manus AI
- Missing proper integration with open-source dependencies

## Related Entities
- [[Perplexity]]

## Citation
Source: [Peter Steinberger Twitter](https://x.com/steipete/status/2042554346060075120)
