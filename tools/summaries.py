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
        
def get_all_summaries():
    
    """
    Returns a list of all stored summary objects.
    """
    if summary_file.exists():
        with open(summary_file, "r") as f:
            return json.load(f)
    return []

def clear_summary_file():
    """
    Clears the contents of the summary file by overwriting it with an empty JSON array.
    """
    if summary_file.exists():
        summary_file.write_text("[]")
