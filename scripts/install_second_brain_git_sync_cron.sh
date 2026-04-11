#!/usr/bin/env bash
set -euo pipefail

CRON_LINE="0 * * * * /root/.openclaw/second-brain/scripts/hourly_git_sync.sh >> /tmp/second-brain-git-sync.log 2>&1"

existing_crontab="$(crontab -l 2>/dev/null || true)"

if grep -Fq "/root/.openclaw/second-brain/scripts/hourly_git_sync.sh" <<<"$existing_crontab"; then
  echo "second-brain git sync cron already installed"
  exit 0
fi

{
  printf '%s\n' "$existing_crontab"
  printf '%s\n' "$CRON_LINE"
} | crontab -

echo "installed hourly second-brain git sync cron"
