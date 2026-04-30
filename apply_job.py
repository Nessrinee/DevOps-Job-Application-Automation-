from pathlib import Path
from playwright.sync_api import sync_playwright
from config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD, AUTO_APPLY
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

def apply_manual(job, pdf_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to job page directly
        page.goto(job["apply_link"])
        random_delay()

        # Show instructions in terminal
        print(f" Job  : {job['title']} at {job['company']}")
        print(f" PDF  : {pdf_path}")
        print(f" URL  : {job['apply_link']}")
        print("✅ Tape 'done' quand tu as postulé")

        # Wait for human to finish
        input()
        browser.close()
        return True

def apply_auto(job, pdf_path):
    # Start Playwright context
    with sync_playwright() as p:
        # Launch Chromium browser in visible mode (headless=False)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to LinkedIn homepage
        page.goto("https://www.linkedin.com/login")
        random_delay()

        # Step 1: fill LINKEDIN_EMAIL 
        page.fill("input[name='session_key']", LINKEDIN_EMAIL)
        random_delay()
        page.click("button[type='submit']")
        random_delay(2, 3)

        # Step: fill LINKEDINT_PASSWORD 
        page.wait_for_selector("input[name='session_password']")
        page.fill("input[name='session_password']", LINKEDIN_PASSWORD)
        random_delay()
        page.click("button[type='submit']")
        random_delay(2, 4)
    

        # Wait for homepage
        page.wait_for_selector("input[placeholder='Search']")
        
        # Go to job page
        page.goto(job["apply_link"])
        random_delay()

        try:
             # Check if the Easy Apply button is visible on the page
            if page.is_visible("button.jobs-apply-button"):
                page.click("button.jobs-apply-button")
                random_delay()

                page.wait_for_selector("input[type='file']")
                page.set_input_files("input[type='file']", str(pdf_path))
                random_delay()
                
                # Continue clicking "Next step" while the button exists
                while page.is_visible("button[aria-label='Continue to next step']"):
                    page.click("button[aria-label='Continue to next step']")
                    random_delay()

                page.click("button[aria-label='Submit application']")
                random_delay()
                print(f"Application submitted for {job['company']}")
                browser.close()
                return True
            # If Easy Apply is not available, switch to manual application mode
            else:
                browser.close()
                apply_manual(job, pdf_path)
                return False
        # If LinkedIn blocks automation or an error occurs, fallback to manual mode
        except:
            print("LinkedIn blocked — switching to manual mode")
            browser.close()
            apply_manual(job, pdf_path)
            return False

if __name__ == "__main__":
    apply_job({"apply_link": "https://linkedin.com", "title": "DevOps", "company": "Test"}, None)