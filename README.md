# URL Scraper Bot 🕸️🤖

**High-fidelity web scraping and batch crawling for content research.**

`url-scrape-bot` is a standalone tool designed to extract clean, structured text and metadata from any website. It uses a headless browser (Playwright) to handle modern JavaScript-heavy sites and supports large-scale batch processing.

## ✨ Key Features
- **High-Fidelity Extraction**: Uses Playwright to render pages exactly like a browser.
- **Batch Processing**: Scrape hundreds of URLs from a single JSON file.
- **Clean Text Output**: Automatically cleans up HTML noise to provide readable markdown/text.
- **Library snapshots**: Saves a permanent JSON record of every scrape for data integrity.

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/andrewbourguignon/url-scrape-bot.git
cd url-scrape-bot
pip install -r requirements.txt
python3 -m playwright install chromium
```

### 2. Usage
**Single URL:**
```bash
python3 scripts/scrape.py --url https://example.com
```

**Batch Mode:**
```bash
python3 scripts/scrape.py --batch examples/batch_template.json
```

## 📁 Output
- **JSON snapshots**: Stored in `library/`
- **Clean text**: Stored in `~/Downloads/Scrapes/` (configurable)

## 🚨 Ethics & Privacy
Please use this tool responsibly. Respect `robots.txt` and avoid aggressive scraping rates on smaller websites.
