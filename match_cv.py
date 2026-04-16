import json
from groq import Groq
from config import GROQ_API_KEY, CV_MAIN_PATH, MATCH_THRESHOLD
def match_cv(job):
    client = Groq(api_key=GROQ_API_KEY)
    with open(CV_MAIN_PATH, 'r') as f:
        cv_content = f.read()
    prompt = f""" 
    ROLE: You are an expert HR recruiter specialized in DevOps and Cloud Engineering roles.

    CV:
    {cv_content}

    JOB OFFER:
    {job["description"]}

    TASK:
    Analyze the match between this CV and this job offer.

    RESPONSE FORMAT — Return ONLY this JSON, nothing else:
    {{
        "score": number between 0 and 100,
        "missing_keywords": ["keyword1", "keyword2"],
        "recommendation": "Good match or Poor match"
    }}

    No explanation. No text before or after. ONLY the JSON.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert HR recruiter specialized in DevOps and Cloud Engineering. Return ONLY valid JSON, no explanation, no text before or after."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=500
    )
    result_text = response.choices[0].message.content
    # Step 4 -- Parser JSON 
    try:
        result = json.loads(result_text.strip())
        if result["score"] >= MATCH_THRESHOLD:
            return result
        return None    #  if the score is too low
    except:
        return None    #  if the JSON is invalid
    