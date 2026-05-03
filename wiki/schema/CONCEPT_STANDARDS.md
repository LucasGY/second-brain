# CONCEPT_STANDARDS.md

## Purpose
A concept page is the evergreen, synthesizing "brain" of the wiki. It is used for abstract ideas, theories, architectures, methodologies, or workflows (e.g., "Retrieval-Augmented Generation", "Agentic Workflow", "Mixture of Experts", "Vibe Coding").

It explains:
- what the concept is (core definition)
- how it works (mechanisms and architecture)
- how the industry's understanding of it is evolving (debates and contradictions)
- how it is applied in practice

## Required Sections
Every concept page MUST contain these sections in this exact order:

1. YAML frontmatter
2. Core Definition
3. Mechanisms & Architecture
4. Contradictions & Evolution
5. Implementations & Best Practices
6. Source Mentions
7. Relationships

## Writing Rules
- Synthesize knowledge from multiple sources; do not just list what individual papers said.
- Assume the reader is a senior algorithm engineer. Be technically precise but clear.
- Explicitly document conflicting information or paradigm shifts (e.g., shifting consensus on chunk sizes in RAG).
- Heavily use Obsidian wikilinks to connect to the specific `[[Entities]]` that implement this concept.
- If the page filename is a normalized slug but the readable concept name contains spaces, case changes, or punctuation, use canonical piped links such as `[[llm-wiki|LLM Wiki]]` instead of relying on the rendered title text as the target.

## Update Rules
- **Core Definition:** Update only when a major paradigm shift fundamentally changes what the concept means.
- **Mechanisms:** Append or refine technical details when new sources provide deeper architectural insights.
- **Contradictions (CRITICAL):** If a new source contradicts an established claim in this wiki, log the conflict here immediately with citations.
- Every major claim MUST cite at least one source page with an inline wikilink.

## Anti-Patterns
Do not:
- turn this into a chronological timeline of news (news belongs in Entity pages).
- copy-paste raw summaries from sources; you must merge and synthesize.
- ignore conflicting data; sweeping contradictions under the rug degrades the wiki's value.
- create concept pages for highly specific, proprietary features (those belong under the tool's Entity page).

## Bilingual Format

English first, Chinese in `>` blockquote immediately below. See CLAUDE.md Section 3.

## Example Template

```markdown
---
type: concept
title: "[Concept Name]"
aliases: [] # List alternative names or acronyms, e.g., ["RAG", "Retrieval-Augmented Gen"]
tags: [concept, #architecture, #methodology] # Replace with specific domain tags
status: [seed | growing | mature] # Choose one to indicate note maturity
first_seen: YYYY-MM-DD
last_updated: YYYY-MM-DD
---

# Core Definition
[Provide a clear, synthesized definition. Explain the theoretical foundation and the core problem it solves.]
> [提供清晰、综合的定义。解释理论基础和它解决的核心问题。]

## 🛠️ Mechanisms & Architecture
[Detail HOW it works. Synthesize the technical steps, mathematical intuition, or pipeline.]
> [详细说明它的工作原理。综合技术步骤、数学直觉或流水线。]
* **Routing Strategy:** [Explanation of how tokens are routed, citing source].
  > **路由策略：** [解释 token 如何被路由，引用来源。]
* **Load Balancing:** [Explanation of load balancing techniques, citing source].
  > **负载均衡：** [解释负载均衡技术，引用来源。]

## ⚔️ Contradictions & Evolution
[Document how the industry understanding has changed, or highlight conflicting opinions/research.]
> [记录行业理解如何变化，或突出来自不同来源的冲突观点/研究。]
* **Debate on X:** [[Source_A_Paper]] argues approach Y is optimal for latency, but [[Source_B_Blog]] found approach Z yields better results in production.
  > **关于 X 的争论：** [[Source_A_Paper]] 认为方法 Y 对延迟最优，但 [[Source_B_Blog]] 发现方法 Z 在生产环境中效果更好。

## 🚀 Implementations & Best Practices
[How is this concept actually used? What are the known pitfalls? Link to specific Entities.]
> [这个概念实际上如何使用？已知的陷阱是什么？链接到具体实体。]
* **Leading Implementations:** [[DeepSeek-V3]], [[Mixtral-8x7B]]
  > **主要实现：** [[DeepSeek-V3]]、[[Mixtral-8x7B]]
* **Engineering Pitfalls:** Be aware of token dropping during heavy load scenarios.
  > **工程陷阱：** 注意高负载场景下的 token 丢失问题。

## 📚 Source Mentions
[A bulleted list of source pages that form the foundation of this concept.]
* [[YYYYMMDD_manual_source_title_1|Source Title 1]]
* [[YYYYMMDD_feeds_source_title_2|Source Title 2]]

## 🕸️ Relationships

### Related Concepts
[[broader-concept|Broader Concept]], [[narrower-concept|Narrower Concept]]

### Related Entities
[[tool-or-model-entity|Tool or Model Entity]]
