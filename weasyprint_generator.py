"""
HTML to PDF Resume Generator using WeasyPrint
This renders the HTML/CSS directly to PDF, maintaining exact appearance
"""

import os

from weasyprint import HTML


def generate_html_content():
    """Generate the HTML content for the resume"""
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Resume - Pawarit Thareechan</title>
    <style>
        @page {
            size: A4;
            margin: 0.5in;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Cambria', 'Georgia', serif;
            font-size: 11pt;
            line-height: 1.4;
            color: #333;
            background: white;
            padding: 0;
        }

        .header {
            margin-bottom: 20px;
            border-bottom: 2px solid #2c3e50;
            padding-bottom: 15px;
        }

        .header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
        }

        .name {
            font-size: 24pt;
            font-weight: bold;
            color: #2c3e50;
        }

        .contact-primary {
            font-size: 11pt;
            color: #555;
            text-align: right;
        }

        .title {
            font-size: 14pt;
            color: #2c3e50;
            font-weight: 500;
        }

        .contact-secondary {
            font-size: 11pt;
            color: #555;
            text-align: right;
        }

        .section {
            margin-bottom: 18px;
            page-break-inside: avoid;
        }

        .section-title {
            font-size: 14pt;
            font-weight: bold;
            color: #2c3e50;
            text-transform: uppercase;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 3px;
            margin-bottom: 10px;
        }

        .job {
            margin-bottom: 12px;
            page-break-inside: avoid;
        }

        .job-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 6px;
        }

        .company {
            font-weight: bold;
            font-size: 12pt;
            color: #2c3e50;
        }

        .position {
            font-style: italic;
            color: #555;
            margin-bottom: 2px;
        }

        .duration-container {
            text-align: right;
            font-size: 10pt;
            color: #000000;
            min-width: 200px;
        }

        .duration-main {
            font-family: 'Courier New', monospace;
            margin-bottom: 2px;
        }

        .duration-detail {
            font-family: 'Courier New', monospace;
        }

        .description-list {
            margin: 8px 0;
            padding-left: 20px;
        }

        .description-list li {
            margin-bottom: 4px;
            font-size: 10.5pt;
            line-height: 1.4;
            color: #444;
            text-align: justify;
        }

        .accomplishment {
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 15px;
            page-break-inside: avoid;
        }

        .accomplishment-content {
            flex: 1;
        }

        .accomplishment-title {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 2px;
            font-size: 11pt;
        }

        .accomplishment-details {
            color: #555;
            font-size: 10.5pt;
            line-height: 1.3;
        }

        .accomplishment-year {
            font-family: 'Courier New', monospace;
            font-size: 10pt;
            color: #000000;
            min-width: 50px;
            flex-shrink: 0;
            text-align: right;
            margin-top: 2px;
        }

        .education-item {
            margin-bottom: 12px;
            page-break-inside: avoid;
        }

        .education-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 4px;
        }

        .degree {
            font-weight: bold;
            color: #2c3e50;
            font-size: 12pt;
        }

        .university {
            color: #555;
            font-style: italic;
            margin-top: 2px;
        }

        .education-duration {
            text-align: right;
            font-size: 10pt;
            color: #000000;
            font-family: 'Courier New', monospace;
            min-width: 200px;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 8px;
        }

        .skill-category {
            display: flex;
            align-items: flex-start;
            gap: 8px;
            page-break-inside: avoid;
        }

        .skill-label {
            font-weight: bold;
            color: #2c3e50;
            min-width: 140px;
            flex-shrink: 0;
        }

        .skill-items {
            color: #555;
            line-height: 1.3;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-row">
            <div class="name">Pawarit Thareechan</div>
            <div class="contact-primary">T.Pawarit@lckyn.com | +66 83-028-2014</div>
        </div>
        <div class="header-row">
            <div class="title">Data Scientist | Machine Learning Engineer</div>
            <div class="contact-secondary">linkedin.lckyn.com | github.lckyn.com</div>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Experience</div>

        <div class="job">
            <div class="job-header">
                <div>
                    <div class="company">Avalant Co. Ltd.</div>
                    <div class="position">Data Scientist</div>
                </div>
                <div class="duration-container">
                    <div class="duration-main">Apr 2023 - Present</div>
                    <div class="duration-detail">2 years 6 months</div>
                </div>
            </div>
            <ul class="description-list">
                <li>AIG Chatbot with Budget Allocation System: Built intelligent chatbot combining data mining and RAG for HR budget allocation recommendations. Developed ML-powered system to suggest optimal budget ratios and predict allocation outcomes for data-driven decision-making.</li>
                <li>HR Performance Analytics & Workload Balancing: Developed real-time analytics pipeline collecting project completion times, monitoring individual employee patterns overtime (base hour, high workmanship overtime). Created automated balanced workload allocation systems.</li>
                <li>Wind Turbine Rotor Failure Analysis: Applied signal analysis on sensor data to predict copper rotor breakage in 1,500 RPM turbines. Identified critical data collection gap (10-minute interval) when failures typically occur. Developed predictive models and recommended edge-based sampling (at least 3-10 degrees per sample) instead of time-based approach to capture converter-driven micro-vibrations effectively.</li>
            </ul>
        </div>

        <div class="job">
            <div class="job-header">
                <div>
                    <div class="company">Looloo Technology</div>
                    <div class="position">Machine Learning Engineer</div>
                </div>
                <div class="duration-container">
                    <div class="duration-main">Aug 2021 - Mar 2023</div>
                    <div class="duration-detail">1 year 8 months</div>
                </div>
            </div>
            <ul class="description-list">
                <li>Car Auction Pricing Model: Developed ML model with 13-20% average price error using brand, model, year, and color features, solving price instability by 80%. Implemented real-time vehicle price assessment improving auction workflow and reducing costly pricing decision.</li>
                <li>Bone Mineralization Assessment: Built multi-stage verification system with QR code validation. Mizer fingerprint detection for secure authentication across patient record system. Improved accuracy to 82% for fingerprint verification rate, accelerating verification workflow by 64%.</li>
                <li>Symptom Clustering System: Developed LLM and ML-powered system to automatically extract and analyze patient symptoms from medical records. Enabled doctors to focus on key symptoms pattern while automatically recording structured data in database, improving clinic efficiency and data quality.</li>
            </ul>
        </div>

        <div class="job">
            <div class="job-header">
                <div>
                    <div class="company">ICONTEX Co., Ltd.</div>
                    <div class="position">Software Engineering Intern</div>
                </div>
                <div class="duration-container">
                    <div class="duration-main">Apr 2018 - Jul 2018</div>
                    <div class="duration-detail">4 months</div>
                </div>
            </div>
            <ul class="description-list">
                <li>Line Chatbot for Meeting Room Booking: Built automated booking system eliminating manual 5-hour processes and improving user adoption through familiarized social media interface. Streamlined room reservation workflows and reduced administrative overhead.</li>
                <li>Automated Sales Reporting System: Developed real-time reporting solution for rental company, reducing manual data entry and ensuring real-time database synchronization. Improved data accuracy and operational efficiency.</li>
            </ul>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Key Achievements</div>

        <div class="accomplishment">
            <div class="accomplishment-content">
                <div class="accomplishment-title">Health Data Science Hackathon by BDMS - Winner, THB 10,000 prize</div>
                <div class="accomplishment-details">Led a 3-person team, built healthcare prediction model and visualized insights to support diagnosis and resource planning.</div>
            </div>
            <div class="accomplishment-year">2021</div>
        </div>

        <div class="accomplishment">
            <div class="accomplishment-content">
                <div class="accomplishment-title">Teaching Assistant - Computer Engineering</div>
                <div class="accomplishment-details">Assisted in algorithm courses: Data Structures and Algorithms, Machine Learning, Introduction to Design and Analysis of Algorithms.</div>
            </div>
            <div class="accomplishment-year">2021</div>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Technical Skills</div>

        <div class="skills-grid">
            <div class="skill-category">
                <div class="skill-label">Programming:</div>
                <div class="skill-items">Python, SQL, JavaScript, Shell, C#</div>
            </div>
            <div class="skill-category">
                <div class="skill-label">ML/AI:</div>
                <div class="skill-items">PyTorch, TensorFlow, scikit-learn, NLP, Computer Vision, Deep Learning</div>
            </div>
            <div class="skill-category">
                <div class="skill-label">Data Engineering:</div>
                <div class="skill-items">Apache Spark, Airflow, ETL/ELT, Data Pipelines, Real-time Processing</div>
            </div>
            <div class="skill-category">
                <div class="skill-label">Vector Databases & RAG:</div>
                <div class="skill-items">Milvus, DIS, Embedding Models, Semantic Search</div>
            </div>
            <div class="skill-category">
                <div class="skill-label">Cloud/Tools:</div>
                <div class="skill-items">Docker, Git, CI/CD, MLops, Apache Superset, PostgreSQL, Vector Databases (Milvus)</div>
            </div>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Education</div>

        <div class="education-item">
            <div class="education-header">
                <div>
                    <div class="degree">Bachelor of Engineering in Computer Engineering</div>
                    <div class="university">Kasetsart University</div>
                </div>
                <div class="education-duration">2017 - 2021</div>
            </div>
        </div>
    </div>
</body>
</html>
"""
    return html_template


def generate_pdf_with_weasyprint(output_path="resume_weasyprint.pdf"):
    """Generate PDF from HTML using WeasyPrint"""

    print("🎨 Generating PDF with WeasyPrint...")
    print("   Using HTML/CSS rendering for perfect quality")

    try:
        # Generate HTML content
        html_content = generate_html_content()

        # Convert HTML to PDF
        HTML(string=html_content).write_pdf(output_path)

        # Check file size
        if os.path.exists(output_path):
            size = os.path.getsize(output_path)
            print(f"✅ PDF generated successfully: {output_path}")
            print(f"📊 File size: {size:,} bytes")
            return output_path
        else:
            print("❌ Failed to generate PDF")
            return None

    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    generate_pdf_with_weasyprint()
