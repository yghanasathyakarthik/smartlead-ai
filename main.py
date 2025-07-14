from file_io import read_companies, write_results, write_excel

from search import get_company_info
from scorer import score_lead
from utils import retry_on_fail, label_score
from tqdm import tqdm

def main():
    companies = read_companies("companies.csv")
    results = []

    print("🚀 Scoring companies with Groq + live search...\n")

    for c in tqdm(companies):
        name = c["company"]

        summary = retry_on_fail(lambda: get_company_info(name)) or "No info found"
        score = retry_on_fail(lambda: score_lead(name, summary))
        label = label_score(score)

        c["summary"] = summary
        c["score"] = score
        c["label"] = label
        results.append(c)

    write_results(results)
    write_excel(results)
    print("\n✅ Done! See scored_companies.csv and scored_companies.xlsx")

if __name__ == "__main__":
    main()
