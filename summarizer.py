import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)


def summarize_stories(stories):
    if not stories:
        return "No stories to summarize."

    story_texts = [
        f"{idx+1}. {story['title']} - {story['url']}" for idx, story in enumerate(stories)]
    combined_text = "\n".join(story_texts)

    prompt = f"""Summarize the following news on english in one sentence per news, and tell me what s happening in each news. 
    Return only a numbered list, one sentence per story, no extra formatting, no bullet points.:\n\n{combined_text}\n\nSummary:"""

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


if __name__ == "__main__":
    from scraper import scrape_hackernews
    stories = scrape_hackernews(limit=5)
    summary = summarize_stories(stories)
    print("Summary of top news:")
    print(summary)
