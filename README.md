# News Digest

Daily AI-powered news digest from Hacker News, summarized with Google Gemini.

## What it does

1. Scrapes top 5 stories from [Hacker News](https://news.ycombinator.com/)
2. Summarizes each story into one sentence using Google Gemini AI
3. Saves the digest to `digests/YYYY-MM-DD.txt`

## Setup

**Requirements:** Python 3.14+, [uv](https://github.com/astral-sh/uv)

```bash
uv sync
```

Create a `.env` file with your Gemini API key:

```
GEMINI_API_KEY=your_key_here
```

Get a free API key at [Google AI Studio](https://aistudio.google.com/).

## Usage

```bash
uv run main.py
```

## Example output

```
1. Montana passes a Right to Compute Act granting citizens ownership rights over their digital devices.
2. Jazzband collective announces sunsetting in March 2026 due to leadership capacity changes.
3. The bzip compression algorithm is praised for its efficiency despite being overshadowed by newer alternatives.
```

Digest is saved to `digests/2026-03-14.txt`.

## Project structure

```
news-digest/
├── main.py         # Entry point — orchestrates scraping and summarizing
├── scraper.py      # Fetches top stories from Hacker News
├── summarizer.py   # Summarizes stories via Gemini API
├── digests/        # Output directory for daily digests
└── pyproject.toml
```

## Dependencies

- `requests` + `beautifulsoup4` — web scraping
- `google-generativeai` — Gemini API
- `python-dotenv` — loads `.env`
