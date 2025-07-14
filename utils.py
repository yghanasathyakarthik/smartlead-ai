import re
import time
from random import uniform

def extract_score_from_response(text):
    match = re.search(r"score[:\s]*([0-9]{1,3})", text.lower())
    if match:
        return int(match.group(1))
    return None

def label_score(score):
    if score is None:
        return "❌ Error"
    if score >= 80:
        return "🔥 Hot"
    elif score >= 50:
        return "🟡 Warm"
    else:
        return "❄️ Cold"

def retry_on_fail(func, retries=3, delay=1.0):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"Retry {attempt+1}: {e}")
            time.sleep(delay + uniform(0.5, 1.5))
    return None
