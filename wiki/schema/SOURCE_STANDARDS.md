# Source Page Standards (`wiki/sources/`)

**Target Directory:** `wiki/sources/`
**Purpose:** To create a digital proxy for a raw file. A source page must distill the signal from the noise, document the author's primary intent, and explicitly state any assumptions or contradictions. It must NOT be a mere summary; it must be a critical reading.

---

## 1. File Naming Convention
- **Format:** `YYYYMMDD_[source_type]_[short_title].md`
- **Source Types:** `manual` (high intent, manual clipping), `feeds` (automated news/updates)
- **Example:** `20260414_inbox_agentic_rl_survey.md`, `20260414_feed_qqq_macro_update.md`

## 2. Universal Pre-requisites
Every Source page MUST contain this YAML frontmatter and the Universal Header.

---
type: source
date_ingested: YYYY-MM-DD
authors: [Author 1, Author 2, or Institution]
source_url: "https://..." 
source_path: "raw/[category]/[platform]/[filename]"
tags: [inherit from index.md, MUST include at least one domain tag]
---
# [Original Title of the Document]

## 📌 TL;DR
[Exactly ONE sentence summarizing the core thesis, primary update, or investment proposition of this document.]

---

## 3. Dynamic Content Sections (Context-Aware)
Based on the domain of the document (identified via content or tags), apply the appropriate analytical framework below. **Do NOT mix these frameworks.** Choose ONE.

### Option A: Financial & Investment Research (Tag: `#finance`)
*Use this for analyst reports, macro data, QQQ updates, backtests, or market strategy deep-dives.*

## 🎯 Core Investment Proposition
[1-2 sentences explaining what core investment question this report tries to answer.]

## 🔍 Critical Breakdown (Problem-Driven)
*(For 2-3 key arguments in the report, evaluate them using this exact structure)*
* **Question/Argument:** [What is the report claiming?]
  * **Their Evidence:** [What data supports this?]
  * **Evidence Quality:** [Is the logic sound, or are there leaps/assumptions?]
  * **Missing Variables:** [What did they fail to consider?]
  * **Independent Assessment:** [Agree/Disagree and WHY. This is the synthesis.]

## 👻 Implicit Assumptions
[List the silent, critical premises the author relies on but doesn't state explicitly. E.g., "Assumes inflation will remain sticky", or "Assumes VIX will revert to mean".]

## ⚡ Alpha & Expectation Gap (预期差)
* **Market Consensus (Priced In):** [What does everyone already know?]
* **Marginal Information:** [What is the new edge or contrarian view provided here?]

## 📈 Key Tracking Metrics
1. [Metric 1 to validate this thesis]
2. [Metric 2]


### Option B: AI & Tech Research (Tag: `#ai_tech`)
*Use this for AI papers, architecture breakdowns, engineering blogs, MLOps, LLM reasoning, or Agentic AI.*

## 🎯 Core Technical Problem
[What engineering or theoretical bottleneck is this paper/blog trying to solve? E.g., latency in transaction models, hallucination in LLMs.]

## 💡 Key Takeaways & Innovations
* **Innovation 1:** [E.g., A new feature extraction algorithm.]
* **Performance Gain:** [E.g., Reduced latency by X%, improved win rate by Y%.]

## 🛠️ Mechanisms & Architecture
[Explain HOW it works. Synthesize the technical steps. Assume the reader is a senior algorithm engineer.]
*(Detail the pipeline, logic flows, or mathematical intuition if relevant.)*

## 👻 Implicit Assumptions & Limitations
[What are the unspoken constraints? E.g., "Assumes high-quality labeled data is available", or "Only tested in offline backtesting environments".]

## 🔗 Actionability / Integration
[How can this be used in current or future projects? E.g., "This method could be tested in the transaction model feature engineering pipeline."]


### Option C: Tools & Workflows (Tag: `#tooling`)
*Use this for CLI tools, IDE plugins, AI coding assistants, Vibe Coding workflows, or Obsidian setups.*

## 🎯 Primary Use Case
[What specific friction does this tool/workflow eliminate?]

## 🚀 Best Practices & Setup
*(Extract the actionable configuration steps, CLI commands, or prompts.)*
* [Code block or terminal command]
* [Key configuration detail]

## ⚠️ Known Pitfalls (踩坑记录)
[What broke? What doesn't work as advertised? How to work around it.]

---

## 4. Universal Graph Linkage
Every Source page, regardless of domain, MUST end with this section to ensure the wiki remains interconnected:

## 🕸️ Knowledge Graph
**Extracted Entities:** [[Entity1]], [[Entity2]]
**Related Concepts:** [[Concept1]], [[Concept2]]