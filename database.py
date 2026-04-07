import sqlite3 # import the SQlite module
from config import DB_PATH


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
def insert_job()


#
def get_new_jobs()


# UPDATE Function
def update_job_status()