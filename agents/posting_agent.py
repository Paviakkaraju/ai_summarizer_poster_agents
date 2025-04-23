import google.generativeai as genai
from config.settings import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro-latest")

system_prompt = '''
                 You are an autonomous AI linkedin posting agent designed to summarize and post AI/ML news updates.
                 The summaries.json contains the summaries of each AIML article posted for yesterday.
                 The summaries.json is formatted as follows:
                 [
                     {
                         "title": "Title of the article",
                         "url": "URL of the article",
                         "date": "Date of the article",
                         "summary": "Summary of the article"
                     },
                     ...
                 ]
                 Your task is to: 
                    1. Collect all the summaries from summaries.json,
                    2. summarize them into a single summary (summary of the summaries)in 3 sentences and
                    3. Create hashtags for the summary of the summaries.
                    
                 
                 Then return the following output:
                 "Today's AI/ML News":
                 <summary of the summaries>
                 
                 <Article1 title, url, summary>

                 <Article2 title, url, summary>

                 <Article3 title, url, summary>
                  ....
                 
                 <hashtags of the summary of the summaries>
                 
                 '''