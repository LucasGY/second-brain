# FEED_BATCH_STANDARDS.md

**Purpose:** Batch triage protocol for high-volume feed sources (`raw/feeds/`). Use when the user issues a `BATCH-INGEST` command or a feed directory has more than ~20 unprocessed files.

---

## 1. Trigger Conditions

Run this protocol when:
- User says `BATCH-INGEST`, `triage`, or "process all" on a feed directory.
- A feed directory has **>20 unprocessed files** (cross-reference `wiki/log.md`).
- User asks to "catch up" on a feed or "process tweets from [date range]".

For single-item feed ingestion, skip this and use the standard INGEST workflow.

---

## 2. Triage Scoring Rubric

Score each item: **HIGH**, **LOW**, or **NOISE**.

### HIGH → full INGEST (SOURCE_STANDARDS deep framework)

Assign HIGH if the item contains ANY of:
- Specific numerical data (revenue, benchmarks, price targets, growth %)
- A claim that contradicts or significantly updates existing wiki knowledge
- First-person primary source from a tracked entity (CEO announcement, official launch)
- Architecture/mechanism explanation that enriches a `wiki/concepts/` page
- A thread with >5 substantive points building a coherent argument

### LOW → INGEST with Feed Update Template (SOURCE_STANDARDS Section 6)

Assign LOW if the item:
- Confirms existing wiki knowledge with minor new detail
- Reports a routine event (earnings beat, version bump, personnel change)
- Links to an external source with limited commentary
- Is a reply or quote tweet with thin standalone value

Creates a source page + entity timeline update; no deep analysis.

### NOISE → skip entirely, log to audit trail

Assign NOISE if the item is:
- A plain retweet (RT) without added commentary
- Single-sentence opinion with no evidence or data
- Off-topic (outside AI, Finance, Full-stack Dev)
- Duplicate of already-ingested content
- Promotional/spam

---

## 3. Podcast-Specific Override

Podcasts always receive individual INGEST regardless of signal level.
- Use **show notes** as the HIGH-signal anchor (topics, guests, timestamps).
- **Summarize** the transcript; do not reproduce it verbatim.
- Use Option B (ai_tech) or A (finance) based on episode content; Option D for interview/conversation format.

---

## 4. Batch Processing Procedure

### Step A: Scope
- List all files in target directory.
- Cross-reference `wiki/log.md` to skip already-ingested items.
- Report count of unprocessed items.

### Step B: Triage (batches of 30-50)
Score items and produce this summary table:

```
| Score | Count | Items |
|-------|-------|-------|
| HIGH  | N     | [filenames or brief descriptions] |
| LOW   | N     | [filenames or brief descriptions] |
| NOISE | N     | [count only] |
```

### Step C: Human Gate (required — do NOT skip)
Present the summary and wait for explicit approval before touching any wiki pages.
Say: "Ready to ingest [N] HIGH and [M] LOW items. Skip [P] NOISE. Proceed?"

### Step D: Execute
- **HIGH:** full INGEST Steps 1-6.
- **LOW:** INGEST using Source Page Feed Template only; still create source page + entity timeline.
- **NOISE:** log filenames only (see Section 5).

### Step E: Bookkeeping
- Append TRIAGE entry to `wiki/log.md`.
- Update `wiki/index.md` with new source pages.

---

## 5. Audit Trail Format

Append NOISE items under the TRIAGE log entry in `wiki/log.md`:

```markdown
* **NOISE (skipped):** `raw/feeds/.../filename.md` — [one-line reason]
```

---

## 6. TRIAGE Log Entry Format

```markdown
## [YYYY-MM-DD] TRIAGE | [Feed Source Description]
* **Scope:** `raw/feeds/[path]/` — [N] scanned, [M] already ingested (skipped)
* **Results:** [A] HIGH (deep) | [B] LOW (update) | [C] NOISE skipped
* **Source Pages Created:** [[slug-1]], [[slug-2]]
* **Entities Touched:** [[entity-1]], [[entity-2]]
* **NOISE Log:** [C] skipped — plain RTs ([n]), off-topic ([n]), duplicates ([n])
```
