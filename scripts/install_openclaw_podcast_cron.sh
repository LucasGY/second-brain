#!/usr/bin/env bash
set -euo pipefail

VENV_PY="/root/.openclaw/.venv/bin/python"
PROMPT="Read /root/.openclaw/second-brain/rss.md and run \`${VENV_PY} /root/.openclaw/second-brain/scripts/podcast_transcriber.py run --max-new-per-feed 1\`. If the command output contains an error, reply with one concise failure line including the key error. If a new markdown transcript is created under /root/.openclaw/second-brain/raw, reply with the created file path. If nothing new is found, reply 'no new podcast transcript'. Keep the reply concise."

openclaw cron add \
  --name "second-brain-podcast-transcriber" \
  --description "Transcribe the latest Xiaoyuzhou RSS episode into second-brain/raw." \
  --every 6h \
  --session isolated \
  --light-context \
  --expect-final \
  --no-deliver \
  --timeout 60000 \
  --timeout-seconds 7200 \
  --tools exec,read,write \
  --message "${PROMPT}"
