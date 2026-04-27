from pathlib import Path

# API Keys 
#ANTHROPIC_API_KEY: str = ""
GROQ_API_KEY: str = ""

# Adzuna Credentials
ADZUNA_APP_ID: str = ""      #  app_id 
ADZUNA_APP_KEY: str = ""#  app_key

# Credentials LinkedIn
LINKEDIN_EMAIL: str = "email.com"
LINKEDINT_PASSWORD: str = "passw"


# Job Search Parameters 
KEYWORDS: list = [
    "DevOps Engineer",
    "Cloud DevOps Engineer",
    "Platform Engineer",
    "Site Reliability Engineer",
    "Kubernetes Engineer",
    "AWS DevOps Engineer",
    "DevSecOps Engineer",
    "CI/CD Engineer",
]

TARGET_COUNTRIES: list = [
    "Netherlands",
    "Germany",
    "France",
    "Belgium",
    "Spain",
    "Italy",
    "Portugal",
    "Austria",
    "Switzerland",
    "Denmark",
    "Sweden",
    "Norway",
    "Finland",
    "Poland",
    "Czech Republic",
    "Hungary",  
    "Greece",
    "Ireland",
    "Luxembourg",
    "Slovakia"
]
EMPLOYMENT_TYPE: str = "FULLTIME"
MAX_JOBS_PER_REQUEST: int = 10

# Matching 
MATCH_THRESHOLD: int = 80

# File Paths 
BASE_DIR: Path = Path(__file__).resolve().parent

CV_MAIN_PATH: Path = BASE_DIR / "cv" / "main.tex"
CV_TAILORED_PATH: Path = BASE_DIR / "cv" / "main_tailored_IA_version.tex"
OUTPUT_DIR: Path = BASE_DIR / "output"
DB_PATH: Path = BASE_DIR / "db" / "jobs.db"

