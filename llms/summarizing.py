import google.generativeai as genai
from tools.web_scraper import get_aiml_updates_yesterday, extract_article_text
from tools.summaries import store_summary
from config.settings import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro-latest")

system_prompt = '''You are an autonomous AI summarizing agent designed to assist with AI/ML news updates." 
                    Your task is to read AI/ML news articles and summarize them in no more than 5 sentences.
                    Make the summary:
                        - Clear and concise
                        - Technically accurate
                        - Professional but engaging (emojis are okay)
                        - Suitable for sharing in a daily update format

                    Focus on the main insights, research contributions, or real-world relevance.
                    '''

