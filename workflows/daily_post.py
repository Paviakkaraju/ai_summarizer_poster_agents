import schedule
import time
import subprocess
import os

python_path = os.path.abspath("../venv/Scripts/python.exe")

summarize_path = os.path.abspath("../main_summarize.py")
post_path = os.path.abspath("../main_post.py")

def job():
    subprocess.run([python_path, summarize_path])
    subprocess.run([python_path, post_path])
    

schedule.every().day.at("08:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
    