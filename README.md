---
name: url-scrape-bot
description: Scrapes data from individual URLs or crawls websites at scale. Supports batch processing and automated extraction for content research.
---

# URL Scraper Bot

## When to use this skill
- When you need to extract text, metadata, or structured data from a specific website.
- When you have a list of hundreds or thousands of URLs that need processing (Batch Mode).
- When performing deep content research for blog posts, scripts, or market analysis.
- When you want to "crawl" a domain to find specific information.

## Workflow

### 1. Single URL Scraping
- [ ] Provide the URL to the bot.
- [ ] Run `scrape.py --url <URL>` to extract content.
- [ ] Results are saved to `library/` and mirrored to `~/Downloads/Scrapes/`.

### 2. Batch Request (At Scale)
- [ ] Create a `urls.txt` or `urls.json` in the `examples/` folder.
- [ ] Run `scrape.py --batch examples/urls.json` to process the list.
- [ ] The bot will handle rate-limiting and headless browser management.

### 3. Web Search & Scrape
- [ ] "Search for [Topic] and scrape the top 10 results."
- [ ] The bot will use search tools to find URLs and then crawl them for data.

## Instructions

### Scrape Script
Location: `scripts/scrape.py`
Usage: `python3 scripts/scrape.py [options]`

**Options:**
- `--url <URL>`: Scrape a single page.
- `--batch <FILE>`: Process a list of URLs from a file.
- `--output <DIR>`: Custom output directory (default: `~/Downloads/Scrapes`).
- `--scale`: (Optional) Trigger Apify Actor for high-volume crawling (requires API token).

### Storage
- **Local Cache**: `library/` contains JSON snapshots of every scrape.
- **User Export**: `~/Downloads/Scrapes/` contains markdown or text versions for easy reading.

## Examples
- `python3 scripts/scrape.py --url https://example.com`
- `python3 scripts/scrape.py --batch examples/competitors.json --scale`

## 🚨 Data Privacy & Ethics
- Always respect `robots.txt` where possible.
- Avoid aggressive scraping that could DNoS a small site.
- Use the `--scale` flag only when necessary for high-volume tasks.
