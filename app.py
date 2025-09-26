import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit UI
st.set_page_config(page_title="AI Summarizer", page_icon="✍️", layout="centered")
st.title("📄 AI Summarizer App")
st.write("Paste any long article, blog, or text and get a short summary instantly.")

# Input box
user_input = st.text_area("✏️ Paste your text here:", height=200)

# Summary button
if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Generating summary..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes long texts clearly and concisely."},
                    {"role": "user", "content": f"Summarize this text:\n\n{user_input}"}
                ],
                temperature=0.5
            )
            summary = response.choices[0].message.content
            st.success("✅ Summary Generated:")
            st.write(summary)
    else:
        st.warning("⚠️ Please paste some text before summarizing!")
