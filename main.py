from scraper import scrape_hackernews
from summarizer import summarize_stories
import datetime
import os


def main():
    try:
        print(
            f"Fetching top news from Hacker News at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
        stories = scrape_hackernews(limit=5)
        summary = summarize_stories(stories)
        print("\nSummary of top news:")
        print(summary)

        os.makedirs('digests', exist_ok=True)
        today = datetime.date.today().strftime('%Y-%m-%d')
        with open(f'digests/{today}.txt', 'w') as f:
            f.write(summary)

        print(f"\nSummary saved to digests/{today}.txt")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
