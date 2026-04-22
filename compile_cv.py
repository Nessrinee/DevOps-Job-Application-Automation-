import subprocess
from datetime import datetime
from pathlib import Path
from config import CV_TAILORED_PATH, OUTPUT_DIR

def compile_cv(job):
    company = job["company"].replace(" ", "_")
    date = datetime.now().strftime("%Y-%m-%d")
    pdf_name = "CV_Nesrine_" + company + "_" + date + ".pdf"

    command = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-output-directory=" + str(OUTPUT_DIR),
        "main_tailored_IA_version.tex",
        str(CV_TAILORED_PATH)
    ]

    try:
        subprocess.run(command, check=True, cwd=str(CV_TAILORED_PATH.parent))
    except Exception as e:
        print("Erreur compilation:", e)
        return None

    old_path = OUTPUT_DIR / "main_tailored_IA_version.pdf"
    new_path = OUTPUT_DIR / pdf_name
    old_path.rename(new_path)

    return new_path