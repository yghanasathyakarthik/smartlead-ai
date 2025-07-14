import csv
import pandas as pd

def read_companies(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def write_results(leads, filename="scored_companies.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=leads[0].keys())
        writer.writeheader()
        writer.writerows(leads)


def write_excel(leads, filename="scored_companies.xlsx"):
    df = pd.DataFrame(leads)
    df.to_excel(filename, index=False)
