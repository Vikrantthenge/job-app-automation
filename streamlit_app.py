import streamlit as st
from jsearch_scraper import fetch_jobs_jsearch
from pathlib import Path
import os

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Job Search Automation | Vikrant Thenge", page_icon="🔍", layout="centered")

# -------------------- SIDEBAR --------------------
st.sidebar.title("Vikrant Thenge")
st.sidebar.title("Connect with Me")
st.sidebar.markdown("[🔗 GitHub](https://github.com/vikrantthenge)")
st.sidebar.markdown("[💼 LinkedIn](https://www.linkedin.com/in/vthenge/)")
st.sidebar.markdown("---")
st.sidebar.info("Built with ❤️ using Streamlit")

# -------------------- TITLE --------------------
st.title("🔍 Job Search Automation Bot")
st.markdown("Search jobs across platforms using keywords and location. Powered by RapidAPI's JSearch.")

# -------------------- RESUME DOWNLOAD --------------------
st.markdown("### 📄 Download My Resume")
resume_path = Path("assets/Vikrant_Thenge_Resume.pdf")
if resume_path.exists():
    with open(resume_path, "rb") as file:
        resume_bytes = file.read()
        if st.download_button(
            label="📥 Download Resume",
            data=resume_bytes,
            file_name="Vikrant_Thenge_Resume.pdf",
            mime="application/pdf"
        ):
            st.success("✅ Resume downloaded successfully!")
            st.balloons()
else:
    st.error("Resume file not found. Please upload it to the assets folder.")

# -------------------- JOB SEARCH --------------------
st.markdown("---")
st.header("🔎 Search for Jobs")

keyword = st.text_input("Enter job title or keyword", "Data Analyst")
location = st.text_input("Enter location", "Mumbai")

api_key = "71a00e1f1emsh5f78d93a2205a33p114d26jsncc6534e3f6b3"  # Replace with your actual RapidAPI key

if st.button("Search Jobs"):
    if keyword and location:
        with st.spinner("Fetching jobs..."):
            jobs = fetch_jobs_jsearch(keyword, location, api_key)

        if jobs:
            st.success(f"Found {len(jobs)} jobs for '{keyword}' in '{location}'")
            for job in jobs:
                st.markdown("----")
                st.subheader(job.get("title", "No Title"))
                st.write(f"**Company:** {job.get('company_name', 'Unknown')}")
                st.write(f"**Location:** {job.get('location', 'Unknown')}")
                st.markdown(f"[📝 Apply Here]({job.get('job_apply_link', job.get('job_google_link', '#'))})", unsafe_allow_html=True)
        else:
            st.warning("No jobs found. Try different keywords or locations.")
    else:
        st.error("Please enter both keyword and location.")

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("© 2025 Vikrant Thenge. All rights reserved.")
