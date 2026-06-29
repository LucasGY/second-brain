---
type: analysis
frontend_category: deep_dive
source_date: 2026-06-18
title: "Mock Mermaid Markdown Analysis"
title_zh: "Mermaid Markdown 测试分析"
summary: "A temporary Markdown-only Deep Dive card used to verify Mermaid rendering without an HTML artifact."
summary_zh: "一个临时的纯 Markdown Deep Dive 卡片，用于验证没有 HTML 制品时的 Mermaid 渲染。"
entity_ids:
  - amazon
event_tags:
  - close_reading
topic_tags:
  - mock
  - mermaid
  - markdown
status: test
---

# Mermaid Markdown 测试分析

这是一条临时 mock，用来验证没有 `artifact_html` 的 analysis md 是否会进入 Markdown 阅读视图。

## 数据流

```mermaid
graph TD
  A[analysis.md] --> B[Deep Dive loader]
  B --> C[卡片: title + summary]
  C --> D[点击卡片]
  D --> E{是否有 artifact_html?}
  E -->|有| F[iframe HTML artifact]
  E -->|没有| G[Markdown 阅读视图]
  G --> H[Mermaid 图表渲染]
```

## 验证点

- 卡片应该出现在 Deep Dive 的「精读笔记」里。
- 点击卡片后应该看到这段 Markdown 正文。
- 上面的 Mermaid 代码块应该渲染成图，而不是普通代码块。
