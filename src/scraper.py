import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def build_driver():
    headless = os.getenv("HEADLESS", "1") == "1"
    user_agent = os.getenv("USER_AGENT", "").strip()

    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1400,900")

    if user_agent:
        opts.add_argument(f"--user-agent={user_agent}")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)


def main():
    load_dotenv()
    start_url = os.getenv("START_URL", "https://example.com")

    driver = build_driver()
    try:
        driver.get(start_url)
        print("TITLE:", driver.title)
        print("URL:", driver.current_url)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
