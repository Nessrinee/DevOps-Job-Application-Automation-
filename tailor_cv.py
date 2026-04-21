import json
from groq import Groq
from config import GROQ_API_KEY, CV_MAIN_PATH, CV_TAILORED_PATH

def tailor_cv(job, match_result):
    # Initialize Groq client using API key
    client = Groq(api_key=GROQ_API_KEY)
    # Load the original CV (LaTeX format)
    with open(CV_MAIN_PATH, 'r') as f:
        cv_content = f.read()
        # The goal is to integrate missing keywords into a LaTeX CV without breaking structure
    prompt = """
    ROLE: You are an expert LaTeX CV writer specialized in DevOps engineering roles.

    CV:
    """ + cv_content + """

    JOB TITLE: """ + job["title"] + """

    MISSING KEYWORDS TO ADD: """ + str(match_result["missing_keywords"]) + """

    TASK:
    - Naturally integrate the missing keywords into the CV
    - Modify ONLY the OBJECTIVE and TECHNICAL SKILLS sections
    - Do NOT break LaTeX syntax
    - Do NOT invent fake experiences
    - Keep the same format and structure

    RESPONSE FORMAT:
    Return ONLY the complete modified .tex file.
    No explanation. No backticks. No text before or after.
    """
    # Call Groq LLM to generate the tailored CV
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content":"You are an expert LaTeX CV writer specialized in DevOps engineering roles"},
            {"role": "user", "content": prompt} 
        ],
        temperature=0,
        max_tokens=4000
    )
    # Extract raw response from the LLM
    result_text = response.choices[0].message.content
    cleaned = result_text.replace("```latex", "").replace("```", "").strip()
    with open (CV_TAILORED_PATH, 'w') as f:
        f.write(cleaned)
    return CV_TAILORED_PATH
