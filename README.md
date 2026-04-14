# second-brain

A practical "LLM wiki" second brain based on Karpathy's persistent-wiki pattern.
A bilingual knowledge base is the default display format: English appears first,
with the corresponding Chinese directly below it.

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
/root/.openclaw/.venv/bin/python scripts/wiki_tools.py rebuild-index
```

Run a health check:

```bash
/root/.openclaw/.venv/bin/python scripts/wiki_tools.py lint
```

Search wiki pages:

```bash
/root/.openclaw/.venv/bin/python scripts/wiki_tools.py search "your query"
```

Append a log entry:

```bash
/root/.openclaw/.venv/bin/python scripts/wiki_tools.py log ingest "Source title" --details "Created source page and updated overview."
```

Register a raw source in the log:

```bash
/root/.openclaw/.venv/bin/python scripts/wiki_tools.py register-source raw/inbox/example.md --title "Example Source"
```

Sync feeds declared in `rss.md` into `raw/`:

```bash
/root/.openclaw/.venv/bin/python /root/.openclaw/everything-clipper/bin/rss-sync --rss /root/.openclaw/second-brain/rss.md
```

Install the local Whisper dependency in `.venv`:

```bash
/root/.openclaw/.venv/bin/pip install faster-whisper
```

Preview which feed commands would run:

```bash
/root/.openclaw/.venv/bin/python /root/.openclaw/everything-clipper/bin/rss-sync --rss /root/.openclaw/second-brain/rss.md --dry-run --max-new-per-feed 3
```

Install an `openclaw` cron job for periodic RSS sync:

```bash
bash scripts/install_openclaw_podcast_cron.sh
```

Example `rss.md`:

```markdown
# 小宇宙
* https://feed.xyzfm.space/r8t44lmvu99m
* 另一个播客 https://feed.xyzfm.space/example-feed-id

# Twitter
* 某个账号 https://rss.example.com/twitter/user.xml
// 这一行会被忽略
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
- Wiki pages should default to bilingual display with English first and Chinese
  immediately below it.
- `index.md` is for navigation.
- `log.md` is append-only operational history.
- The LLM should prefer updating existing pages over creating duplicates.
- Podcast transcripts are written under `raw/inbox/` as `小宇宙+标题+日期.md`.
- `x.com` list captures are written under `raw/feeds/x.com/<feed>/`.
- Processed podcast episode GUIDs are tracked in `raw/processed/podcast_transcriptions.json`.
- The transcriber uses local `faster-whisper` on CPU (`small` + `int8` by default), so it does not require an API key.
- Episode audio is downloaded to a temporary file under `/tmp` for transcription and removed immediately after the run.
- `rss.md` supports multiple headings, inline labels, blank lines, comment lines, and duplicate URLs.
- `rss-sync` dispatches `小宇宙` feeds to `podcast-transcriber` and `x.com` feeds to `twitter-list`.
