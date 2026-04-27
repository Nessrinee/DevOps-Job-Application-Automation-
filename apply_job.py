from pathlib import Path
from config import LINKEDIN_EMAIL , LINKEDINT_PASSWORD
from playwright.sync_api import sync_playwright
import random
import time

def random_delay(min_sec=1, max_sec=3):
    # Simulate human delay
    time.sleep(random.uniform(min_sec, max_sec))
    
    
def apply_job(job, pdf_path):
    if AUTO_APPLY:
        apply_auto(job, pdf_path)
    else:
        apply_manual(job, pdf_path)

def apply_auto(job, pdf_path):
    # Start Playwright context
    with sync_playwright() as p:
        
        # Launch Chromium browser in visible mode (headless=False)
        browser = p.chromium.launch(headless=False)

        # Create a new browser page (tab)
        page = browser.new_page()

        # Navigate to LinkedIn homepage
        page.goto("https://www.linkedin.com/login")
        
        # fill LINKEDIN_EMAIL 
        page.fill("input[name='session_key']", LINKEDIN_EMAIL)
        random_delay()
        
        # fill LINKEDINT_PASSWORD 
        page.fill("input[name='session_passwd']", LINKEDINT_PASSWORD)
        random_delay()
        # Click login
        page.click("button=[type='submit']")
        random_delay(2,4)
        # wait for homepage (feed)
        page.wait_for_selector("input[placeholder='Search']")

        # Take a screenshot of the current page
        page.screenshot(path="screenshot.png")
        # Debug Only
        print(page.title())

        # Close the browser after actions are done
        browser.close()
        
if __name__ == "__main__":
    # Call the function
    apply_job({}, None)
        
        
    