import streamlit as st
from pathlib import Path

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Vikrant Thenge | Job Automation App", page_icon="📄", layout="centered")

# -------------------- SIDEBAR --------------------
st.sidebar.title("Connect with Me")
st.sidebar.markdown("[🔗 GitHub](https://github.com/vikrantthenge)")
st.sidebar.markdown("[💼 LinkedIn](https://www.linkedin.com/in/vikrantthenge)")
st.sidebar.markdown("---")
st.sidebar.info("Built with ❤️ using Streamlit")

# -------------------- MAIN CONTENT --------------------
st.title("📄 Download My Resume")
st.write("Hi, I'm **Vikrant Thenge** — a Data Analyst & Cloud Engineer blending automation, analytics, and storytelling to drive business impact.")

st.markdown("Click the button below to download my resume:")

# -------------------- RESUME DOWNLOAD --------------------
resume_path = Path("assets/resume.pdf")
with open(resume_path, "rb") as file:
    resume_bytes = file.read()

st.download_button(
    label="📥 Download Resume",
    data=resume_bytes,
    file_name="Vikrant_Thenge_Resume.pdf",
    mime="application/pdf"
)

# -------------------- BALLOONS --------------------
st.success("Thanks for downloading! 🎉")
st.balloons()

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("© 2025 Vikrant Thenge. All rights reserved.")
