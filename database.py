import sqlite3 # import the SQlite module
from config import DB_PATH
from datetime import datetime


# Create Table function
def create_table ():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute ("""
        CREATE TABLE IF NOT EXISTS jobs (
        job_id TEXT PRIMARY KEY,
        title TEXT,
        company TEXT,
        description TEXT,
        apply_link TEXT,
        date_fetched TEXT,
        status TEXT DEFAULT 'new'    
        ) 
    """)
    conn.commit()
    conn.close()

# Function to check if job_id exists
def job_exists(job_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = "SELECT job_id FROM jobs WHERE job_id = ?"
    cursor.execute(query, (job_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None 


# INSERT Function
def insert_job(job):
    if job_exists(job["job_id"]):
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("""
        INSERT INTO jobs (job_id, title, company, description, apply_link, date_fetched, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (job["job_id"], job["title"], job["company"], job["description"], job["apply_link"], date, "new"))
    conn.commit()
    conn.close()

# Get NEW jobs
def get_new_jobs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs WHERE status = 'new'")
    results = cursor.fetchall()
    conn.close()
    return results



# UPDATE Function
def update_job_status(id_job, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE jobs SET status = ? WHERE job_id = ?", (status, id_job))
    conn.commit()
    conn.close()