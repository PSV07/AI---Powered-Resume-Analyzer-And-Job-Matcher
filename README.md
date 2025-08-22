# AI---Powered-Resume-Analyzer-And-Job-Matcher
================================================
🚀 Project Overview

This project is an AI-driven Resume Analyzer that evaluates resumes against job descriptions (JDs) and provides:
A Match Score (0–100%) based on skill similarity.
Missing skills & improvement suggestions for candidates.
A Recruiter dashboard (optional) to rank multiple resumes for a job posting.
The system combines Natural Language Processing (NLP), Machine Learning (ML), and Cloud Computing for scalability.
_______________________________________________________________________________________________________________________________________________________________________________________________

✨ Features

📑 Resume Parsing – Extract text from PDF/DOC resumes.
🔍 Job Description Analysis – Extract required skills & keywords.
🤖 AI Matching Engine – Uses Sentence-BERT embeddings + cosine similarity to calculate match score.
📝 Improvement Suggestions – Identifies missing keywords/skills.
☁️ Cloud Deployment – Resumes stored in cloud (AWS S3/Azure Blob).
📊 Recruiter Dashboard (optional) – Compare multiple candidates.
______________________________________________________________________________________________________________________________________________________________________________________________

🏗️ System Architecture
_____________________________________________________________________________________
|                                                                                    |
|  [Frontend (React)]                                                                |
|        |                                                                           | 
|        v                                                                           |  
|   [Spring Boot Backend (Java)]  ---> [Database (PostgreSQL/MongoDB)]               |
|        |                                                                           |  
|        v                                                                           |  
|   [ML Microservice (Python FastAPI/Flask)]                                         | 
|        |                                                                           |   
|        v                                                                           |  
|   [AI/NLP Engine (BERT/SBERT, spaCy)]                                              |
|        |                                                                           |  
|        v                                                                           |
|   [Cloud Storage (AWS S3 / Azure Blob)]                                            | 
|____________________________________________________________________________________|

____________________________________________________________________________________________________________________________________________________________________________________________

⚙️ Tech Stack

Frontend: React / Angular
Backend: Spring Boot (Java)
ML Service: Python (FastAPI / Flask, HuggingFace Transformers, spaCy)
Database: PostgreSQL / MongoDB
Cloud: AWS (S3, EC2, RDS, Lambda) or Azure (Blob, Functions, App Service)
Libraries/Tools:

    Resume Parsing → PyMuPDF, pdfminer
    NLP & ML → Sentence-BERT, spaCy, scikit-learn
    Deployment → Docker, AWS/GCP/Azure
____________________________________________________________________________________________________________________________________________________________________________________________

🔮 Future Enhancements

✅ LinkedIn Job Scraper → Auto-fetch JDs.
✅ Chatbot Support → “Why is my resume score low?” → AI explains.
✅ Multi-language Resume Support.
✅ Analytics Dashboard → Most missing skills across all resumes.
____________________________________________________________________________________________________________________________________________________________________________________________

🧑‍💻 How to Run Locally

1. Clone the Repository
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer

2. Run ML Microservice (Python)
cd ml-service
pip install -r requirements.txt
uvicorn app:main --reload

3. Run Backend (Spring Boot)
cd backend
./mvnw spring-boot:run

4. Run Frontend (React)
cd frontend
npm install
npm start
____________________________________________________________________________________________________________________________________________________________________________________________

📊 Sample Output

Match Score: 78%
Missing Skills: Spring Boot, Kubernetes, AWS
Suggestions: “Add cloud-related keywords in your resume.”
____________________________________________________________________________________________________________________________________________________________________________________________

📜 License

This project is licensed under the MIT License – feel free to use and modify.
____________________________________________________________________________________________________________________________________________________________________________________________

👤 Author

👨‍💻 Parag Soni – B.Tech CSE (AIML), Technocrats Institute of Technology
💼 Interested in AI + Cloud Computing | Preparing for 15+ LPA roles    
