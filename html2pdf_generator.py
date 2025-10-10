"""
HTML to PDF Resume Generator using xhtml2pdf
Pure Python solution that works perfectly on Windows
"""

import os

from xhtml2pdf import pisa


def generate_html_content():
    """Generate the HTML content for the resume"""
    html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Resume - Pawarit Thareechan</title>
    <style>
        @page {
            size: a4;
            margin: 0.5in;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Helvetica, Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.4;
            color: #333;
        }

        .header {
            margin-bottom: 15pt;
            border-bottom: 2pt solid #2c3e50;
            padding-bottom: 10pt;
        }

        .name {
            font-size: 24pt;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 4pt;
        }

        .title {
            font-size: 14pt;
            color: #2c3e50;
            margin-bottom: 6pt;
        }

        .contact {
            font-size: 11pt;
            color: #555;
            margin-bottom: 3pt;
        }

        .section {
            margin-bottom: 15pt;
        }

        .section-title {
            font-size: 14pt;
            font-weight: bold;
            color: #2c3e50;
            text-transform: uppercase;
            border-bottom: 1pt solid #bdc3c7;
            padding-bottom: 3pt;
            margin-bottom: 8pt;
        }

        .job {
            margin-bottom: 10pt;
        }

        .company {
            font-weight: bold;
            font-size: 12pt;
            color: #2c3e50;
        }

        .position {
            font-style: italic;
            color: #555;
            margin-bottom: 2pt;
        }

        .duration {
            font-family: Courier, monospace;
            font-size: 10pt;
            color: #000;
            margin-bottom: 4pt;
        }

        .description-list {
            margin: 6pt 0 0 20pt;
            padding-left: 0;
        }

        .description-list li {
            margin-bottom: 4pt;
            font-size: 10.5pt;
            line-height: 1.4;
            color: #444;
        }

        .accomplishment {
            margin-bottom: 8pt;
        }

        .accomplishment-title {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 2pt;
            font-size: 11pt;
        }

        .accomplishment-details {
            color: #555;
            font-size: 10.5pt;
            line-height: 1.3;
            margin-bottom: 2pt;
        }

        .accomplishment-year {
            font-family: Courier, monospace;
            font-size: 10pt;
            color: #000;
        }

        .education-item {
            margin-bottom: 10pt;
        }

        .degree {
            font-weight: bold;
            color: #2c3e50;
            font-size: 12pt;
        }

        .university {
            color: #555;
            font-style: italic;
            margin-top: 2pt;
        }

        .education-duration {
            font-family: Courier, monospace;
            font-size: 10pt;
            color: #000;
            margin-top: 2pt;
        }

        .skill-category {
            margin-bottom: 6pt;
        }

        .skill-label {
            font-weight: bold;
            color: #2c3e50;
            display: inline;
        }

        .skill-items {
            color: #555;
            display: inline;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="name">Pawarit Thareechan</div>
        <div class="title">Data Scientist | Machine Learning Engineer</div>
        <div class="contact">T.Pawarit@lckyn.com | +66 83-028-2014</div>
        <div class="contact">linkedin.lckyn.com | github.lckyn.com</div>
    </div>

    <div class="section">
        <div class="section-title">Experience</div>

        <div class="job">
            <div class="company">Avalant Co. Ltd.</div>
            <div class="position">Data Scientist</div>
            <div class="duration">Apr 2023 - Present | 2 years 6 months</div>
            <ul class="description-list">
                <li><strong>AIG Chatbot with Budget Allocation System:</strong> Built intelligent chatbot combining data mining and RAG for HR budget allocation recommendations. Developed ML-powered system to suggest optimal budget ratios and predict allocation outcomes for data-driven decision-making.</li>
                <li><strong>HR Performance Analytics & Workload Balancing:</strong> Developed real-time analytics pipeline collecting project completion times, monitoring individual employee patterns overtime (base hour, high workmanship overtime). Created automated balanced workload allocation systems.</li>
                <li><strong>Wind Turbine Rotor Failure Analysis:</strong> Applied signal analysis on sensor data to predict copper rotor breakage in 1,500 RPM turbines. Identified critical data collection gap (10-minute interval) when failures typically occur. Developed predictive models and recommended edge-based sampling (at least 3-10 degrees per sample) instead of time-based approach to capture converter-driven micro-vibrations effectively.</li>
            </ul>
        </div>

        <div class="job">
            <div class="company">Looloo Technology</div>
            <div class="position">Machine Learning Engineer</div>
            <div class="duration">Aug 2021 - Mar 2023 | 1 year 8 months</div>
            <ul class="description-list">
                <li><strong>Car Auction Pricing Model:</strong> Developed ML model with 13-20% average price error using brand, model, year, and color features, solving price instability by 80%. Implemented real-time vehicle price assessment improving auction workflow and reducing costly pricing decision.</li>
                <li><strong>Bone Mineralization Assessment:</strong> Built multi-stage verification system with QR code validation. Mizer fingerprint detection for secure authentication across patient record system. Improved accuracy to 82% for fingerprint verification rate, accelerating verification workflow by 64%.</li>
                <li><strong>Symptom Clustering System:</strong> Developed LLM and ML-powered system to automatically extract and analyze patient symptoms from medical records. Enabled doctors to focus on key symptoms pattern while automatically recording structured data in database, improving clinic efficiency and data quality.</li>
            </ul>
        </div>

        <div class="job">
            <div class="company">ICONTEX Co., Ltd.</div>
            <div class="position">Software Engineering Intern</div>
            <div class="duration">Apr 2018 - Jul 2018 | 4 months</div>
            <ul class="description-list">
                <li><strong>Line Chatbot for Meeting Room Booking:</strong> Built automated booking system eliminating manual 5-hour processes and improving user adoption through familiarized social media interface. Streamlined room reservation workflows and reduced administrative overhead.</li>
                <li><strong>Automated Sales Reporting System:</strong> Developed real-time reporting solution for rental company, reducing manual data entry and ensuring real-time database synchronization. Improved data accuracy and operational efficiency.</li>
            </ul>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Key Achievements</div>

        <div class="accomplishment">
            <div class="accomplishment-title">Health Data Science Hackathon by BDMS - Winner, THB 10,000 prize</div>
            <div class="accomplishment-details">Led a 3-person team, built healthcare prediction model and visualized insights to support diagnosis and resource planning.</div>
            <div class="accomplishment-year">2021</div>
        </div>

        <div class="accomplishment">
            <div class="accomplishment-title">Teaching Assistant - Computer Engineering</div>
            <div class="accomplishment-details">Assisted in algorithm courses: Data Structures and Algorithms, Machine Learning, Introduction to Design and Analysis of Algorithms.</div>
            <div class="accomplishment-year">2021</div>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Technical Skills</div>

        <div class="skill-category">
            <span class="skill-label">Programming:</span>
            <span class="skill-items">Python, SQL, JavaScript, Shell, C#</span>
        </div>
        <div class="skill-category">
            <span class="skill-label">ML/AI:</span>
            <span class="skill-items">PyTorch, TensorFlow, scikit-learn, NLP, Computer Vision, Deep Learning</span>
        </div>
        <div class="skill-category">
            <span class="skill-label">Data Engineering:</span>
            <span class="skill-items">Apache Spark, Airflow, ETL/ELT, Data Pipelines, Real-time Processing</span>
        </div>
        <div class="skill-category">
            <span class="skill-label">Vector Databases & RAG:</span>
            <span class="skill-items">Milvus, DIS, Embedding Models, Semantic Search</span>
        </div>
        <div class="skill-category">
            <span class="skill-label">Cloud/Tools:</span>
            <span class="skill-items">Docker, Git, CI/CD, MLops, Apache Superset, PostgreSQL, Vector Databases (Milvus)</span>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Education</div>

        <div class="education-item">
            <div class="degree">Bachelor of Engineering in Computer Engineering</div>
            <div class="university">Kasetsart University</div>
            <div class="education-duration">2017 - 2021</div>
        </div>
    </div>
</body>
</html>
"""
    return html_template


def generate_pdf_with_xhtml2pdf(output_path="resume_html2pdf.pdf"):
    """Generate PDF from HTML using xhtml2pdf"""

    print("🎨 Generating PDF with xhtml2pdf...")
    print("   Using HTML rendering for quality output")

    try:
        # Generate HTML content
        html_content = generate_html_content()

        # Convert HTML to PDF
        with open(output_path, "w+b") as pdf_file:
            pisa_status = pisa.CreatePDF(html_content, dest=pdf_file, encoding="utf-8")

        if not pisa_status.err:
            size = os.path.getsize(output_path)
            print(f"✅ PDF generated successfully: {output_path}")
            print(f"📊 File size: {size:,} bytes")
            print(f"✨ Features:")
            print(f"   ✓ Professional typography")
            print(f"   ✓ Clean layout")
            print(f"   ✓ Proper margins (0.5 inch)")
            print(f"   ✓ Works on Windows without extra dependencies")
            return output_path
        else:
            print(f"❌ Error generating PDF: {pisa_status.err}")
            return None

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return None


if __name__ == "__main__":
    generate_pdf_with_xhtml2pdf()
