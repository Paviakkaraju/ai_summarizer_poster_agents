from llms.summarizing import system_prompt, model
from tools.web_scraper import get_aiml_updates_yesterday, extract_article_text
from tools.summaries import store_summary
import time
import sys

def safe_print(*args, sep=' ', end='\n'):
    """
    Print function that avoids crashing on UnicodeEncodeError (e.g., emojis in Windows terminal).
    Falls back to ASCII-safe printing if needed.
    """
    try:
        print(*args, sep=sep, end=end)
    except UnicodeEncodeError:
        def strip_unicode(s):
            return s.encode('ascii', errors='ignore').decode()
        safe_args = [strip_unicode(str(arg)) for arg in args]
        print(*safe_args, sep=sep, end=end)


def main():
    print("Fetching recent AI/ML article links...")
    articles = get_aiml_updates_yesterday()

    if not articles:
        print("No articles found.")
        return

    for article in articles:
        title = article.get("title")
        url = article.get("url")
        date = article.get("date")
        safe_print(f"\n📄 Summarizing: {title}")

        content = extract_article_text(url)
        if not content:
            print(f"Could not extract content from: {url}")
            continue

        # Create the full prompt
        prompt = (
            f"{system_prompt}\n\n"
            f"Title: {title}\nDate: {date}\nURL: {url}\n\n"
            f"Content:\n{content}\n\n"
            f"Please summarize the above article."
        )

        # Generate summary
        try:
            response = model.generate_content(prompt)
            summary = response.text.strip()
            
            # Save the summary
            store_summary({
            "title": title,
            "url": url,
            "date": date,
            "summary": summary})

            print("Summary saved.")
    
        except Exception as e:
            print(f"Skipped due to error: {e}")
            time.sleep(20)  # wait before next try
            continue

    
    
if __name__ == "__main__":
    main()