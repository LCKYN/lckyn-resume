// Duration calculation functions
function parseDate(dateStr) {
    // Handle different date formats
    const cleanStr = dateStr.trim().toLowerCase();

    // Handle "Present" case
    if (cleanStr === 'present') {
        return new Date();
    }

    // Parse "MMM YYYY" format (e.g., "Apr 2023")
    const monthYear = cleanStr.match(/^([a-z]{3})\s+(\d{4})$/);
    if (monthYear) {
        const monthNames = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
            'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
        const monthIndex = monthNames.indexOf(monthYear[1]);
        const year = parseInt(monthYear[2]);
        return new Date(year, monthIndex, 1);
    }

    // Fallback to Date constructor
    return new Date(dateStr);
}

function calculateDuration(startDate, endDate) {
    const start = parseDate(startDate);
    const end = parseDate(endDate);

    let years = end.getFullYear() - start.getFullYear();
    let months = end.getMonth() - start.getMonth();

    if (months < 0) {
        years--;
        months += 12;
    }

    let result = '';
    if (years > 0) {
        result += `${years} year${years > 1 ? 's' : ''}`;
    }
    if (months > 0) {
        if (result) result += ' ';
        result += `${months} month${months > 1 ? 's' : ''}`;
    }

    return result || '0 months';
}

function formatDurationRange(duration) {
    // Extract start and end dates from duration string
    const parts = duration.split(' – ');
    if (parts.length !== 2) {
        return { duration: duration, detail: '' };
    }

    const startDate = parts[0].trim();
    const endDate = parts[1].trim();

    const calculatedDuration = calculateDuration(startDate, endDate);

    return {
        duration: duration,
        detail: calculatedDuration
    };
}

// Resume data in JSON format
const resumeData = {
    "name": "Pawarit Thareechan",
    "contact": {
        "email": "T.Pawarit@lckyn.com",
        "phone": "+66 83-028-2014",
        "linkedin": "linkedin.lckyn.com",
        "github": "github.lckyn.com"
    },
    "title": "Data Scientist | Machine Learning Engineer",
    "experience": [
        {
            "company": "Avalant Co. Ltd.",
            "position": "Data Scientist",
            "duration": "Apr 2023 – Present",
            "descriptions": [
                "Built RAG chatbot system handling HR queries and government budget allocation predictions, integrating email automation and ML-powered budget ratio forecasting for Thai government projects.",
                "Developed real-time HR performance analytics pipeline tracking project completion times, predicting task duration, and detecting anomalies in employee patterns (leave abuse, low productivity) with live dashboard for HR teams."
            ]
        },
        {
            "company": "Looloo Technology",
            "position": "Machine Learning Engineer",
            "duration": "Aug 2021 – Mar 2023",
            "descriptions": [
                "<strong>Car Auction Pricing Model:</strong> Developed ML model with 11-26% average price error using brand, model, year, and color features, solving data imbalance by leveraging similar-vehicle pricing patterns. Deployed real-time price range predictions to help valuers and customers make informed bidding decisions.",
                "<strong>Image Authentication Pipeline:</strong> Built multi-stage verification system with QR code validation, Moiré pattern detection for screen capture rejection, and EfficientNet classification to verify legitimate cardboard-based submissions. Achieved 97% accuracy with 0.2% false positive rate, accelerating verification workflow by 66%."
            ]
        },
        {
            "company": "iCONEXT Co., Ltd.",
            "position": "Software Engineer Intern",
            "duration": "Apr 2018 – Jul 2018",
            "descriptions": [
                "<strong>Line Chatbot for Meeting Room Booking:</strong> Built automated booking system eliminating manual G Suite processes and improving user adoption through familiar messaging interface. Streamlined room reservation workflow and reduced administrative overhead.",
                "<strong>Automated Sales Reporting System:</strong> Developed real-time reporting solution for metal company, reducing manual data entry and ensuring real-time database synchronization. Improved data accuracy and operational efficiency."
            ]
        }
    ],
    "accomplishments": [
        {
            "year": "2021",
            "title": "Health Data Science Hackathon by BDMS – Winner, THB 10,000 prize",
            "description": "Won 24-hour hackathon with 3-person team, built healthcare prediction model and visualized insights to support diagnosis and resource planning"
        },
        {
            "year": "2021",
            "title": "Teaching Assistant – Computer Engineering",
            "description": "Assisted in undergraduate courses: Data Structures and Algorithms, Machine Learning, Introduction to Design and Analysis of Algorithms"
        }
    ],
    "education": [
        {
            "degree": "Bachelor of Engineering in Computer Engineering",
            "university": "King Mongkut's University of Technology North Bangkok (KMUTNB)",
            "duration": "Aug 2015 – Apr 2019"
        }
    ],
    "skills": {
        "Programming": "Python, SQL, JavaScript, Shell, C#",
        "ML/AI": "PyTorch, TensorFlow, scikit-learn, NLP, Computer Vision, Deep Learning",
        "Data Engineering": "Apache Spark, Airflow, ETL/ELT, Data Pipelines, Real-time Processing",
        "Vector Databases & RAG": "Milvus, Dify, Embedding Models, Semantic Search",
        "Cloud/Tools": "Docker, Git, CI/CD, Min.io, Apache Superset, PostgreSQL, Vector Databases (Milvus)",
        "Visualization": "Dashboard Development, Business Intelligence, Data Visualization"
    },
    // New sections for page 2
    "additionalAccomplishments": [
        {
            "year": "2019",
            "title": "Senior Project – ML Model Evaluation: AUC vs Accuracy Performance Study",
            "description": "Researched optimal feature selection methods and compared AUC vs accuracy metrics, demonstrating AUC's superior ability to distinguish model quality despite complexity trade-offs"
        },
        {
            "year": "2018",
            "title": "Cyber Security Challenge by KPMG – 12th place (Top 60%)",
            "description": "Competed in 4-person team during one-day hackathon solving real-world cybersecurity scenarios among 20 teams"
        }
    ],
    "personalProjects": [
        {
            "year": "2024 – Present",
            "title": "Discord Anti-Spam Bot – Behavioral Analysis System",
            "description": "Developed ML-powered bot protecting 6,000+ users (500-1,000 active weekly) with 100% accuracy over 1+ year, using behavioral pattern analysis to distinguish scammers from legitimate users without false positives"
        }
    ],
    "certifications": [
        // Add certifications here if you have any
    ],
    "additionalSkills": {
        // Add more detailed technical skills here if needed
    }
};

