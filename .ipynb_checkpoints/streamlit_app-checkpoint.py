import streamlit as st
from jsearch_scraper import fetch_jobs_jsearch

# ⚠️ Hardcoded API key — for local testing only
api_key = "71a00e1f1emsh5f78d93a2205a33p114d26jsncc6534e3f6b3"

# 🎯 App Title
st.title("🔍 Job Search Automation Bot")
st.markdown("Search jobs across platforms using keywords and location. Powered by RapidAPI's JSearch.")

# 🧠 Input Fields
keyword = st.text_input("Enter job title or keyword", "Data Analyst")
location = st.text_input("Enter location", "Mumbai")

# 🚀 Search Button
if st.button("Search Jobs"):
    if keyword and location:
        with st.spinner("Fetching jobs..."):
            jobs = fetch_jobs_jsearch(keyword, location, api_key)

        if jobs:
            st.success(f"Found {len(jobs)} jobs for '{keyword}' in '{location}'")
            for job in jobs:
                st.markdown("----")
                st.subheader(job["title"])
                st.write(f"**Company:** {job['company']}")
                st.write(f"**Location:** {job['location']}")
                st.markdown(f"[📝 Apply Here]({job['link']})", unsafe_allow_html=True)
        else:
            st.warning("No jobs found. Try different keywords or locations.")
    else:
        st.error("Please enter both keyword and location.")