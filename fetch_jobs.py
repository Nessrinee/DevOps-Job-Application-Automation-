import requests
from config import ADZUNA_APP_ID, ADZUNA_APP_KEY, KEYWORDS, MAX_JOBS_PER_REQUEST
from database import insert_job, get_new_jobs

def fetch_jobs():
    # Define the Adzuna API endpoint for job search
    url = "https://api.adzuna.com/v1/api/jobs/nl/search/1"
    # Loop through all keywords to search different job categories
    for keyword in KEYWORDS:
        # Build request parameters for the API cal
        params = {
            "app_id": ADZUNA_APP_ID,
            "app_key": ADZUNA_APP_KEY,
            "what": keyword,
            "results_per_page": MAX_JOBS_PER_REQUEST,
        }
        # Send HTTP GET request to Adzuna API
        response = requests.get(url, params=params)
        if response.status_code == 200:
            jobs = response.json()["results"]
            # Loop through each job and structure the data
            for job in jobs:
                dictionnaire = {
                    "job_id": job["id"],
                    "title": job["title"],
                    "company": job["company"]["display_name"],
                    "description": job["description"],
                    "apply_link": job["redirect_url"]
                }
                insert_job(dictionnaire)
        else:
            print("Erreur:", response.status_code)
            continue 
    # Return only newly inserted jobs (not duplicates)    
    return get_new_jobs()