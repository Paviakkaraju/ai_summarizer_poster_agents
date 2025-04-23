import json
from pathlib import Path

summary_file = Path('summaries.json')

def store_summary(summary_obj):
    """
    Stores a single summary object to the JSON file.
    Expected format:
    {
        "title": "Article Title",
        "url": "https://example.com",
        "summary": "Summarized content in 5 lines or less"
    }
    """
    existing = []
    
    if summary_file.exists():
        with open(summary_file, "r") as f:
            existing = json.load(f)
            
    existing.append(summary_obj)
    
    with open(summary_file, "w") as f:
        json.dump(existing, f, indent=2)
        
def load_summaries(json_path="summaries.json"):
    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
def format_articles_for_prompt(summaries):
    return "\n\n".join([
        f"Title: {item['title']}\nURL: {item['url']}\nSummary: {item['summary']}"
        for item in summaries
    ])
    
def reset_posting_files():
    # Reset summaries.json to an empty list
    with open("summaries.json", "w", encoding="utf-8") as f:
        f.write("[]")

    # Clear final_post.txt content
    open("final_post.txt", "w", encoding="utf-8").close()

    print("✅ summaries.json and final_post.txt have been reset.")
