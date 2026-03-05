import os
import sys
import json
import argparse
import asyncio
from datetime import datetime
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# Ensure local library and download folder exist
LIB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "library")
DOWNLOAD_DIR = os.path.expanduser("~/Downloads/Scrapes")

os.makedirs(LIB_DIR, exist_ok=True)
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def scrape_url(url, headless=True):
    """
    Scrapes a single URL using Playwright for high-fidelity content extraction.
    """
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=headless)
            context = await browser.new_context(viewport={'width': 1280, 'height': 800})
            page = await context.new_page()
            
            print(f"Scraping: {url}")
            await page.goto(url, wait_until="networkidle", timeout=60000)
            
            # Extract content
            title = await page.title()
            content = await page.content()
            
            # Use BeautifulSoup for cleaner text extraction
            soup = BeautifulSoup(content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
                
            text = soup.get_text(separator='\n')
            
            # Clean up the text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            clean_text = '\n'.join(chunk for chunk in chunks if chunk)
            
            result = {
                "url": url,
                "title": title,
                "timestamp": datetime.now().isoformat(),
                "content": clean_text
            }
            
            await browser.close()
            return result
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

def save_result(result):
    if not result:
        return
        
    domain = result['url'].split("//")[-1].split("/")[0].replace(".", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{domain}_{timestamp}"
    
    # Save JSON to library
    json_path = os.path.join(LIB_DIR, f"{filename}.json")
    with open(json_path, 'w') as f:
        json.dump(result, f, indent=4)
        
    # Save Text to Downloads
    txt_path = os.path.join(DOWNLOAD_DIR, f"{filename}.txt")
    with open(txt_path, 'w') as f:
        f.write(f"SOURCE: {result['url']}\n")
        f.write(f"TITLE: {result['title']}\n")
        f.write(f"DATE: {result['timestamp']}\n")
        f.write("-" * 40 + "\n\n")
        f.write(result['content'])
        
    print(f"Saved to: {txt_path}")

async def main():
    parser = argparse.ArgumentParser(description="URL Scraper Bot - High-fidelity web scraping.")
    parser.add_argument("--url", help="Single URL to scrape")
    parser.add_argument("--batch", help="Path to a JSON file containing a list of URLs")
    parser.add_argument("--scale", action="store_true", help="Trigger Apify for large scale (placeholder)")
    
    args = parser.parse_args()
    
    if args.url:
        result = await scrape_url(args.url)
        save_result(result)
    elif args.batch:
        if not os.path.exists(args.batch):
            print(f"Error: Batch file {args.batch} not found.")
            return
            
        with open(args.batch, 'r') as f:
            data = json.load(f)
            urls = data.get("urls", [])
            
        print(f"Starting batch scrape for {len(urls)} URLs...")
        for url in urls:
            result = await scrape_url(url)
            save_result(result)
    else:
        parser.print_help()

if __name__ == "__main__":
    asyncio.run(main())
