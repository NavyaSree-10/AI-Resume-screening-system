# 🤖 AI Resume Screening System

> An AI-powered Resume Screening application that helps recruiters evaluate resumes by comparing them with job descriptions and generating a resume-job matching score.

---

## 📖 Overview

The **AI Resume Screening System** is a Python and Streamlit-based application designed to simplify the initial resume screening process.

The system extracts text from a candidate's resume, compares it with a given job description, and calculates a similarity score to help identify how closely the candidate's profile matches the job requirements.

---

## ✨ Features

- 📄 Upload resumes in PDF format
- 📝 Extract resume text automatically
- 💼 Compare resumes with job descriptions
- 📊 Generate a resume-job matching score
- 📈 Display the matching score clearly
- 🖥️ Simple and user-friendly Streamlit interface
- ⚡ Fast automated resume screening

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Application Development |
| Streamlit | Web Application Interface |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-learn | Text Similarity Calculation |
| PDFPlumber / PyPDF2 | PDF Text Extraction |

> **Note:** Keep only the PDF library that your actual `resume_parser.py` code uses.

---

## 📁 Project Structure

```text
AI-Resume-screening-system/
│
├── app.py
├── resume_parser.py
├── screening.py
├── requirements.txt
├── job_description.txt
├── resumes/
├── assets/
└── README.md
