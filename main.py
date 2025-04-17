from utils import scrape_text, summarize_with_llm
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post("/summarize")
def summarize_url(req: URLRequest):
    try:
        scraped = scrape_text(req.url)
        if not scraped.strip():
            return {"error": "No meaningful text found on the page."}
        summarized = summarize_with_llm(scraped)
        return {"table": summarized}
    except Exception as e:
        return {"error": str(e)}