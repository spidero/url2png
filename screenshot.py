import argparse
import sys
from playwright.sync_api import sync_playwright

def take_screenshot(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        try:
            page.goto(url, timeout=15000)
            # Domyślnie zwraca PNG
            return page.screenshot(full_page=True)
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)
            sys.exit(1)
        finally:
            browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take full page screenshot as PNG')
    parser.add_argument('url', help='URL of the webpage to screenshot')
    parser.add_argument('output', nargs='?', default='-', help='Output file (default: stdout)')
    
    args = parser.parse_args()
    png_data = take_screenshot(args.url)
    
    if args.output == '-':
        sys.stdout.buffer.write(png_data)
    else:
        with open(args.output, 'wb') as f:
            f.write(png_data)
        print(f"Screenshot saved as {args.output}", file=sys.stderr)
