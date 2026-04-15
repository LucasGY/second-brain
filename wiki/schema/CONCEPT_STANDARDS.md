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
[Provide a clear, synthesized definition. Explain the theoretical foundation and the core problem it solves. e.g., Mixture of Experts (MoE) is a neural network architecture that...]

## 🛠️ Mechanisms & Architecture
[Detail HOW it works. Synthesize the technical steps, mathematical intuition, or pipeline. Use bullet points or code blocks to explain complex workflows.]
* **Routing Strategy:** [Explanation of how tokens are routed, citing source].
* **Load Balancing:** [Explanation of load balancing techniques, citing source].

## ⚔️ Contradictions & Evolution
[Document how the industry understanding has changed, or highlight conflicting opinions/research from different sources. This is where the synthesis shines.]
* **Debate on X:** [[Source_A_Paper]] argues that approach Y is optimal for latency, but recent empirical tests in [[Source_B_Blog]] found that approach Z yields better results in production environments.

## 🚀 Implementations & Best Practices
[How is this concept actually used? What are the known pitfalls? Link to specific Entities.]
* **Leading Implementations:** [[DeepSeek-V3]], [[Mixtral-8x7B]]
* **Engineering Pitfalls:** Be aware of token dropping during heavy load scenarios.

## 📚 Source Mentions
[A bulleted list of source pages that form the foundation of this concept. Add new sources here when they heavily contribute to the mechanisms above.]
* [[YYYY-MM-DD-source-title-1]]
* [[YYYY-MM-DD-source-title-2]]

## 🕸️ Relationships

### Related Concepts
[[Broader_Concept]], [[Narrower_Concept]]

### Related Entities
[[Tool_or_Model_Entity_1]]
