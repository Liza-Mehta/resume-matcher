import streamlit as st
from utils.text_extract import extract_text_from_file
from utils.matcher import calculate_similarity
import pandas as pd

# Configure Streamlit page
st.set_page_config(page_title="AI Resume Matcher", layout="wide")
st.title("📄 AI Resume Matcher")
st.write("Upload a job description and resumes to see the best matches!")

# File uploaders
col1, col2 = st.columns(2)
with col1:
    jd_file = st.file_uploader("Job Description (PDF or DOCX)", type=["pdf", "docx"])
with col2:
    resume_files = st.file_uploader("Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

# Process files when uploaded
if jd_file and resume_files:
    jd_text = extract_text_from_file(jd_file)
    
    results = []
    for resume_file in resume_files:
        resume_text = extract_text_from_file(resume_file)
        score = calculate_similarity(jd_text, resume_text)
        results.append({"Filename": resume_file.name, "Match Score": score})
    
    # Display results as a sorted table
    df = pd.DataFrame(results).sort_values("Match Score", ascending=False)
    st.subheader("Results (Best Matches First)")
    st.dataframe(df.style.background_gradient(cmap="Blues"))