# second-brain

A practical "LLM wiki" second brain based on Karpathy's persistent-wiki pattern.

This repository turns the idea into a local markdown-first workflow:

- `raw/` stores immutable source material.
- `wiki/` stores the maintained knowledge base.
- `AGENTS.md` tells the LLM how to operate on the wiki.
- `scripts/wiki_tools.py` automates the repetitive maintenance work.

## Why this exists

Traditional RAG re-discovers the same knowledge every time you ask a question.
This repo uses a different pattern: sources are read once, then compiled into a
persistent, interlinked wiki that gets richer over time.

## Repository layout

```text
.
├── AGENTS.md
├── raw/
│   ├── inbox/
│   ├── processed/
│   └── assets/
├── scripts/
│   └── wiki_tools.py
└── wiki/
    ├── index.md
    ├── log.md
    ├── overview.md
    ├── entities/
    ├── concepts/
    ├── sources/
    ├── analyses/
    └── syntheses/
```

## Core workflow

1. Drop new source files into `raw/inbox/`.
2. Ask the LLM to ingest one source at a time using the rules in `AGENTS.md`.
3. The LLM creates or updates pages under `wiki/`.
4. Run tooling to rebuild the index and lint the wiki.
5. Ask questions against the wiki and file useful answers back into `wiki/`.

## Commands

Rebuild the content index:

```bash
python3 scripts/wiki_tools.py rebuild-index
```

Run a health check:

```bash
python3 scripts/wiki_tools.py lint
```

Search wiki pages:

```bash
python3 scripts/wiki_tools.py search "your query"
```

Append a log entry:

```bash
python3 scripts/wiki_tools.py log ingest "Source title" --details "Created source page and updated overview."
```

Register a raw source in the log:

```bash
python3 scripts/wiki_tools.py register-source raw/inbox/example.md --title "Example Source"
```

## Suggested ingest loop

- Read the raw source.
- Create or update `wiki/sources/...` with a concise source note.
- Update affected concept, entity, analysis, and synthesis pages.
- Add or fix wiki links.
- Rebuild `wiki/index.md`.
- Append an entry to `wiki/log.md`.

## Notes

- Raw files are source-of-truth inputs and should stay immutable.
- The wiki is allowed to evolve aggressively as new evidence arrives.
- `index.md` is for navigation.
- `log.md` is append-only operational history.
- The LLM should prefer updating existing pages over creating duplicates.
