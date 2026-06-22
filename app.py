
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-flash-2.5")
# model = genai.GenerativeModel("gemini-pro-1.5")
model = genai.GenerativeModel("gemini-2.5-flash")

def my_output(query) -> str:
    response = model.generate_content(query)
    return response.text

### UI Development using Streamlit

st.set_page_config(page_title="My Streamlit App")
st.header("My Streamlit App")
input = st.text_input("Input " , key = "input")
submit = st.button("Ask Your Query")

if submit:
    response = my_output(input)
    st.subheader("Your Answer is ......")
    st.write(response)
