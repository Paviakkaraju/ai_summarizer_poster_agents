import feedparser
from datetime import datetime, timedelta
from newspaper import Article

def get_aiml_updates_yesterday(feed_url="https://www.marktechpost.com/feed/"):
    '''
    Fetches AI/ML news articles from the provided RSS feed that were published yesterday.
    
    Args:
        feed_url (str): The URL of the RSS feed (default is MarkTechPost feed).
        
    Returns:
        list: A list of dictionaries containing 'title', 'url', and 'published_date' of each article.
    '''
    
    feed = feedparser.parse(feed_url)
    
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    articles = []

    for entry in feed.entries:
        published_date = datetime(*entry.published_parsed[:6]).date()

        if published_date == yesterday:
            articles.append({
                "title": entry.title,
                "url": entry.link,
                "published_date": published_date
            })

    return articles

def extract_article_text(url):
    '''
    Downloads and extracts the main article content from a given URL.
    
    Args:
        url (str): The URL of the article.
        
    Returns:
        dict: A dictionary containing the article's 'url', 'title', 'text', and 'publish_date'.
    '''
    try:
        article = Article(url)
        article.download()
        article.parse()

        return {
            "URL" : url,
            "title": article.title,
            "text": article.text,
            "publish_date": article.publish_date
        }

    except Exception as e:
        print(f"[Error] Failed to extract article from {url}: {e}")
        return None