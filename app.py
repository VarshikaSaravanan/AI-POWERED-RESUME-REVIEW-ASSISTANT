import streamlit as st
import os
import tempfile
from main import process_resume_workflow, chat_with_manager
from memory import load_memory

st.set_page_config(page_title="AI Resume Review Assistant", layout="wide")

st.title("📄 AI-Powered Resume Review Assistant")
st.write("Upload your resume and target job details to get a comprehensive review from our AI Agents.")

with st.sidebar:
    st.header("1. Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])
    
    st.header("2. Target Job")
    job_role = st.text_input("Target Job Role (e.g., Software Engineer)")
    job_description = st.text_area("Job Description (Optional)")
    
    start_review = st.button("Start Review", type="primary")

if 'report' not in st.session_state:
    st.session_state.report = None

if start_review and uploaded_file and job_role:
    with st.spinner("Agents are analyzing your resume... This might take a minute."):
        # Save uploaded file to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        
        try:
            report = process_resume_workflow(tmp_path, job_role, job_description)
            st.session_state.report = report
        except Exception as e:
            st.error(f"An error occurred: {e}")
        finally:
            os.remove(tmp_path)

if st.session_state.report:
    st.header("📊 Your Resume Review Report")
    st.markdown(st.session_state.report)
    
    st.divider()
    
    st.header("💬 Discuss with Manager Agent")
    st.write("Have questions about the report? Ask the manager!")
    
    # Initialize chat history in Streamlit based on memory
    memory = load_memory()
    for msg in memory:
        if msg["role"] in ["user", "assistant"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                
    prompt = st.chat_input("Ask a question about your resume...")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.spinner("Manager is thinking..."):
            response = chat_with_manager(prompt)
            with st.chat_message("assistant"):
                st.markdown(response)
                
elif start_review and not uploaded_file:
    st.warning("Please upload a resume to start.")
elif start_review and not job_role:
    st.warning("Please enter a target job role.")
