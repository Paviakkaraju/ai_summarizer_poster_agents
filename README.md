# AI/ML LinkedIn Automation Workflow
### This project automates the daily workflow of:
* Scraping the latest AI/ML updates from a RSS feed.
* Summarizing the updates using LLMs (Large Language Models).
* Storing the summaries in a JSON file.
* Crafting a LinkedIn post with hashtags based on the summaries.
* Posting the update automatically on LinkedIn.

## Project Structure
```
AI_SUMMARIZER_POSTER/
│
├── agents/
│   ├── posting_agent.py          # LLM - Prepares the LinkedIn post content
│   └── summarizing_agent.py      # LLM -Summarizes scraped articles
│
├── config/
│   └── settings.py               # Project settings and configurations
│
├── tools/
│   ├── linkedin_poster.py         # LinkedIn posting logic
│   ├── summaries.py               # Summary storage handling
│   └── web_scraper.py             # Scrapes AI/ML articles
│
├── workflows/
│   ├── daily_post.py              # Full daily automation workflow
│
├── main_summarize.py              # Script to scrape + summarize
├── main_post.py                   # Script to generate + post LinkedIn content
│
├── summaries.json                 # Stored summaries (output)
├── final_post.txt                 # Generated LinkedIn post (output)
│
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── LICENSE                        # License file
└── .gitignore                     # Files/folders to ignore
```
## Overview
The workflow is divided into two parts:

Part 1: Scrape and Summarize
* Scrape latest AI/ML news and updates using the web_scraper.py.
* Summarize the scraped content with the help of LLMs (summarizing_agent.py).
* Save the summaries into a JSON file (summaries.json).

Part 2: Create and Post on LinkedIn
* Combine all summaries to generate a LinkedIn post with appropriate hashtags using another LLM (posting_agent.py).
* Post the crafted content directly on LinkedIn through the LinkedIn API (linkedin_poster.py).
