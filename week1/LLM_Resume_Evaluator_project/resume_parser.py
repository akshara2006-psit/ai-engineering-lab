import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel,Field
load_dotenv()
import time
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API KEY GYABBBB HAI!!!!!!")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"
job_description='''
As a Software Engineering Intern,You will get to be part of the one or more aspects of the engineering lifecycle of tools and/ or features that enable our solutions to reach millions of end users and enterprises who use our important applications and services every day to run their business. We also look to you to help deliver high quality software through automated testing, and own your service in production with real-time monitoring tools and frameworks.
 

Responsibilities
Operate within a dynamic work environment to generate software of exceptional quality
Collaborate with the development team to design, develop, test and deploy software products
Engage in developing solutions that seamlessly integrate into distributed systems, using innovative technology at an unprecedented scale and speed.
Develop optimized code that may be included as part of our next software release
Contribute to our suite of automated tests and testing infrastructure
Contribute to tools and solutions to support and monitor our various cloud services 
Eligibility Criteria
Enrolled in sophomore year or higher at a college/university or any year at a graduate school
Working towards a B.E/ B.Tech in Computer Science, Information Technology and Circuit Branch graduating in 2028
Required Skills
Academic or professional/internship
Ability to quickly learn new technologies
Strong analytical and problem-solving skills
Ability to thrive in a fast-paced environment
Be a self-starter and possess strong sense of self-motivation
Excellent in effectively communicating technical challenges and proposing solutions
Skilled in navigating through ambiguous or undefined problems, coupled with the ability to think abstractly
Desired Skills
Experience with programming languages such as Java, C++ or Python
Knowledge of web development technologies (HTML, CSS, JavaScript) and frameworks (React, Angular, or Vue.js) is a plus
Coursework in SQL and relational database conceptsility to think abstractly
Strong in Computer Science fundamentals, including object-oriented design, data structures, algorithm development, problem-solving, and complexity analysis


'''


class JobD(BaseModel):
    role:str
    required_skills:list[str]
    preferred_skills:list[str]
    minimum_experience:float |None
    educational_requirement:list[str]
    responsibilities:list[str]

jobd_schema=JobD.model_json_schema()
system_prompt=f"""
Your are an expert HR assistant.Your job is to analyse job description and extract structured information from them.

Return valid JSON matching this schema 
{jobd_schema}
IMPORTANT:
Do not return the schema itself.
Do not return fields like "properties", "title" or "type".


Do not rename any field.
Do not replace:
- role with job_title
- educational_requirement with education_requirements
Fill the schema with actual information extracted from the job description

If minimum experience is not mentioned, return null
If information fro list is missing, return an empty list
Do not invent information

"""
user_prompt=f"""
Analyze the following job description {job_description}
"""

message_system={
    "role":"system",
    "content":system_prompt
}
message_user={
    "role":"user",
    "content":user_prompt
}

response_format={
    "type":"json_object"
}
messages=[message_system,message_user]
response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)
answer=response.choices[0].message.content


import json
raw_json=answer
data_file=json.loads(raw_json)
job=JobD(**data_file)
print(job.minimum_experience)
print(job.educational_requirement)


# ==============================
# 1. PYDANTIC MODELS
# ==============================

class MatchResult(BaseModel):
    score: float = Field(ge=0, le=100)
    details: dict[str, str]


class Experience(BaseModel):
    company: str | None = None
    role: str | None = None
    duration: str | None = None
    description: str | None = None
    skills_used: list[str] = Field(default_factory=list)


class Resume(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None

    total_experience_years: float | None = None

    skills: list[str] = Field(default_factory=list)
    experiences: list[Experience] = Field(default_factory=list)
    education: list[str] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)


resume_schema = Resume.model_json_schema()


# ==============================
# 2. RESUME PARSING
# ==============================

def parse_resume(resume_text):

    system_prompt = f"""
    You are an expert resume parser.

    Extract information from the resume based on its meaning,
    not only exact section headings.

    Return ONLY valid JSON matching this schema:

    {resume_schema}

    Rules:
    1. Do not invent information.
    2. Missing values should be null.
    3. Missing lists should be empty.
    4. Include internships inside experiences.
    5. Extract skills from the entire resume.
    """

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"Parse this resume:\n{resume_text}"
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        response_format={"type": "json_object"},
        temperature=0.2
    )

    raw_output = response.choices[0].message.content

    data = json.loads(raw_output)

    resume = Resume.model_validate(data)

    return resume


