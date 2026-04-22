# Each module represents a step in the automation workflow
from fetch_jobs import fetch_jobs          # Fetch jobs from API / database
from match_cv import match_cv              # Evaluate CV-job compatibility using LLM
from tailor_cv import tailor_cv            # Generate tailored CV (LaTeX)
from compile_cv import compile_cv          # Compile LaTeX CV into PDF
from database import update_job_status     # Update job processing status in DB


def main():

    # Fetch new jobs to process
    jobs = fetch_jobs()

    # Stop the pipeline if no jobs are found
    if not jobs:
        print("No jobs found. Stopping program")
        return

    #  Iterate through each job
    for job in jobs:

        # Convert raw job data (tuple) into a structured dictionary
        # This makes it easier to work with meaningful keys instead of indexes
        job_dict = {
            "job_id": job[0],
            "title": job[1],
            "company": job[2],
            "description": job[3],
            "apply_link": job[4]
        }

        # Log current job being processed
        print(f"Processing: {job_dict['title']} at {job_dict['company']}")

        #  Run AI-based CV matching to evaluate relevance
        match_result = match_cv(job_dict)

        #  If match score is too low, skip this job
        if match_result is None:
            print("Score too low — job skipped")

            # Update job status in database as "skipped"
            update_job_status(job_dict["job_id"], "skipped")
            continue
        tailor_cv(job_dict, match_result)

        compile_cv(job_dict)


        update_job_status(job_dict["job_id"], "applied")

        print(f"✅ CV generated for {job_dict['company']}")


# Entry point of the script
# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()