# LinkedIn Profile Intelligence Analyzer

Streamlit + LangChain + Gemini MVP for analyzing user-provided LinkedIn profile text or PDF resumes.

## Data access
This MVP does not directly scrape LinkedIn. Use user-provided data or an authorized API/data source. Do not bypass authentication, CAPTCHA, rate limits, robots.txt, or anti-bot controls.

## Windows
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Copy `.env.example` to `.env`, add `GOOGLE_API_KEY`, then:
```powershell
streamlit run app.py
```

## Next phases
LangSmith tracing/evaluation, profile comparison, job-description RAG, Chroma, LangGraph, and authorized data-source integration.
