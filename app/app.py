import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="RAG AI Assistant", page_icon="🤖")

st.title("🤖 RAG AI Assistant")
st.write("Upload a PDF and this app will read the text from it.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    pdf = PdfReader(uploaded_file)
    full_text = ""

    for page in pdf.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    st.success("PDF uploaded successfully!")
    st.subheader("Extracted Text")
    st.text_area("PDF Content", full_text, height=300)
