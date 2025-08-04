# URL2PNG 🐍📸

**Lightweight Dockerized webpage screenshot tool using Python & Playwright**

Capture full-page screenshots of any website with this ready-to-deploy container solution.

## Quick Start
```bash
# Build the image
docker build -t url2png .

# Alternative: Pipe to stdout
docker run --rm url2png "https://example.com" > screenshot.png
