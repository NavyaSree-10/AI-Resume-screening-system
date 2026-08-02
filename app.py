import streamlit as st
import pdfplumber
from screening import analyze_skills, calculate_match_score


# Page settings
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="centered"
)


# Title
st.title("📄 AI Resume Screening System")
st.caption("AI-powered resume analysis and job matching")

st.info(
    "Upload a resume, compare it with a job description, "
    "and view the match score, recommendation, and skill analysis."
)


# Upload resume
uploaded_file = st.file_uploader(
    "📤 Upload Resume",
    type=["pdf", "txt"]
)


# Job description
job_description = st.text_area(
    "💼 Enter the Job Description:",
    value="""We are looking for a Python Developer with skills in Python, SQL,
Machine Learning, Pandas, NumPy and Data Analysis.
The candidate should have experience working on Python programming
and data analysis projects.""",
    height=200
)


# If resume is uploaded
if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    text = ""

    # Read PDF
    if uploaded_file.type == "application/pdf":

        try:
            with pdfplumber.open(uploaded_file) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

        except Exception as e:
            st.error(f"Error reading PDF: {e}")

    # Read TXT
    else:

        text = uploaded_file.read().decode("utf-8")


    # If text was extracted
    if text:

        # Resume content
        st.subheader("📄 Resume Content")

        st.text_area(
            "Extracted Text",
            text,
            height=300
        )


        # Check score
        if st.button("🔍 Check Match Score"):

            if job_description.strip():

                # Calculate match score
                score = calculate_match_score(
                    text,
                    job_description
                )


                # Analyze skills
                matched_skills, missing_skills = analyze_skills(
                    text,
                    job_description
                )


                # Match score
                st.subheader("📊 Resume Match Score")

                st.success(
                    f"Your resume matches the job description by {score}%"
                )


                # Progress bar
                st.progress(int(score))

                st.write(
                    f"Match Score: {score}%"
                )


                # Dashboard
                st.subheader("📊 Match Score Dashboard")

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Resume Match Score",
                        f"{score}%"
                    )

                with col2:

                    if score >= 70:

                        st.metric(
                            "Status",
                            "Strong Match"
                        )

                    elif score >= 50:

                        st.metric(
                            "Status",
                            "Moderate Match"
                        )

                    else:

                        st.metric(
                            "Status",
                            "Low Match"
                        )


                # Recommendation
                st.subheader("🎯 Recommendation")

                if score >= 70:

                    st.success(
                        "Strong Match - Recommended"
                    )

                elif score >= 50:

                    st.warning(
                        "Moderate Match - Consider for Review"
                    )

                else:

                    st.error(
                        "Low Match - Further Review Required"
                    )


                # Skill Analysis
                st.subheader("🧠 Skill Analysis")


                # Matched skills
                if matched_skills:

                    st.write("✅ Matched Skills:")

                    st.write(
                        ", ".join(matched_skills)
                    )

                else:

                    st.write(
                        "❌ No matched skills found."
                    )


                # Missing skills
                if missing_skills:

                    st.write("⚠️ Missing Skills:")

                    st.write(
                        ", ".join(missing_skills)
                    )

                else:

                    st.write(
                        "🎉 No missing skills!"
                    )


                # Download result
                result = f"""
AI RESUME SCREENING SYSTEM
==========================

Resume Match Score: {score}%

Recommendation:
{"Strong Match - Recommended"
 if score >= 70
 else "Moderate Match - Consider for Review"
 if score >= 50
 else "Low Match - Further Review Required"}

Matched Skills:
{", ".join(matched_skills) if matched_skills else "None"}

Missing Skills:
{", ".join(missing_skills) if missing_skills else "None"}
"""


                # Download button
                st.subheader("📥 Download Result")

                st.download_button(
                    label="Download Screening Result",
                    data=result,
                    file_name="resume_screening_result.txt",
                    mime="text/plain"
                )


            else:

                st.warning(
                    "⚠️ Please enter a job description."
                )


    else:

        st.warning(
            "⚠️ No text found in the uploaded file."
        )