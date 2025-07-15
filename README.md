# 🔍 SmartLead AI – AI-Powered Lead Scoring Tool using Groq & SerpAPI

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Groq API](https://img.shields.io/badge/Groq-LLM-green)
![SerpAPI](https://img.shields.io/badge/SerpAPI-Integrated-yellow)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)
![Internship Ready](https://img.shields.io/badge/Built%20For-Internship%20Submission-blueviolet)
![Excel Output](images/excel.png)

SmartLead AI is an AI-powered lead scoring tool that uses live web data and Groq's lightning-fast LLM (LLaMA 3 70B) to analyze and score companies in real time.  
It intelligently evaluates companies based on online search data, using both custom heuristics and large language models to predict how promising each lead is.

---

## 🚀 Project Features

- 🔎 **Live Company Info Search** – Uses [SerpAPI](https://serpapi.com/) to fetch fresh Google search results for each company.
- 🧠 **AI Scoring Engine** – Powered by [Groq's LLaMA 3 70B model](https://console.groq.com/) for ultra-fast, intelligent evaluation.
- 📝 **Custom Prompts** – Each company is scored using a context-rich prompt sent to the LLM.
- 📊 **Outputs to Excel & CSV** – Clean and ready for client/team usage.
- 🔐 **Secure API Keys** – All sensitive data is stored in a `.env` file.

---

## 📂 Project Structure

smartlead-ai/
├── main.py                # Entry point – loops through companies, scores them
├── scorer.py              # Handles prompt creation and scoring with Groq
├── search.py              # Performs Google search using SerpAPI
├── config.py              # Loads Groq and SerpAPI keys from .env
├── file_io.py             # Handles reading/writing CSV and Excel files
├── utils.py               # Helpers for formatting, cleaning, parsing scores
├── requirements.txt       # Dependencies
├── companies.csv          # Input file of company names to score
├── README.md              # You're reading it!
└── images/excel.png       # Sample output preview
