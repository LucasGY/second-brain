# INDEX_STANDARDS.md

## Purpose
`index.md` is the global map of the wiki. It is the very first file the LLM reads to understand the current state of the knowledge base, discover existing pages, and avoid creating duplicate entities. 
**It is the source of truth for semantic navigation.**

## Required Sections
The file MUST contain these sections in this exact order:
1. Concept Map (Abstract theories & workflows)
2. Entity Directory (Concrete tools, models, people)
3. Source Directory (Chronological list of ingested raw files)

## Writing & Update Rules
- **Formatting is paramount:** Every item MUST be a bullet point containing a wikilink, followed by a one-line description.
- **Deduplication Check:** Before the LLM creates a new Concept or Entity, it MUST scan this file to ensure it or its aliases don't already exist.
- **Alphabetical/Chronological sorting:** Entities and Concepts should ideally be sorted alphabetically. Sources MUST be sorted chronologically (newest at the bottom).
- **Canonical targets:** The wikilink target should always use the page slug or relative file path target, not an unstable display variant. If using Obsidian-style wikilinks in examples, prefer `[[slug|Readable Name]]`.

## Anti-Patterns
Do not:
- write long paragraphs explaining the links here. One line max.
- use tags here; tags belong in the YAML of the individual pages.
- rewrite the whole file just to add one link. Use surgical appends or precise insertions.

## File Template (`wiki/index.md`)

```markdown
# 🗺️ Global Index

## 🧠 Concept Map
[List of all `wiki/concepts/` files. Alphabetical order.]
* [[Agentic Workflow]] - AI systems executing tasks with varying degrees of autonomy.
* [[mixture-of-experts|Mixture of Experts]] - Neural network architecture routing tokens to specialized subnetworks.
* [[vibe-coding|Vibe Coding]] - Rapid prototyping using LLMs and natural language commands.

## 🏢 Entity Directory
[List of all `wiki/entities/` files. Alphabetical order.]
* [[claude-3-5|Claude 3.5]] - Foundation model developed by Anthropic.
* [[deepseek-v3|DeepSeek-V3]] - Open-weight MoE model by DeepSeek.
* [[obsidian|Obsidian]] - Local-first markdown knowledge base.

## 📚 Source Directory
[List of all `wiki/sources/` files. Chronological order, oldest to newest.]
* [[20251128_inbox_ai_coding_assistants|20251128_inbox_AI_coding_assistants]] - Review of early AI coding tools.
* [[20260410_inbox_deepseek_moe_architecture|20260410_inbox_DeepSeek_MoE_Architecture]] - Technical breakdown of the V3 routing logic.
* [[20260414_inbox_karpathy_llm_wiki|20260414_inbox_karpathy_llm_wiki]] - The foundational architecture for this knowledge base.
