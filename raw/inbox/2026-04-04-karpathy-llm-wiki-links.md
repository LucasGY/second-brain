# Karpathy LLM Wiki Pattern

Captured on: 2026-04-06

## Source URLs

- X post: https://x.com/karpathy/status/2039805659525644595
- Gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Capture Notes

This file captures the external references that inspired the repository
structure. The gist describes an "LLM Wiki" pattern where an LLM maintains a
persistent markdown wiki between the user and raw source material.

Key ideas captured from the gist:

- The system should compile knowledge into a maintained wiki, not re-derive it
  from source chunks on every question.
- The architecture has three layers: raw sources, the wiki, and a schema file
  that defines how the LLM should behave.
- Every ingest should update multiple pages, not just create a standalone note.
- `index.md` is the navigation layer and `log.md` is the chronological layer.
- Query results can become durable wiki pages instead of disappearing into chat
  history.
- Linting should check contradictions, stale claims, orphan pages, and missing
  cross-references.