function createHeader(data) {
    return `
        <div class="header">
            <div class="header-row">
                <div class="name">${data.name}</div>
                <div class="contact-primary">${data.contact.email} | ${data.contact.phone}</div>
            </div>
            <div class="header-row">
                <div class="title">${data.title}</div>
                <div class="contact-secondary"><a href="https://${data.contact.linkedin}" target="_blank">${data.contact.linkedin}</a> | <a href="https://${data.contact.github}" target="_blank">${data.contact.github}</a></div>
            </div>
        </div>
    `;
}

function createContinuationHeader(data) {
    return `
        <div class="continuation-header">
            <div class="continuation-name">${data.name}</div>
        </div>
    `;
}

function createExperienceSection(data) {
    return `
        <div class="section">
            <div class="section-title">Experience</div>
            ${data.experience.map(job => {
        const durationInfo = formatDurationRange(job.duration);

        // Create bullet list instead of paragraph
        const bulletList = job.descriptions.map(desc =>
            `<li>${desc}</li>`
        ).join('');

        return `
                    <div class="job">
                        <div class="job-header">
                            <div>
                                <div class="company">${job.company}</div>
                                <div class="position">${job.position}</div>
                            </div>
                            <div class="duration-container">
                                <div class="duration-main">${durationInfo.duration}</div>
                                <div class="duration-detail">${durationInfo.detail}</div>
                            </div>
                        </div>
                        <ul class="description-list">${bulletList}</ul>
                    </div>
                `;
    }).join('')}
        </div>
    `;
}

function createAccomplishmentsSection(data) {
    return `
        <div class="section">
            <div class="section-title">Key Achievements</div>
            ${data.accomplishments.map(acc => `
                <div class="accomplishment">
                    <div class="accomplishment-content">
                        <div class="accomplishment-title">${acc.title}</div>
                        <div class="accomplishment-details">${acc.description}</div>
                    </div>
                    <div class="accomplishment-year">${acc.year}</div>
                </div>
            `).join('')}
        </div>
    `;
}

