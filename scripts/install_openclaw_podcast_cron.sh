#!/usr/bin/env bash
set -euo pipefail

CLIPPER_BIN="/root/.openclaw/everything-clipper/bin/rss-sync"
PROMPT="Read /root/.openclaw/second-brain/rss.md and run \`/root/.openclaw/.venv/bin/python ${CLIPPER_BIN} --rss /root/.openclaw/second-brain/rss.md --max-new-per-feed 1\`. Important: when using exec, set the command timeout to at least 10800 seconds. If exec returns a running process, keep waiting and polling until it finishes; do not abandon the job early just because transcription is quiet for a while. Use the script's progress output to judge status. If the command output contains an error, reply with one concise failure line including the key error. If new markdown files are created under /root/.openclaw/second-brain/raw/inbox, reply with the created file paths. If nothing new is found, reply 'no new rss clips'. Keep the reply concise."

openclaw cron add \
  --name "second-brain-rss-sync" \
  --description "Sync rss.md feeds into second-brain/raw/inbox with the matching everything-clipper command." \
  --every 2h \
  --session isolated \
  --light-context \
  --expect-final \
  --no-deliver \
  --timeout 60000 \
  --timeout-seconds 10800 \
  --tools exec,read,write \
  --message "${PROMPT}"
