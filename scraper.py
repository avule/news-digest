import requests
from bs4 import BeautifulSoup


def scrape_hackernews(limit=10):
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.select(".titleline > a")
    stories = []
    for title in titles[:limit]:
        story = {
            "title": title.text,
            "url": title["href"]
        }
        stories.append(story)
    return stories


if __name__ == "__main__":
    stories = scrape_hackernews(limit=5)
    for i, story in enumerate(stories, 1):
        print(f"{i}. {story['title']}")
        print(f"   {story['url']}")
        print()