# ==============================
# 3. JOB AND RESUME MATCHING
# ==============================

def final_score(job, resume):

    match_schema = MatchResult.model_json_schema()

    
    prompt = f"""
You are an HR recruiter.

Compare the candidate's resume with the job description.

JOB DESCRIPTION:
{job.model_dump_json(indent=2)}

CANDIDATE RESUME:
{resume.model_dump_json(indent=2)}

Analyze the following:

1. Candidate name.
2. Matching skills.
3. Missing important skills.
4. Whether experience requirement is met.
5. Educational qualification.
6. Relevant projects.
7. Overall match percentage from 0 to 100.
8. A short final verdict.

IMPORTANT JSON RULES:

Return ONLY valid JSON.

Follow this exact structure:

{{
    "score": 85,
    "details": {{
        "Candidate Name": "Candidate name",
        "Matching Skills": "Matching skills",
        "Missing Skills": "Missing skills",
        "Experience Requirement Met": "Yes or No with reason",
        "Educational Qualification": "Education details",
        "Relevant Projects": "Relevant projects",
        "Final Verdict": "Short verdict"
    }}
}}

All analysis fields MUST be inside the details object.

Do not add any additional fields outside this structure.
"""


    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        response_format={"type": "json_object"},
        temperature=0.2
    )

    data = json.loads(response.choices[0].message.content)

    return MatchResult.model_validate(data)


# ==============================
# 4. READ PDF RESUME
# ==============================

from pypdf import PdfReader
from docx import Document


def read_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# ==============================
# 5. READ DOCX RESUME
# ==============================

def read_docx(file_path):

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text += paragraph.text + "\n"

    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                if cell.text.strip():
                    text += cell.text + "\n"

    return text


# ==============================
# 6. SELECT FILE READER
# ==============================

def read_resume(file_path):

    if file_path.suffix.lower() == ".pdf":
        return read_pdf(file_path)

    elif file_path.suffix.lower() == ".docx":
        return read_docx(file_path)

    else:
        raise ValueError("Unsupported resume format")


# ==============================
# 7. PROCESS ALL RESUMES
# ==============================

resume_folder = Path(__file__).parent / "resumes"

all_results = []

if not resume_folder.exists():
    raise FileNotFoundError("Resumes folder does not exist")


for file_path in resume_folder.iterdir():

    if file_path.suffix.lower() not in [".pdf", ".docx"]:
        continue

    print("\nProcessing:", file_path.name)

    try:

        # Step 1: Read resume
        resume_text = read_resume(file_path)

        if not resume_text.strip():
            print("No readable text found. Skipping.")
            continue

        # Step 2: Extract resume information
        parsed_resume = parse_resume(resume_text)

        time.sleep(5)

        # Step 3: Compare resume with job description
        result = final_score(job, parsed_resume)

        time.sleep(5)

        # Step 4: Store candidate result
        all_results.append({
            "name": parsed_resume.name or file_path.stem,
            "score": result.score,
            "details": result.details
        })

        print("Score:", result.score)

    except Exception as e:

        print("Error processing", file_path.name, ":", e)


# ==============================
# 8. RANK CANDIDATES
# ==============================

all_results.sort(
    key=lambda candidate: candidate["score"],
    reverse=True
)


# ==============================
# 9. DISPLAY TOP 2
# ==============================

top_2 = all_results[:2]

print("\n========== TOP 2 CANDIDATES ==========")

for candidate in top_2:

    print(
        candidate["name"],
        "-",
        candidate["score"],
        "%"
    )

    print(candidate["details"])


# ==============================
# 10. DISPLAY LOWEST 2
# ==============================

worst_2 = all_results[-2:]

print("\n========== LOWEST 2 CANDIDATES ==========")

for candidate in worst_2:

    print(
        candidate["name"],
        "-",
        candidate["score"],
        "%"
    )

    print(candidate["details"])


# ==============================
# 11. TOTAL CANDIDATES
# ==============================

print("\nTotal candidates processed:", len(all_results))
