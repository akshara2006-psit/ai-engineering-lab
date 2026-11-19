# Day 05 – AI-Powered Resume Evaluator & Candidate Ranking System

## Overview

The **LLM Resume Evaluator** is an AI-powered application that analyzes job descriptions and candidate resumes using Large Language Models (LLMs).

It extracts structured information from job descriptions and resumes, evaluates how well each candidate matches the job requirements, and ranks candidates based on their match scores.

The project uses **Groq API, Pydantic, and Python** to build a structured resume-screening pipeline.

## Features

- **Job Description Analysis:** Extracts job role, required skills, preferred skills, minimum experience, educational requirements, and responsibilities.
- **Resume Parsing:** Extracts candidate information, skills, work experience, education, projects, and certifications.
- **Multiple File Support:** Reads resumes in PDF and DOCX formats.
- **Structured Data Extraction:** Uses Pydantic models to validate LLM-generated information.
- **Candidate Matching:** Compares candidate profiles against job requirements.
- **AI-Based Scoring:** Generates a match score and detailed evaluation.
- **Candidate Ranking:** Sorts candidates by their match scores and identifies the top and lowest-performing matches.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Groq API | LLM-powered analysis |
| Pydantic | Structured data validation |
| pypdf | PDF resume text extraction |
| python-docx | DOCX resume extraction |
| JSON | Structured LLM responses |
| python-dotenv | Environment variable management |

## Project Workflow

1. **Job Description Input:** Provide the job description.
2. **Job Description Parsing:** Use the LLM to extract structured job requirements.
3. **Resume Collection:** Read multiple PDF and DOCX resumes.
4. **Resume Parsing:** Extract candidate details using the LLM.
5. **Data Validation:** Validate extracted information using Pydantic models.
6. **Resume Evaluation:** Compare each candidate's profile with the job description.
7. **Candidate Scoring:** Generate a match percentage and evaluation details.
8. **Candidate Ranking:** Sort candidates and display the top matches.

## Installation and Setup

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install groq pydantic python-dotenv pypdf python-docx
```

### 3. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Keep your API key private. Never upload your `.env` file to GitHub.

### 4. Add resumes

Place candidate resumes in the `resumes/` folder. Supported formats:

- PDF (`.pdf`)
- Word documents (`.docx`)

### 5. Run the project

```bash
python resume_parser.py
```

## Candidate Evaluation Output

For every candidate, the system generates:

- Candidate name
- Matching skills
- Missing skills
- Experience requirement evaluation
- Educational qualification
- Relevant projects
- Overall match score
- Final evaluation verdict

Candidates are sorted according to their match scores to identify the strongest matches.

## Learning Outcomes

Through this project, I explored:

- Integrating Large Language Models into Python applications.
- Using Groq API for LLM-based information extraction.
- Designing structured Pydantic models.
- Handling JSON responses from LLMs.
- Extracting text from PDF and DOCX documents.
- Building a multi-document processing pipeline.
- Evaluating and ranking candidates using AI-generated insights.

## Future Improvements

- Build a web-based interface for recruiters.
- Add more detailed skill-matching algorithms.
- Improve scoring consistency and evaluation reliability.
- Support additional resume formats.
- Export candidate rankings to CSV or Excel.
- Add explainable evaluation reports.

---

**Day 05 | AI Engineering Lab**

Building practical AI applications using Python, LLMs, and structured data validation.