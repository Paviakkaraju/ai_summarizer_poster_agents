from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def post_on_linkedin(username, password, post_text, dry_run=True):
    """
    Logs into LinkedIn and optionally posts the given text using JS injection (emoji-safe).
    
    Args:
        username (str): LinkedIn email
        password (str): LinkedIn password
        post_text (str): Text content to post (can include emojis)
        dry_run (bool): If True, does everything except click 'Post'
    """

    # Setup Chrome options
    options = Options()
    # Comment out to watch it in real-time
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.linkedin.com/login")

    try:
        # Login
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

        # Go to feed page
        driver.get("https://www.linkedin.com/feed/")
        time.sleep(5)

        # Click 'Start a post'
        start_post = driver.find_element(By.XPATH, "//button[contains(., 'Start a post')]")
        start_post.click()
        time.sleep(3)

        # Locate the post editor
        editor = driver.find_element(By.CLASS_NAME, 'ql-editor')

        # Escape backticks in post text (for JS)
        escaped_text = post_text.replace("`", "\\`")

        # Inject content directly (supports emojis & formatting)
        driver.execute_script(f"arguments[0].innerHTML = `{escaped_text}`;", editor)
        time.sleep(2)

        if dry_run:
            print("✅ Dry run complete — content inserted (including emojis), but not posted.")
        else:
            post_button = driver.find_element(By.XPATH, "//button/span[text()='Post']/..")
            post_button.click()
            print("✅ Post submitted successfully.")

        time.sleep(5)

    except Exception as e:
        print(f"❌ Error during LinkedIn automation: {e}")

    finally:
        driver.quit()
