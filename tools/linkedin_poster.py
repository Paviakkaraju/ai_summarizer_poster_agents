from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
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
def linkedin(post_text, profile_path, profile_name, dry_run=True):
    """
    Opens LinkedIn in your real Chrome profile and creates a post using Selenium.

    Args:
        post_text (str): The content to post (supports emojis and formatting).
        dry_run (bool): If True, inserts content but does not click 'Post'.
    """

    # === 🛠 Customize Chrome setup ===
    PROFILE_NAME = profile_name
    PROFILE_PATH = profile_path

    options = Options()
    options.add_argument(f"--user-data-dir={PROFILE_PATH}")
    options.add_argument(f"--profile-directory={PROFILE_NAME}")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("detach", True)

    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 15)

    try:
        print("🌐 Opening LinkedIn...")
        driver.get("https://www.linkedin.com/feed/")

        # Wait for the "Start a post" button and click it
        start_post = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Start a post')]")))
        start_post.click()
        print("📝 Opening post editor...")

        # Wait for editor and insert content
        editor = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ql-editor")))
        escaped_text = post_text.replace("`", "\\`")
        driver.execute_script(f"arguments[0].innerHTML = `{escaped_text}`;", editor)

        if dry_run:
            print("✅ Dry run complete — post content inserted, not submitted.")
        else:
            post_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Post']/..")))
            post_button.click()
            print("✅ Post submitted successfully.")

        time.sleep(3)

    except Exception as e:
        print(f"❌ Error during LinkedIn automation: {e}")

    finally:
        driver.quit()
        print("🧹 Browser closed.")