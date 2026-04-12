---
title: LLM Wiki Pattern
tags: [Concept, Methodology, Knowledge_Management]
---

# LLM Wiki Pattern | LLM Wiki 模式

A methodology where an LLM maintains a persistent markdown wiki to compile and organize knowledge from raw sources.

一种由LLM维护持久Markdown wiki来从原始资料编译和组织知识的方法论。

## Core Principles | 核心原则

1. **Three-Layer Architecture** | 三层架构
   - Raw Sources (不可变原始资料)
   - Wiki (编译后的知识)
   - Schema (定义LLM行为)

2. **Distributed Updates** | 分布式更新
   - Every ingest should update multiple pages
   - Link sources to entities and concepts

3. **Two Index Types** | 两种索引
   - `index.md` = Navigation layer (导航层)
   - `log.md` = Chronological layer (时间顺序层)

4. **Durable Knowledge** | 持久知识
   - Query results become wiki pages
   - Don't re-derive from source chunks every time

5. **Quality Checks** | 质量检查
   - Check for contradictions
   - Find stale claims
   - Identify orphan pages
   - Verify cross-references

## Related Entities
- [[Andrej_Karpathy]]

## Sources
- [[2026-04-04-karpathy-llm-wiki-pattern]]
