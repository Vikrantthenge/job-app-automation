import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="Job Application Automation", page_icon="🧠", layout="centered")

# --- Branding Header ---
logo = Image.open("your_logo.png")  # Replace with your logo file
st.image(logo, width=120)
st.title("Job Application Automation Bot")
st.markdown("#### Created by [Vikrant Thenge](https://github.com/vikrantthenge)")

# --- Intro Section ---
st.markdown("""
Welcome to my end-to-end job application automation tool.  
This app streamlines your job search using **Python**, **Streamlit**, and **real-time scraping**.

🔍 **Features:**
- Search jobs across platforms (LinkedIn, Naukri, Indeed)
- Upload your resume and auto-match keywords
- Track applications and recruiter outreach
- Designed for recruiters to explore automation potential

📁 **Tech Stack:** Python · Streamlit · BeautifulSoup · GitHub · Resume Parsing · UI/UX Polish
""")

# --- Resume Download Button ---
with open("Vikrant_Resume.pdf", "rb") as file:
    btn = st.download_button(
        label="📄 Download My Resume",
        data=file,
        file_name="Vikrant_Resume.pdf",
        mime="application/pdf"
    )

# --- GitHub Link ---
st.markdown("[🔗 View Full Project on GitHub](https://github.com/vikrantthenge/job-app-automation)")

# --- App Functionality ---
st.markdown("---")
st.subheader("Try It Yourself 👇")
st.markdown("Use the sidebar to start your job search, upload your resume, and explore automation.")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ by Vikrant · FAA Dispatcher turned Data Engineer · Always optimizing.")
