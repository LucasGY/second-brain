#!/usr/bin/env python3
"""Fetch podcast RSS entries, transcribe audio streams, and save raw markdown sources."""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import html
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw"
STATE_PATH = RAW_DIR / "processed" / "podcast_transcriptions.json"
RSS_PATH = ROOT / "rss.md"

USER_AGENT = "second-brain-podcast-transcriber/1.0"
URL_RE = re.compile(r"https?://[^\s)>]+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transcribe podcast episodes referenced in rss.md."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Process RSS feeds.")
    run_parser.add_argument(
        "--rss",
        default=str(RSS_PATH),
        help="Path to rss.md-style config file.",
    )
    run_parser.add_argument(
        "--max-new-per-feed",
        type=int,
        default=1,
        help="Maximum new episodes to process per feed in a single run.",
    )
    run_parser.add_argument(
        "--include-existing",
        action="store_true",
        help="Ignore state file and reprocess items anyway.",
    )
    run_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List candidate episodes without downloading or transcribing.",
    )

    return parser.parse_args()


def load_env_file(path: pathlib.Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def first_url(text: str) -> str | None:
    match = URL_RE.search(text)
    if not match:
        return None
    return match.group(0).rstrip(".,;")


def infer_feed_kind(source_name: str, group_name: str, url: str) -> str:
    lowered_name = source_name.lower()
    lowered_group = group_name.lower()
    lowered_url = url.lower()
    if "xyzfm.space" in lowered_url or "xiaoyuzhoufm.com" in lowered_url or "小宇宙" in source_name or "小宇宙" in group_name:
        return "podcast"
    if (
        "twitter" in lowered_name
        or "twitter" in lowered_group
        or lowered_group == "x"
        or "x.com" in lowered_url
        or "twitter.com" in lowered_url
    ):
        return "twitter"
    return "unknown"


def parse_feed_line(line: str) -> tuple[str, str] | None:
    stripped = line.strip()
    if not stripped:
        return None
    if stripped.startswith(("<!--", "//", ";")):
        return None

    bullet_match = re.match(r"^[-*+]\s+(.*)$", stripped)
    candidate = bullet_match.group(1).strip() if bullet_match else stripped
    url = first_url(candidate)
    if not url:
        return None

    label = candidate.replace(url, "").strip(" -|\t")
    return url, label


def load_rss_config(path: pathlib.Path) -> list[dict[str, str]]:
    feeds: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    current_name = "Uncategorized"

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue

        if line.startswith("#"):
            heading = line.lstrip("#").strip()
            if heading:
                current_name = heading
            continue

        parsed = parse_feed_line(line)
        if not parsed:
            continue

        url, inline_label = parsed
        if url in seen_urls:
            continue
        seen_urls.add(url)

        source_name = inline_label or current_name
        feeds.append(
            {
                "source_name": source_name,
                "group_name": current_name,
                "url": url,
                "kind": infer_feed_kind(source_name, current_name, url),
                "line_number": str(line_number),
            }
        )
    return feeds


def load_state() -> dict[str, dict[str, object]]:
    if not STATE_PATH.exists():
        return {"processed": {}}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict[str, dict[str, object]]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def fetch_bytes(url: str, timeout: int = 60) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def fetch_xml(url: str) -> ET.Element:
    return ET.fromstring(fetch_bytes(url))


def strip_namespace(tag: str) -> str:
    return tag.split("}", 1)[-1]


def child_text(node: ET.Element, name: str) -> str:
    for child in node:
        if strip_namespace(child.tag) == name:
            return (child.text or "").strip()
    return ""


def find_child(node: ET.Element, name: str) -> ET.Element | None:
    for child in node:
        if strip_namespace(child.tag) == name:
            return child
    return None


def parse_pub_date(raw_value: str) -> dt.datetime:
    parsed = email.utils.parsedate_to_datetime(raw_value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def safe_name(value: str) -> str:
    sanitized = re.sub(r"[\\/:*?\"<>|]+", "-", value)
    sanitized = re.sub(r"\s+", " ", sanitized).strip()
    return sanitized[:120].rstrip(". ") or "untitled"


def slugify(value: str) -> str:
    lowered = value.lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    return lowered.strip("-") or "podcast"


def extract_paragraphs(html_text: str) -> str:
    text = html_text
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p\s*>", "\n\n", text, flags=re.IGNORECASE)

    def replace_link(match: re.Match[str]) -> str:
        href = match.group(1).strip()
        label = re.sub(r"<.*?>", "", match.group(2)).strip()
        if not label:
            return href
        return f"{label} ({href})"

    text = re.sub(
        r"<a [^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>",
        replace_link,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(r"<.*?>", "", text, flags=re.DOTALL)
    text = html.unescape(text)
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
    paragraphs: list[str] = []
    pending_blank = False
    for line in lines:
        if not line:
            if paragraphs:
                pending_blank = True
            continue
        if pending_blank:
            paragraphs.append("")
            pending_blank = False
        paragraphs.append(line)
    return "\n".join(paragraphs).strip()


def enclosure_info(item: ET.Element) -> tuple[str, str]:
    enclosure = find_child(item, "enclosure")
    if enclosure is None:
        raise ValueError("RSS item is missing <enclosure> audio URL.")

    audio_url = enclosure.attrib.get("url", "").strip()
    if not audio_url:
        raise ValueError("RSS item enclosure has no URL.")

    parsed = urllib.parse.urlparse(audio_url)
    suffix = pathlib.Path(parsed.path).suffix or ".bin"
    return audio_url, suffix


def podcast_entries(feed: dict[str, str]) -> list[dict[str, object]]:
    root = fetch_xml(feed["url"])
    channel = root.find("channel")
    if channel is None:
        raise ValueError(f"Feed has no channel: {feed['url']}")

    show_title = child_text(channel, "title") or feed["source_name"]
    entries: list[dict[str, object]] = []
    for item in channel.findall("item"):
        title = child_text(item, "title")
        guid = child_text(item, "guid") or child_text(item, "link") or title
        pub_date = parse_pub_date(child_text(item, "pubDate"))
        description_html = child_text(item, "description") or child_text(item, "encoded")
        link = child_text(item, "link")
        audio_url, audio_suffix = enclosure_info(item)
        entries.append(
            {
                "source_name": feed["source_name"],
                "group_name": feed["group_name"],
                "feed_url": feed["url"],
                "show_title": show_title,
                "title": title,
                "guid": guid,
                "pub_date": pub_date,
                "pub_date_iso": pub_date.date().isoformat(),
                "description_text": extract_paragraphs(description_html),
                "episode_url": link,
                "audio_url": audio_url,
                "audio_suffix": audio_suffix,
            }
        )
    entries.sort(key=lambda item: item["pub_date"], reverse=True)
    return entries


def download_audio_to_temp(audio_url: str, suffix: str) -> pathlib.Path:
    request = urllib.request.Request(audio_url, headers={"User-Agent": USER_AGENT})
    with tempfile.NamedTemporaryFile(prefix="podcast-", suffix=suffix, delete=False) as handle:
        with urllib.request.urlopen(request, timeout=600) as response:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                handle.write(chunk)
        return pathlib.Path(handle.name)


def transcribe_with_faster_whisper(audio_url: str, audio_suffix: str) -> str:
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:  # pragma: no cover - runtime dependency
        raise RuntimeError(
            "faster-whisper is not installed in /root/.openclaw/.venv."
        ) from exc

    model_name = os.environ.get("PODCAST_WHISPER_MODEL", "small")
    language = os.environ.get("PODCAST_WHISPER_LANGUAGE", "zh")
    compute_type = os.environ.get("PODCAST_WHISPER_COMPUTE_TYPE", "int8")
    beam_size = int(os.environ.get("PODCAST_WHISPER_BEAM_SIZE", "5"))

    audio_path = download_audio_to_temp(audio_url, audio_suffix)
    try:
        model = WhisperModel(model_name, device="cpu", compute_type=compute_type)
        segments, _info = model.transcribe(
            str(audio_path),
            language=language,
            beam_size=beam_size,
        )
        text_parts = [segment.text.strip() for segment in segments if segment.text.strip()]
        transcript = "\n\n".join(text_parts).strip()
        if not transcript:
            raise RuntimeError("faster-whisper returned no transcript text.")
        return transcript
    finally:
        audio_path.unlink(missing_ok=True)


def transcribe_audio(audio_url: str, audio_suffix: str) -> tuple[str, str]:
    backend = os.environ.get("PODCAST_TRANSCRIBE_BACKEND", "faster-whisper").strip().lower()
    if backend == "faster-whisper":
        return transcribe_with_faster_whisper(audio_url, audio_suffix), "faster-whisper"
    raise RuntimeError("Unsupported PODCAST_TRANSCRIBE_BACKEND. Use 'faster-whisper'.")


def build_markdown(entry: dict[str, object], transcript: str, backend: str) -> str:
    title = str(entry["title"])
    published = str(entry["pub_date_iso"])
    episode_url = str(entry["episode_url"])
    description_text = str(entry["description_text"]).strip()

    frontmatter_lines = [
        "---",
        f'title: "{title.replace(chr(34), chr(39))}"',
        'source_type: "podcast-transcript"',
        f'platform: "{entry["source_name"]}"',
        f'show_title: "{str(entry["show_title"]).replace(chr(34), chr(39))}"',
        f'published: "{published}"',
        f'episode_url: "{episode_url}"',
        f'audio_url: "{entry["audio_url"]}"',
        f'feed_url: "{entry["feed_url"]}"',
        f'guid: "{str(entry["guid"]).replace(chr(34), chr(39))}"',
        f'transcription_backend: "{backend}"',
        "---",
        "",
        f"# {title}",
        "",
        "## Metadata",
        "",
        f"- 平台: {entry['source_name']}",
        f"- 播客: {entry['show_title']}",
        f"- 日期: {published}",
        f"- 单集链接: {episode_url}",
        f"- 音频流: {entry['audio_url']}",
        f"- RSS: {entry['feed_url']}",
        "",
    ]

    if description_text:
        frontmatter_lines.extend(
            [
                "## Show Notes",
                "",
                description_text,
                "",
            ]
        )

    frontmatter_lines.extend(
        [
            "## Transcript",
            "",
            transcript.strip(),
            "",
        ]
    )
    return "\n".join(frontmatter_lines)


def output_path_for_entry(entry: dict[str, object]) -> pathlib.Path:
    filename = f"{entry['source_name']}+{safe_name(str(entry['title']))}+{entry['pub_date_iso']}.md"
    return RAW_DIR / filename


def process_entry(entry: dict[str, object], state: dict[str, dict[str, object]], dry_run: bool) -> pathlib.Path | None:
    output_path = output_path_for_entry(entry)
    if dry_run:
        print(f"[dry-run] {output_path.relative_to(ROOT)}")
        return output_path

    transcript, backend = transcribe_audio(
        str(entry["audio_url"]),
        str(entry["audio_suffix"]),
    )
    output_path.write_text(
        build_markdown(entry, transcript, backend),
        encoding="utf-8",
    )
    state["processed"][str(entry["guid"])] = {
        "title": entry["title"],
        "published": entry["pub_date_iso"],
        "output_path": output_path.relative_to(ROOT).as_posix(),
        "updated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    save_state(state)
    print(f"Wrote {output_path.relative_to(ROOT)}")
    return output_path


def run(args: argparse.Namespace) -> int:
    rss_path = pathlib.Path(args.rss).resolve()
    feeds = load_rss_config(rss_path)
    state = load_state()
    processed = state.setdefault("processed", {})

    anything_processed = False
    for feed in feeds:
        if feed["kind"] != "podcast":
            print(
                f"Skipping unsupported feed kind '{feed['kind']}' for {feed['source_name']} -> {feed['url']}",
                file=sys.stderr,
            )
            continue

        print(f"Checking {feed['source_name']} -> {feed['url']}")
        try:
            entries = podcast_entries(feed)
        except (ValueError, urllib.error.URLError, ET.ParseError) as exc:
            print(f"Failed to load feed {feed['url']}: {exc}", file=sys.stderr)
            continue

        pending_entries = [
            entry
            for entry in entries
            if args.include_existing or str(entry["guid"]) not in processed
        ]
        if args.max_new_per_feed >= 0:
            pending_entries = pending_entries[: args.max_new_per_feed]

        if not pending_entries:
            print("No new episodes found.")
            continue

        for entry in pending_entries:
            try:
                result = process_entry(entry, state, args.dry_run)
            except Exception as exc:  # noqa: BLE001
                print(f"Failed to process '{entry['title']}': {exc}", file=sys.stderr)
                continue
            anything_processed = anything_processed or bool(result)

    return 0 if anything_processed or args.dry_run else 0


def main() -> int:
    load_env_file(pathlib.Path("/root/.openclaw/.env"))
    load_env_file(ROOT / ".env")
    args = parse_args()
    if args.command == "run":
        return run(args)
    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
