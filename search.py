import requests
from config import SERPAPI_KEY

def get_company_info(company_name):
    params = {
        "engine": "google",
        "q": f"{company_name} company",
        "api_key": SERPAPI_KEY
    }

    try:
        res = requests.get("https://serpapi.com/search", params=params)
        data = res.json()

        if "knowledge_graph" in data:
            return data["knowledge_graph"].get("description", "")

        if "organic_results" in data and data["organic_results"]:
            return data["organic_results"][0].get("snippet", "")

        return ""
    except Exception as e:
        print(f"Search failed for {company_name}: {e}")
        return ""
