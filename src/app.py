import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("📄 BERT-Powered Resume Screener")
st.subheader("Compare Resumes against Job Descriptions using NLP")

# User Input
jd_input = st.text_area("Paste the Job Description here:", height=200)
uploaded_files = st.file_uploader("Upload Resumes (PDF)", accept_multiple_files=True)

if st.button("Analyze Resumes"):
    if not jd_input or not uploaded_files:
        st.error("Please provide both a JD and at least one resume.")
    else:
        for uploaded_file in uploaded_files:
            # Connect to our FastAPI backend
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
            params = {"job_description": jd_input}
            
            with st.spinner(f"Analyzing {uploaded_file.name}..."):
                response = requests.post("http://localhost:8000/score", params=params, files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    score = float(result['match_score'].replace('%', ''))
                    
                    # UI logic for color-coding results
                    if score > 80:
                        st.success(f"**{uploaded_file.name}**: {score}% Match (Strong Candidate)")
                    elif score > 50:
                        st.warning(f"**{uploaded_file.name}**: {score}% Match (Potential Fit)")
                    else:
                        st.error(f"**{uploaded_file.name}**: {score}% Match (Low Correlation)")