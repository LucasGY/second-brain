#!/usr/bin/env bash
set -euo pipefail

RSS_SYNC_BIN="/root/.openclaw/everything-clipper/bin/rss-sync"
RSS_MD="/root/.openclaw/second-brain/rss.md"
OLD_JOB_ID="edf97585-ff26-4853-bd72-10166dace600"

X_PROMPT="Read ${RSS_MD} and run \`/root/.openclaw/.venv/bin/python ${RSS_SYNC_BIN} --rss ${RSS_MD} --skip-podcast\`. Important: only process x.com / twitter-list feeds. If the command output contains an error, reply with one concise failure line including the key error. If new markdown files are created under /root/.openclaw/second-brain/raw/feeds/x.com, reply with the created file paths. If nothing new is found, reply 'no new x clips'. Keep the reply concise."

PODCAST_PROMPT="Read ${RSS_MD} and run \`/root/.openclaw/.venv/bin/python ${RSS_SYNC_BIN} --rss ${RSS_MD} --max-new-per-feed 1 --skip-twitter\`. Important: only process podcast feeds. When using exec, set the command timeout to at least 10800 seconds. If exec returns a running process, keep waiting and polling until it finishes. If the command output contains an error, reply with one concise failure line including the key error. If new markdown files are created under /root/.openclaw/second-brain/raw/feeds/podcast, reply with the created file paths. If nothing new is found, reply 'no new podcast clips'. Keep the reply concise."

if openclaw cron list --json | grep -q "\"id\": \"${OLD_JOB_ID}\""; then
  openclaw cron disable "${OLD_JOB_ID}"
fi

if ! openclaw cron list --json | grep -q '"name": "second-brain-x-rss-sync"'; then
  openclaw cron add \
    --name "second-brain-x-rss-sync" \
    --description "Sync only x.com/twitter-list feeds from rss.md into second-brain/raw/feeds/x.com." \
    --every 1h \
    --session isolated \
    --light-context \
    --expect-final \
    --no-deliver \
    --timeout 60000 \
    --timeout-seconds 1800 \
    --tools exec,read,write \
    --message "${X_PROMPT}"
fi

if ! openclaw cron list --json | grep -q '"name": "second-brain-podcast-rss-sync"'; then
  openclaw cron add \
    --name "second-brain-podcast-rss-sync" \
    --description "Sync only podcast feeds from rss.md into second-brain/raw/feeds/podcast." \
    --every 2h \
    --session isolated \
    --light-context \
    --expect-final \
    --no-deliver \
    --timeout 60000 \
    --timeout-seconds 10800 \
    --tools exec,read,write \
    --message "${PODCAST_PROMPT}"
fi

echo "installed split rss cron jobs"
