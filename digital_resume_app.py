from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Aviel Derhy"
PAGE_ICON = ":wave:"
NAME = "Aviel Derhy"
DESCRIPTION = "Machine Learning Engineer & AI Infrastructure"
EMAIL = "avielderhy@email.com"
PHONE = "0543330068"
LINKEDIN = "https://www.linkedin.com/in/aviel-derhy-44041a1b0/"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📱", PHONE)
    st.write(f"🔗 [linkedin]({LINKEDIN})")


with col2:
    st.image(profile_pic, width=300)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 5 Years expereince with Python
- ✔️ Strong hands on experience with K8s and MLOps tools
- ✔️ BSc in Computer Engineering - Bar Ilan University
- ✔️ DevOps Certification - Bynet
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Machine Learning Engineer | Walmart**")
st.write("01/2023 - Present")
st.write(
    """
- ► Responsible for the main core of the product
- ► Optimazing and integrating the AI models into the server
- ► Develop and maintain the infrastructure of the product
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Software Engineer | Marvell Technologies**")
st.write("08/2021 - 01/2023")
st.write(
    """
- ► Develop and maintain software that verify the usage of hardware APIs
- ► Created automatic tests to verify the hardware's quality
"""
)


# --- JOB 3
st.write('\n')
st.write("🚧", "**Python Developer | IDF - Intelligence Force 9900**")
st.write("10/2014 - 05/2017")
st.write(
    """
- ► Integrated the AI models into the main flow of the product
- ► Developed tools to the manual visual analysts
"""
)

# --- STUDIES ---
st.write('\n')
st.subheader("Studies")
st.write("---")

# --- Degree
st.write('\n')
st.write("🚧", "**Computer Engineer Student | Bar Ilan University**")
st.write("10/2018 - 06/2022")
st.write(
    """
- ► Specialized in Software development as well as Networks and Computation
- ► Graduated with honors (GPA: 90.2)
"""
)

# --- Devops Course
st.write('\n')
st.write("🚧", "**DevOps course | Bynet - 8200 program**")
st.write("07/2022 - 11/2022")
st.write(
    """
- ► Write pipelines with Jenkins, deploy to AWS
- ► Working with Docker and K8s
- ► Finished the course with GPA of 99.7 (8 assignments + final project)
"""
)
