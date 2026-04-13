import requests
from config import ADZUNA_APP_ID, ADZUNA_APP_KEY, KEYWORDS, MAX_JOBS_PER_REQUEST
from database import insert_job, get_new_jobs

def fetch_jobs():
    url = "https://api.adzuna.com/v1/api/jobs/nl/search/1"
    
    for keyword in KEYWORDS:
        params = {
            "app_id": ADZUNA_APP_ID,
            "app_key": ADZUNA_APP_KEY,
            "what": keyword,
            "results_per_page": MAX_JOBS_PER_REQUEST,
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            jobs = response.json()["results"]
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
         
    return get_new_jobs()