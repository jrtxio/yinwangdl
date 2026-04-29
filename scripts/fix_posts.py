#!/usr/bin/env python3
"""
Fix existing posts:
1. Add title to API-sourced posts (English slug filenames)
2. Convert ![[image.png|650]] Obsidian syntax to standard markdown
"""

import os
import re
import time
from pathlib import Path

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://www.yinwang.org"
API_BASE = f"{BASE_URL}/api/v1"
POSTS_DIR = Path(__file__).resolve().parent.parent / "posts"
IMAGES_DIR = Path(__file__).resolve().parent.parent / "images"

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; yinwangdl-crawler/2.0)"})
session.verify = False


def is_chinese_filename(name):
    """Check if filename contains Chinese characters."""
    return bool(re.search(r'[一-鿿]', name))


def slug_from_filename(filename):
    """Get slug from filename (without .md extension)."""
    return filename[:-3] if filename.endswith('.md') else filename


def fetch_all_titles():
    """Fetch slug->title mapping from API."""
    print("Fetching titles from API...")
    titles = {}
    skip = 0
    limit = 20

    while True:
        try:
            resp = session.get(f"{API_BASE}/posts", params={"skip": skip, "limit": limit})
            resp.raise_for_status()
            data = resp.json()
            posts = data.get("posts", [])
            total = data.get("total", 0)

            for p in posts:
                titles[p["slug"]] = p.get("title", "")

            print(f"  Fetched {len(posts)} posts (skip={skip}, total={total})")
            skip += limit
            if skip >= total or not posts:
                break
            time.sleep(0.5)
        except Exception as e:
            print(f"  API error: {e}")
            break

    print(f"  Got {len(titles)} titles")
    return titles


def parse_frontmatter(text):
    """Parse YAML frontmatter, return (meta_dict, body)."""
    if not text.startswith("---"):
        return {}, text

    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    fm_text = text[4:end]
    body = text[end + 4:]
    if body.startswith("\n"):
        body = body[1:]

    meta = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()

    return meta, body


def build_frontmatter(meta):
    """Rebuild frontmatter string from meta dict."""
    lines = ["---"]
    lines.append(f"dg-publish: {meta.get('dg-publish', 'false')}")
    lines.append(f"title: \"{meta.get('title', '')}\"")
    if meta.get('author'):
        lines.append(f"author: {meta['author']}")
    if meta.get('created'):
        lines.append(f"created: {meta['created']}")
    if meta.get('source'):
        lines.append(f"source: {meta['source']}")
    lines.append("---")
    return "\n".join(lines)


def fix_obsidian_images(body, slug):
    """Convert ![[image.png|650]] or ![[image.png]] to standard markdown."""
    def replacer(m):
        filename = m.group(1)
        # Strip size parameter if present (e.g., image.png|650 -> image.png)
        if '|' in filename:
            filename = filename.split('|')[0]
        return f"![{filename}](/images/{slug}/{filename})"

    return re.sub(r'!\[\[([^\]]+)\]\]', replacer, body)


def fix_existing_images(body, slug):
    """Fix existing relative image paths to absolute paths."""
    body = body.replace(f"../images/{slug}/", f"/images/{slug}/")
    return body


def main():
    api_titles = {}
    files = sorted(os.listdir(POSTS_DIR))
    md_files = [f for f in files if f.endswith('.md')]

    title_fixed = 0
    image_fixed = 0
    api_post_count = 0

    # First pass: collect API-sourced posts (English slug filenames)
    api_posts = []
    for f in md_files:
        if not is_chinese_filename(f):
            api_posts.append(f)

    print(f"Total posts: {len(md_files)}, API-sourced (no Chinese): {len(api_posts)}")

    # Fetch titles from API for API-sourced posts
    if api_posts:
        api_titles = fetch_all_titles()

    # Fix each post
    for f in md_files:
        filepath = POSTS_DIR / f
        slug = slug_from_filename(f)

        text = filepath.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)

        changed = False

        # Fix title for API-sourced posts
        if not is_chinese_filename(f) and 'title' not in meta:
            title = api_titles.get(slug, "")
            if title:
                meta['title'] = title
                changed = True
                title_fixed += 1
                print(f"  + title: {slug} -> {title}")
            else:
                print(f"  ! no API title for: {slug}")

        # Fix Obsidian image syntax
        if '![[' in body:
            body = fix_obsidian_images(body, slug)
            changed = True
            image_fixed += 1

        # Fix relative image paths to absolute
        if f"../images/{slug}/" in body:
            body = fix_existing_images(body, slug)
            changed = True

        if changed:
            new_fm = build_frontmatter(meta)
            filepath.write_text(new_fm + "\n" + body, encoding="utf-8")

    print(f"\nDone! Titles fixed: {title_fixed}, Images fixed: {image_fixed}")


if __name__ == "__main__":
    main()
