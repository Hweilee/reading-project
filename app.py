from utils import scrape_text, summarize_with_llm
import streamlit as st

st.title("Webpage Summarizer")
url = st.text_input("Enter a web page URL")
if st.button("Summarize"):
    if url:
        with st.spinner("Scraping and summarizing..."):
            text = scrape_text(url)
            summary = summarize_with_llm(text)

        st.markdown("### Summary Output")
        st.markdown(summary)
    else:
        st.warning("Please enter a valid URL.")