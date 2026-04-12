---
title: "Karpathy LLM Wiki Pattern"
date: "2026-04-04"
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
tags: [Methodology, Knowledge_Management]
---

# Karpathy LLM Wiki Pattern | Karpathy LLM Wiki 模式

## Summary | 摘要

A pattern described by Andrej Karpathy where an LLM maintains a persistent markdown wiki between the user and raw source material.

由 Andrej Karpathy 描述的一种模式，其中LLM在用户和原始资料之间维护一个持久的Markdown wiki。

## Key Ideas | 核心概念

### Three-Layer Architecture | 三层架构
1. **Raw Sources** - Immutable source documents
2. **Wiki** - Compiled, maintained knowledge
3. **Schema** - Defines LLM behavior

### Core Principles | 核心原则
- Compile knowledge into maintained wiki, don't re-derive from source chunks
- Every ingest should update multiple pages
- `index.md` = navigation layer
- `log.md` = chronological layer
- Query results become durable wiki pages
- Linting should check contradictions, stale claims, orphan pages, cross-references

## Related Concepts
- [[LLM_Wiki_Pattern]]

## Citation
Source: [Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