function createAdditionalAccomplishmentsSection(data) {
    if (!data.additionalAccomplishments || data.additionalAccomplishments.length === 0) {
        return '';
    }
    return `
        <div class="section">
            <div class="section-title">Additional Projects & Activities</div>
            ${data.additionalAccomplishments.map(acc => `
                <div class="accomplishment">
                    <div class="accomplishment-content">
                        <div class="accomplishment-title">${acc.title}</div>
                        <div class="accomplishment-details">${acc.description}</div>
                    </div>
                    <div class="accomplishment-year">${acc.year}</div>
                </div>
            `).join('')}
        </div>
    `;
}

function createEducationSection(data) {
    return `
        <div class="section">
            <div class="section-title">Education</div>
            ${data.education.map(edu => {
        const durationInfo = formatDurationRange(edu.duration);
        return `
                    <div class="education-item">
                        <div class="education-header">
                            <div>
                                <div class="degree">${edu.degree}</div>
                                <div class="university">${edu.university}</div>
                            </div>
                            <div class="education-duration">
                                <div>${durationInfo.duration}</div>
                                <div>${durationInfo.detail}</div>
                            </div>
                        </div>
                    </div>
                `;
    }).join('')}
        </div>
    `;
}

function createSkillsSection(data) {
    return `
        <div class="section">
            <div class="section-title">Technical Skills</div>
            <div class="skills-grid">
                ${Object.entries(data.skills).map(([category, items]) => `
                    <div class="skill-category">
                        <div class="skill-label">${category}:</div>
                        <div class="skill-items">${items}</div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

function createPersonalProjectsSection(data) {
    if (!data.personalProjects || data.personalProjects.length === 0) {
        return '';
    }
    return `
        <div class="section">
            <div class="section-title">Personal Projects</div>
            ${data.personalProjects.map(project => `
                <div class="accomplishment">
                    <div class="accomplishment-content">
                        <div class="accomplishment-title">${project.title}</div>
                        <div class="accomplishment-details">${project.description}</div>
                    </div>
                    <div class="accomplishment-year">${project.year}</div>
                </div>
            `).join('')}
        </div>
    `;
}

function createCertificationsSection(data) {
    if (!data.certifications || data.certifications.length === 0) {
        return '';
    }
    return `
        <div class="section">
            <div class="section-title">Certifications</div>
            ${data.certifications.map(cert => `
                <div class="accomplishment">
                    <div class="accomplishment-content">
                        <div class="accomplishment-title">${cert.title}</div>
                        <div class="accomplishment-details">${cert.issuer}${cert.details ? ' - ' + cert.details : ''}</div>
                    </div>
                    <div class="accomplishment-year">${cert.year}</div>
                </div>
            `).join('')}
        </div>
    `;
}

function createPageFooter(pageNumber) {
    return `
        <div class="footer">
            <div class="page-number">- ${pageNumber} -</div>
        </div>
    `;
}

function renderMultiPageResume(data) {
    const container = document.getElementById('resume-pages');

    // Page 1 content
    const page1Content = `
        <div class="content">
            ${createHeader(data)}
            ${createExperienceSection(data)}
            ${createAccomplishmentsSection(data)}
            ${createSkillsSection(data)}
        </div>

    `;

    // Page 2 content
    const page2Content = `
        <div class="content">
            ${createContinuationHeader(data)}
            ${createEducationSection(data)}
            ${createPersonalProjectsSection(data)}
            ${createAdditionalAccomplishmentsSection(data)}
            ${createCertificationsSection(data)}
        </div>
        ${createPageFooter(2)}
    `;

    // Only create page 2 if there's content for it
    const hasPage2Content = (data.additionalAccomplishments && data.additionalAccomplishments.length > 0) ||
        (data.personalProjects && data.personalProjects.length > 0) ||
        (data.certifications && data.certifications.length > 0);

    if (hasPage2Content) {
        container.innerHTML = `
            <div class="page">${page1Content}</div>
            <div class="page">${page2Content}</div>
        `;
    } else {
        container.innerHTML = `
            <div class="page">${page1Content}</div>
        `;
    }
}

// Render the resume when the page loads
document.addEventListener('DOMContentLoaded', function () {
    renderMultiPageResume(resumeData);
});
