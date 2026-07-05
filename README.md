# 📄 AI-Powered Resume Review Assistant (Multi-Agent System)

This project is an **AI-powered Resume Review Assistant** that leverages a **Multi-Agent Architecture** to analyze and improve resumes. It helps job seekers optimize their resumes for Applicant Tracking Systems (ATS) and specific job roles by coordinating specialized AI agents to handle formatting, grammar, skills matching, and content enhancement.

## 🚀 Features

- **PDF Resume Upload**: Easily upload your resume in PDF format (`pdfplumber`).
- **Target Role Matching**: Compare your resume directly against a specific job role and description.
- **Multi-Agent Workflow**: Utilizes specialized LLM personas (Agents) to process the resume step-by-step.
- **ATS Compatibility Score**: Analyzes formatting and structure to give a hypothetical ATS score.
- **Grammar & Spelling Check**: Detects awkward phrasing and suggests grammatical corrections.
- **Skill Gap Analysis & Certifications**: Identifies missing keywords and recommends highly relevant certification courses based on the target job.
- **Action-Oriented Improvements**: Suggests stronger bullet points with achievement-oriented metrics.
- **Interactive Chat Interface**: After the review is complete, chat with the "Manager Agent" to ask follow-up questions about your report or career.

## 🤖 Multi-Agent Architecture

The system orchestrates the following specialized agents behind the scenes:

1. **PDF Extraction Agent (Tool)**: Reads and extracts text from the uploaded PDF.
2. **ATS Analysis Agent**: Calculates ATS scores and identifies missing keywords.
3. **Grammar Agent**: Detects language errors and suggests corrections.
4. **Skills Matching Agent**: Compares the resume to the job description and recommends relevant certifications.
5. **Resume Improvement Agent**: Generates professional summaries and rewrites weak bullet points using strong action verbs.
6. **Report Generation Agent**: Synthesizes all outputs into a final, comprehensive Markdown report.
7. **Manager Agent**: Coordinates the final interactive chat interface to answer user follow-up queries.

## 🛠️ Technology Stack

- **Python**: Core programming language.
- **Streamlit**: For the interactive web-based UI.
- **OpenRouter API**: To access large language models (LLMs).
- **pdfplumber**: For robust PDF text extraction.
- **python-dotenv**: For environment variable management.

## ⚙️ Setup and Installation

### 1. Prerequisites
Ensure you have Python installed. You will also need an OpenRouter API key.

### 2. Clone/Download the Repository
Make sure you are in the project folder:
```bash
cd "Resume Review Agent"
```

### 3. Install Dependencies
Install all required libraries using `pip`:
```bash
pip install -r requirement.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory (if it doesn't already exist) and add your OpenRouter API key:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 5. Run the Application
Launch the Streamlit web application:
```bash
streamlit run app.py
```

The application will open in your default web browser. Upload a PDF resume, specify your target job role, and click **Start Review** to watch the agents work!
