#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${SECOND_BRAIN_SYNC_REPO_DIR:-/root/.openclaw/second-brain}"
REMOTE="${SECOND_BRAIN_SYNC_REMOTE:-origin}"
BRANCH="${SECOND_BRAIN_SYNC_BRANCH:-main}"
LOCK_FILE="${SECOND_BRAIN_SYNC_LOCK_FILE:-/tmp/second-brain-git-sync.lock}"
COMMIT_PREFIX="${SECOND_BRAIN_SYNC_COMMIT_PREFIX:-vault sync}"
DRY_RUN=0

for arg in "$@"; do
  case "$arg" in
    --dry-run)
      DRY_RUN=1
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

timestamp() {
  date "+%F %T"
}

log() {
  printf '[%s] %s\n' "$(timestamp)" "$*"
}

run() {
  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "DRY-RUN: $*"
  else
    "$@"
  fi
}

exec 9>"$LOCK_FILE"
if ! flock -xn 9; then
  log "another sync is already running"
  exit 0
fi

cd "$REPO_DIR"

if [[ ! -d .git ]]; then
  log "not a git repository: $REPO_DIR"
  exit 1
fi

current_branch="$(git branch --show-current)"
if [[ "$current_branch" != "$BRANCH" ]]; then
  log "expected branch '$BRANCH' but found '$current_branch'"
  exit 1
fi

log "starting sync for $REPO_DIR on $REMOTE/$BRANCH"

run git fetch "$REMOTE" "$BRANCH"
run git pull --rebase --autostash "$REMOTE" "$BRANCH"
run git add -A

if [[ "$DRY_RUN" -eq 1 ]]; then
  if ! git diff --quiet || ! git diff --cached --quiet || [[ -n "$(git ls-files --others --exclude-standard)" ]]; then
    log "DRY-RUN: local changes detected and would be committed"
  else
    log "DRY-RUN: no local changes to commit"
  fi
else
  if ! git diff --cached --quiet; then
    commit_message="${COMMIT_PREFIX}: $(date '+%F %T')"
    git commit -m "$commit_message"
    log "created commit: $commit_message"
  else
    log "no staged changes to commit"
  fi
fi

ahead_count="$(git rev-list --count "${REMOTE}/${BRANCH}..HEAD")"
if [[ "$ahead_count" -gt 0 ]]; then
  run git push "$REMOTE" "$BRANCH"
  log "pushed $ahead_count commit(s) to $REMOTE/$BRANCH"
else
  log "nothing to push"
fi

log "sync complete"
