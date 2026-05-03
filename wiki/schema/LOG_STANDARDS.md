# LOG_STANDARDS.md

## Purpose
`log.md` is the chronological audit trail of the wiki. It records exactly what the LLM did, when it did it, and what pages were affected.
It is critical for rollback, debugging LLM hallucinations, and understanding the recent trajectory of the knowledge base.

## Required Sections
The file has NO sections. It is a pure, flat, append-only ledger.

## Writing & Update Rules
- **APPEND ONLY:** The LLM must NEVER modify or delete historical entries. It must only append to the very bottom of the file.
- **Strict Syntax:** Every log entry MUST follow a rigid, grep-friendly format. This allows simple terminal commands (like `tail -n 10 log.md`) to parse recent activity.
- **Action Verbs:** Use standardized action verbs: `INGEST`, `TRIAGE`, `LINT`, `SYNTHESIZE`, `UPDATE`.
  - `INGEST` — a single source file was processed into the wiki.
  - `TRIAGE` — a batch of feed items was scored and routed (HIGH/LOW/NOISE). Use this for `BATCH-INGEST` sessions.
  - `LINT` — a health check was run on the wiki (contradictions, orphans, stale links).
  - `SYNTHESIZE` — a cross-source analysis or query was compiled into a new page.
  - `UPDATE` — an existing page was manually edited outside of an INGEST workflow.

## Anti-Patterns
Do not:
- write prose or conversational text in this file.
- omit the affected wikilinks (touched pages). If a page was modified, it MUST be linked in the log entry.
- rewrite the file.

## File Template (`wiki/log.md`)

```markdown
# 🕰️ System Operation Log

[This file is append-only. Do not edit previous entries.]

## [2026-04-10] INGEST | DeepSeek V3 Architecture Release
* **Source Created:** [[20260410_inbox_DeepSeek_MoE_Architecture]]
* **Touched:** Updated `Mechanisms` in [[Mixture of Experts]]; Added timeline event to [[DeepSeek-V3]].

## [2026-04-12] SYNTHESIZE | QQQ Investment Strategy Comparison
* **Action:** Generated comparison matrix based on user prompt.
* **Source Created:** N/A (Synthesis query)
* **Touched:** Added new insights to [[QQQ Strategy]] concept page.

## [2026-04-14] INGEST | Karpathy LLM Wiki Gist
* **Source Created:** [[20260414_inbox_karpathy_llm_wiki]]
* **Touched:** Created new concept [[LLM-maintained Knowledge Base]]; Updated [[Obsidian]] entity page.

## [2026-05-03] TRIAGE | x.com/list-2010668465980424307 (AI list)
* **Scope:** `raw/feeds/x.com/2010668465980424307/` — 45 items scanned, 3 already ingested (skipped)
* **Results:** 6 HIGH ingested (deep) | 14 LOW ingested (update) | 22 NOISE skipped
* **Source Pages Created:** [[20260503_feeds_openai_gpt5_launch]], [[20260503_feeds_karpathy_inference_cost]]
* **Entities Touched:** [[openai]], [[andrej-karpathy]]
* **NOISE Log:** 22 items skipped — plain RTs (14), off-topic (5), duplicates (3)