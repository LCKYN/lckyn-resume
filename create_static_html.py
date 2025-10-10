"""
Pre-render HTML content for wkhtmltopdf
Since wkhtmltopdf has issues with JavaScript, we'll generate a static HTML file
"""

import json
import os


def create_static_html():
    """Create a static HTML file with all content pre-rendered"""

    # Read the resume data from resume_data.py
    import resume_data

    data = resume_data.RESUME_DATA

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume - {data["personal"]["name"]}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="resume-pages">
        <div class="page">
            <div class="header">
                <h1 class="name">{data["personal"]["name"]}</h1>
                <p class="title">{data["personal"]["title"]}</p>
                <p class="contact">
                    {data["personal"]["email"]} | {data["personal"]["phone"]}<br>
                    {data["personal"]["linkedin"]} | {data["personal"]["github"]}
                </p>
            </div>

            <div class="content">
                <section class="section experience">
                    <h2 class="section-title">Experience</h2>
"""

    # Add experience
    for exp in data["experience"]:
        duration_detail = exp.get("duration_detail", "")
        html_content += f"""
                    <div class="job">
                        <div class="job-header">
                            <div class="job-info">
                                <h3 class="company">{exp["company"]}</h3>
                                <p class="position">{exp["position"]}</p>
                            </div>
                            <div class="duration">{exp["duration"]} | {duration_detail}</div>
                        </div>
                        <ul class="description">
"""
        for desc in exp["description"]:
            html_content += f"                            <li>{desc}</li>\n"

        html_content += """                        </ul>
                    </div>
"""

    html_content += """
                </section>

                <section class="section achievements">
                    <h2 class="section-title">Additional Accomplishments</h2>
                    <ul>
"""

    # Add achievements
    for achievement in data["achievements"]:
        html_content += f"""                        <li>
                            <strong>{achievement["title"]}</strong>
                            <p>{achievement["details"]}</p>
                        </li>
"""

    html_content += """                    </ul>
                </section>

                <section class="section skills">
                    <h2 class="section-title">Skills</h2>
"""

    # Add skills
    for category, skills in data["skills"].items():
        html_content += f"""                    <div class="skill-category">
                        <strong>{category}:</strong> {skills}
                    </div>
"""

    html_content += """
                </section>
            </div>

            <div class="footer">
                <p>Page 1</p>
            </div>
        </div>

        <div class="page">
            <div class="header continuation-header">
                <h1 class="name">{}</h1>
                <p class="title">{}</p>
            </div>

            <div class="content">
                <section class="section education">
                    <h2 class="section-title">Education</h2>
""".format(data["personal"]["name"], data["personal"]["title"])

    # Add education
    for edu in data["education"]:
        gpa_text = f" (GPA: {edu.get('gpa', 'N/A')})" if edu.get("gpa") else ""
        html_content += f"""                    <div class="education-item">
                        <h3 class="degree">{edu["degree"]}{gpa_text}</h3>
                        <p class="university">{edu["university"]}</p>
                        <p class="duration">{edu["duration"]}</p>
                    </div>
"""

    html_content += """                </section>
            </div>

            <div class="footer">
                <p>Page 2</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

    # Write to file
    output_file = "index_static.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Created static HTML: {output_file}")
    return output_file


if __name__ == "__main__":
    create_static_html()
