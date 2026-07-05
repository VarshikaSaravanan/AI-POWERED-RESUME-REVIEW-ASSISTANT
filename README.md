# AI-Powered Resume Review Assistant (Multi-Agent System)
<img width="1918" height="635" alt="image" src="https://github.com/user-attachments/assets/8e2ff385-96a2-4b26-90b7-f8b515cd30b2" />
<img width="1918" height="635" alt="image" src="https://github.com/user-attachments/assets/7344dec9-1a1f-438a-bbdd-efcd81c26d54" />
<img width="1912" height="852" alt="image" src="https://github.com/user-attachments/assets/6164c87c-e374-40b1-a9e1-550229bccfee" />
<img width="1882" height="552" alt="image" src="https://github.com/user-attachments/assets/2daff396-0138-45a2-9689-f81d17567056" />
<img width="1896" height="645" alt="image" src="https://github.com/user-attachments/assets/6e373500-867f-409c-89ff-1c3408d3f4dd" />
<img width="1582" height="143" alt="image" src="https://github.com/user-attachments/assets/969d053b-4e33-4db4-9c17-198a173b6c82" />
<img width="1585" height="172" alt="image" src="https://github.com/user-attachments/assets/5b3d304b-9bfd-429d-836f-7bbe82083840" />
<img width="1568" height="611" alt="image" src="https://github.com/user-attachments/assets/26898443-477e-4e08-ad83-0f0c7768fe5a" />
<img width="1572" height="187" alt="image" src="https://github.com/user-attachments/assets/cede5726-a75d-4b5d-9c11-3cff46a133bb" />
<img width="1587" height="165" alt="image" src="https://github.com/user-attachments/assets/0a8b849c-d239-45e7-a0c1-84a51ae0bf41" />
<img width="1562" height="677" alt="image" src="https://github.com/user-attachments/assets/a5376cf5-dcda-4133-b437-2bd39f2c19ed" />
<img width="1571" height="605" alt="image" src="https://github.com/user-attachments/assets/962b3854-0e33-4886-a3df-0a663c3960ec" />

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
