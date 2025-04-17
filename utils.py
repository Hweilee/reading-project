import requests
from bs4 import BeautifulSoup
import openai
import os
from dotenv import load_dotenv


#Load OpenAI API key from environment variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

 
def scrape_text(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    return " ".join(paragraphs)

def summarize_with_llm(text: str) -> str:
    #if I want to limit the output of summary, I can modify the prompt below
    prompt = f"""
You are an AI assistant. Summarize the following web content in a table with the format:
| Section | Summary | Key Points |
Limit the summary to the most important 3-5points only.
Only use the information directly from the webpage content. Do not answer or assume any information that is not present in the provided text.

Content:
{text}
                                                    """
    client = openai.OpenAI()
    
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    ) 
    return response.choices[0].message.content
