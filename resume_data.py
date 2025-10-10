"""
Resume data structure for Pawarit Thareechan
"""

from datetime import datetime

from dateutil.relativedelta import relativedelta


def calculate_duration(start_date, end_date):
    """Calculate duration between two dates"""
    if end_date == "Present":
        end_date = datetime.now()
    else:
        end_date = datetime.strptime(end_date, "%b %Y")

    start_date = datetime.strptime(start_date, "%b %Y")

    diff = relativedelta(end_date, start_date)

    result = []
    if diff.years > 0:
        result.append(f"{diff.years} year{'s' if diff.years > 1 else ''}")
    if diff.months > 0:
        result.append(f"{diff.months} month{'s' if diff.months > 1 else ''}")

    return " ".join(result) if result else "0 months"


RESUME_DATA = {
    "personal": {
        "name": "Pawarit Thareechan",
        "title": "Data Scientist | Machine Learning Engineer",
        "email": "T.Pawarit@lckyn.com",
        "phone": "+66 83-028-2014",
        "linkedin": "linkedin.lckyn.com",
        "github": "github.lckyn.com",
    },
    "experience": [
        {
            "company": "Avalant Co. Ltd.",
            "position": "Data Scientist",
            "duration": "Apr 2023 - Present",
            "duration_detail": calculate_duration("Apr 2023", "Present"),
            "description": [
                "AIG Chatbot with Budget Allocation System: Built intelligent chatbot combining data mining and RAG for HR budget allocation recommendations. Developed ML-powered system to suggest optimal budget ratios and predict allocation outcomes for data-driven decision-making.",
                "HR Performance Analytics & Workload Balancing: Developed real-time analytics pipeline collecting project completion times, monitoring individual employee patterns overtime (base hour, high workmanship overtime). Created automated balanced workload allocation systems.",
                "Wind Turbine Rotor Failure Analysis: Applied signal analysis on sensor data to predict copper rotor breakage in 1,500 RPM turbines. Identified critical data collection gap (10-minute interval) when failures typically occur. Developed predictive models and recommended edge-based sampling (at least 3-10 degrees per sample) instead of time-based approach to capture converter-driven micro-vibrations effectively.",
            ],
        },
        {
            "company": "Looloo Technology",
            "position": "Machine Learning Engineer",
            "duration": "Aug 2021 - Mar 2023",
            "duration_detail": calculate_duration("Aug 2021", "Mar 2023"),
            "description": [
                "Car Auction Pricing Model: Developed ML model with 13-20% average price error using brand, model, year, and color features, solving price instability by 80%. Implemented real-time vehicle price assessment improving auction workflow and reducing costly pricing decision.",
                "Bone Mineralization Assessment: Built multi-stage verification system with QR code validation. Mizer fingerprint detection for secure authentication across patient record system. Improved accuracy to 82% for fingerprint verification rate, accelerating verification workflow by 64%.",
                "Symptom Clustering System: Developed LLM and ML-powered system to automatically extract and analyze patient symptoms from medical records. Enabled doctors to focus on key symptoms pattern while automatically recording structured data in database, improving clinic efficiency and data quality.",
            ],
        },
        {
            "company": "ICONTEX Co., Ltd.",
            "position": "Software Engineering Intern",
            "duration": "Apr 2018 - Jul 2018",
            "duration_detail": calculate_duration("Apr 2018", "Jul 2018"),
            "description": [
                "Line Chatbot for Meeting Room Booking: Built automated booking system eliminating manual 5-hour processes and improving user adoption through familiarized social media interface. Streamlined room reservation workflows and reduced administrative overhead.",
                "Automated Sales Reporting System: Developed real-time reporting solution for rental company, reducing manual data entry and ensuring real-time database synchronization. Improved data accuracy and operational efficiency.",
            ],
        },
    ],
    "achievements": [
        {
            "title": "Health Data Science Hackathon by BDMS - Winner, THB 10,000 prize",
            "details": "Led a 3-person team, built healthcare prediction model and visualized insights to support diagnosis and resource planning.",
            "year": "2021",
        },
        {
            "title": "Teaching Assistant - Computer Engineering",
            "details": "Assisted in algorithm courses: Data Structures and Algorithms, Machine Learning, Introduction to Design and Analysis of Algorithms.",
            "year": "2021",
        },
    ],
    "education": [
        {
            "degree": "Bachelor of Engineering in Computer Engineering",
            "university": "King Mongkut's University of Technology North Bangkok (KMUTNB)",
            "duration": "2017 - 2021",
            "gpa": "3.45",
        }
    ],
    "skills": {
        "Programming": "Python, SQL, JavaScript, Shell, C#",
        "ML/AI": "PyTorch, TensorFlow, scikit-learn, NLP, Computer Vision, Deep Learning",
        "Data Engineering": "Apache Spark, Airflow, ETL/ELT, Data Pipelines, Real-time Processing",
        "Vector Databases & RAG": "Milvus, DIS, Embedding Models, Semantic Search",
        "Cloud/Tools": "Docker, Git, CI/CD, MLops, Apache Superset, PostgreSQL, Vector Databases (Milvus)",
    },
}
