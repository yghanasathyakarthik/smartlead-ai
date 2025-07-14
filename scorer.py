import requests
from config import GROQ_API_KEY, GROQ_MODEL
from utils import extract_score_from_response

def score_lead(company_name, summary):
    prompt = (
        "You're an AI business analyst. Score this company lead from 0 to 100 based on value.\n"
        f"Company: {company_name}\n"
        f"Summary: {summary}\n"
        "Respond with just: Score: <number>"
    )

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }

    r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
    data = r.json()

    try:
        return extract_score_from_response(data["choices"][0]["message"]["content"])
    except:
        print(f"Groq scoring failed for {company_name}: {data}")
        return None
