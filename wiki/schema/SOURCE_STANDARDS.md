# Source Page Standards (`wiki/sources/`)

**Target Directory:** `wiki/sources/`
**Purpose:** Create a digital proxy for a raw file. A source page distills signal from noise, documents the author's primary intent, and flags assumptions or contradictions. It is NOT a summary; it is a critical reading.

---

## 0. Classification: DOMAIN & DEPTH

Before writing any source page, classify the raw file on two dimensions:

**DOMAIN** — primary subject matter:

| Value | Use When |
|-------|----------|
| `finance` | Analyst reports, earnings, macro data, valuations, investment theses |
| `ai_tech` | AI papers, model releases, architecture blogs, LLM reasoning, agentic systems, MLOps |
| `tooling` | CLI tools, IDE plugins, coding assistants, workflows, dev infrastructure |
| `event` | News, policy changes, corporate announcements, product launches |
| `general` | Philosophy, business strategy, leadership, essays spanning multiple domains |

A source may span two domains. Pick the **primary** for the framework; note the secondary in YAML tags.

**DEPTH** — extraction intensity:

| Value | Condition | Framework |
|-------|-----------|-----------|
| `deep` | Source is from `raw/manual/` | Use Option A/B/C/D (Section 5) |
| `update` | Source is from `raw/feeds/` | Use Feed Template (Section 6) |

---

## 1. File Naming Convention
- **Format:** `YYYYMMDD_[source_type]_[short_title].md`
- **Source Types:** `manual`, `feeds`
- **Example:** `20260414_manual_agentic_rl_survey.md`, `20260503_feeds_karpathy_inference_cost.md`
- The filename stem is the canonical `slug`. Link as `[[YYYYMMDD_source_type_short_title|Readable Title]]`.

## 2. Universal YAML & Header

```yaml
---
type: source
date_ingested: YYYY-MM-DD
domain: [finance | ai_tech | tooling | event | general]
authors: [Author 1, Author 2]
source_url: "https://..."
source_path: "raw/[category]/[platform]/[filename]"
tags: [must include at least one domain tag from index.md]
---
```

```markdown
# [Original Title]

## 📌 TL;DR
[ONE sentence: the core thesis, update, or investment proposition.]
> [对应中文一句话。]
```

---

## 3. Universal Extraction Checklist

Regardless of DOMAIN or DEPTH, always perform:

1. **One-sentence thesis** — the single most important claim or event.
2. **Named entities** — cross-reference `wiki/index.md` to resolve aliases before creating new pages.
3. **Concepts** — identify methodologies/architectures deserving a `wiki/concepts/` page.
4. **Novelty assessment** — NEW info (update definitions) vs. confirmatory (timeline entry only).
5. **Contradiction check** — flag conflicts with existing wiki using `> [!IMPORTANT] CONTRADICTION:` format.

---

## 4. Source-Type Routing

- `raw/manual/` → DEPTH=`deep` → Use ONE framework from Section 5 (A/B/C/D).
- `raw/feeds/` → DEPTH=`update` → Use Section 6 (Feed Template). Do not force short items into deep frameworks.

---

## 5. Deep Frameworks (for `raw/manual/` only)

Choose ONE framework based on DOMAIN. Do NOT mix.

---

### Option A: Finance (Tag: `#finance`)

```markdown
## 🎯 Core Investment Proposition
[What core question does this report answer?]
> [中文]

## 🔍 Critical Breakdown
* **Argument:** [Claim]
  * **Evidence:** [Data]
  * **Evidence Quality:** Strong / Partial / Weak — [why]
  * **Missing Variables:** [Gaps]
  * **Independent Assessment:** Agree / Disagree — [why]

## 👻 Implicit Assumptions
[Unstated premises the author relies on.]
> [中文]

## ⚡ Expectation Gap (预期差)
* **Priced In:** [Consensus knowledge]
* **Marginal Info:** [New edge or contrarian view]

## 📈 Key Tracking Metrics
1. [Metric to validate/falsify]
2. [Metric 2]
```

---

### Option B: AI & Tech (Tag: `#ai_tech`)

```markdown
## 🎯 Core Technical Problem
[What bottleneck is being solved?]
> [中文]

## 💡 Key Innovations
* [Innovation + performance numbers if available]

## 🛠️ Mechanisms & Architecture
[HOW it works. Assume reader is senior engineer.]
> [中文]

## 👻 Limitations & Failure Modes
[Unspoken constraints, known weaknesses.]
> [中文]

## 🔗 Actionability
[How to apply in current/future projects.]
> [中文]
```

---

### Option C: Tooling (Tag: `#tooling`)

```markdown
## 🎯 Primary Use Case
[What friction does this eliminate?]
> [中文]

## 🚀 Setup & Best Practices
* [CLI commands, config snippets]

## ⚠️ Known Pitfalls (踩坑记录)
[What breaks? Workarounds.]
> [中文]
```

---

### Option D: Event & Narrative (Tag: `#event`)

```markdown
## 🎯 Core Event
[What happened? One sentence.]
> [中文]

## 🕐 Timeline & Causality
* **Trigger:** [...] -> **Event:** [...] -> **Consequence:** [...] -> **2nd-Order:** [...]

## 🗺️ Stakeholder Map
* **[Actor]:** [Action, motive, gain/loss]

## 👻 Implicit Assumptions
[What does the narrative assume about future behavior?]
> [中文]

## 🔗 Portfolio / Wiki Relevance
[Connection to tracked entities/concepts.]
> [中文]
```

---

## 6. Feed Update Template (for `raw/feeds/`)

Used for both HIGH and LOW triage scores. Keep event-focused and concise.

```markdown
## 🗓️ Update Event
[One sentence: what happened, who, when.]
> [中文]

## 🔎 Why It Matters
[1-2 sentences: why this is worth preserving.]
> [中文]

## 🧭 Entity Timeline Updates
* [[entity-slug|Entity]]: [Timeline-ready sentence. Source: [[source-slug|Title]]]
  > [[entity-slug|实体]]：[中文时间线句子。来源：[[source-slug|标题]]]

## ⚠️ Caveats / Open Questions
[Uncertainty, missing context, or "None identified."]
> [中文]
```

---

## 7. Universal Graph Linkage

Every source page MUST end with:

```markdown
## 🕸️ Knowledge Graph
**Extracted Entities:** [[entity-slug-1|Entity 1]], [[entity-slug-2|Entity 2]]
**Related Concepts:** [[concept-slug-1|Concept 1]], [[concept-slug-2|Concept 2]]
```
