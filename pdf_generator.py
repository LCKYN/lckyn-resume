"""
PDF Resume Generator using ReportLab - Professional Version
Matches the original HTML/CSS design quality
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_RIGHT, TA_JUSTIFY, TA_LEFT
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate

from resume_data import RESUME_DATA

# Color scheme matching HTML/CSS version
COLOR_PRIMARY = HexColor('#2c3e50')
COLOR_TEXT = HexColor('#333333')
COLOR_LIGHT_TEXT = HexColor('#555555')
COLOR_BORDER = HexColor('#bdc3c7')

class ResumeTemplate(BaseDocTemplate):
    """Custom template for resume with consistent margins"""
    
    def __init__(self, filename, **kwargs):
        self.allowSplitting = 1
        BaseDocTemplate.__init__(self, filename, **kwargs)
        
        # Define page margins - matching original design (20mm)
        margin = 20 * mm
        frame = Frame(margin, margin, A4[0] - 2*margin, A4[1] - 2*margin,
                     leftPadding=0, bottomPadding=15*mm, rightPadding=0, topPadding=0,
                     id='normal')
        
        template = PageTemplate(id='resume', frames=frame, onPage=self.add_page_number)
        self.addPageTemplates([template])
    
    def add_page_number(self, canvas, doc):
        """Add page number at bottom"""
        page_num = canvas.getPageNumber()
        if page_num > 1:
            canvas.saveState()
            canvas.setFont("Courier", 10)
            canvas.setFillColor(HexColor('#777777'))
            canvas.drawCentredString(A4[0]/2, 10*mm, f"Page {page_num}")
            canvas.restoreState()

def create_styles():
    """Create custom paragraph styles matching HTML/CSS design"""
    styles = getSampleStyleSheet()
    
    # Name - large and bold
    styles.add(ParagraphStyle(
        name='Name',
        parent=styles['Normal'],
        fontSize=24,
        leading=28,
        spaceAfter=4,
        textColor=COLOR_PRIMARY,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT
    ))
    
    # Job title/subtitle
    styles.add(ParagraphStyle(
        name='Subtitle',
        parent=styles['Normal'],
        fontSize=14,
        leading=17,
        spaceAfter=6,
        textColor=COLOR_PRIMARY,
        fontName='Helvetica',
        alignment=TA_LEFT
    ))
    
    # Contact info
    styles.add(ParagraphStyle(
        name='Contact',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        textColor=COLOR_LIGHT_TEXT,
        fontName='Helvetica',
        alignment=TA_LEFT
    ))
    
    # Section headers
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Normal'],
        fontSize=14,
        leading=17,
        spaceBefore=18,
        spaceAfter=10,
        textColor=COLOR_PRIMARY,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT
    ))
    
    # Company/Job title
    styles.add(ParagraphStyle(
        name='CompanyName',
        parent=styles['Normal'],
        fontSize=12,
        leading=15,
        textColor=COLOR_PRIMARY,
        fontName='Helvetica-Bold',
        spaceAfter=2
    ))
    
    # Position
    styles.add(ParagraphStyle(
        name='Position',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        textColor=COLOR_LIGHT_TEXT,
        fontName='Helvetica-Oblique',
        spaceAfter=2
    ))
    
    # Duration text
    styles.add(ParagraphStyle(
        name='Duration',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        fontName='Courier',
        alignment=TA_RIGHT,
        textColor=black
    ))
    
    # Description/bullet points
    styles.add(ParagraphStyle(
        name='Description',
        parent=styles['Normal'],
        fontSize=10.5,
        leading=15,
        spaceBefore=4,
        spaceAfter=4,
        leftIndent=0,
        fontName='Helvetica',
        textColor=HexColor('#444444'),
        alignment=TA_JUSTIFY
    ))
    
    # Skill label
    styles.add(ParagraphStyle(
        name='SkillLabel',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        fontName='Helvetica-Bold',
        textColor=COLOR_PRIMARY
    ))
    
    # Skill items
    styles.add(ParagraphStyle(
        name='SkillItems',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        fontName='Helvetica',
        textColor=COLOR_LIGHT_TEXT
    ))
    
    return styles

def build_header(story, styles, data):
    """Build the header section matching HTML/CSS design"""
    personal = data['personal']
    
    # Name - large and prominent
    story.append(Paragraph(personal['name'], styles['Name']))
    
    # Title/subtitle
    story.append(Paragraph(personal['title'], styles['Subtitle']))
    
    # Contact info in two-column layout
    contact_data = [
        [
            Paragraph(personal['email'], styles['Contact']),
            Paragraph(personal['phone'], styles['Contact'])
        ],
        [
            Paragraph(personal['linkedin'], styles['Contact']),
            Paragraph(personal['github'], styles['Contact'])
        ]
    ]
    
    contact_table = Table(contact_data, colWidths=[3.5*inch, 2.5*inch])
    contact_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (-1, -1), COLOR_LIGHT_TEXT),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    
    story.append(contact_table)
    story.append(Spacer(1, 15))
    
    # Add horizontal divider line
    story.append(HRFlowable(width="100%", thickness=2, lineCap='round', 
                           color=COLOR_PRIMARY, spaceAfter=4))

def build_experience(story, styles, data):
    """Build experience section with improved formatting"""
    # Section header with underline
    story.append(Paragraph("EXPERIENCE", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_BORDER, 
                           spaceBefore=0, spaceAfter=10))
    
    for idx, job in enumerate(data['experience']):
        # Job header: company and duration
        job_header = Table(
            [[
                Paragraph(f"<b>{job['company']}</b>", styles['CompanyName']),
                Paragraph(job['duration'], styles['Duration'])
            ]],
            colWidths=[4.2*inch, 2*inch]
        )
        job_header.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ]))
        story.append(job_header)
        
        # Position and duration detail
        position_row = Table(
            [[
                Paragraph(f"<i>{job['position']}</i>", styles['Position']),
                Paragraph(job['duration_detail'], styles['Duration'])
            ]],
            colWidths=[4.2*inch, 2*inch]
        )
        position_row.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(position_row)
        
        # Job descriptions with bullets
        for desc in job['description']:
            bullet_text = f"• {desc}"
            story.append(Paragraph(bullet_text, styles['Description']))
        
        # Add space between jobs
        if idx < len(data['experience']) - 1:
            story.append(Spacer(1, 12))
        else:
            story.append(Spacer(1, 6))

def build_achievements(story, styles, data):
    """Build key achievements section"""
    story.append(Paragraph("KEY ACHIEVEMENTS", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_BORDER,
                           spaceBefore=0, spaceAfter=10))
    
    for achievement in data['achievements']:
        # Achievement in table format
        ach_content = f"<b>{achievement['title']}</b><br/>{achievement['details']}"
        ach_table = Table(
            [[
                Paragraph(ach_content, styles['Description']),
                Paragraph(achievement['year'], styles['Duration'])
            ]],
            colWidths=[4.8*inch, 1.4*inch]
        )
        ach_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))
        
        story.append(ach_table)

def build_skills_and_education(story, styles, data):
    """Build technical skills and education sections"""
    
    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_BORDER,
                           spaceBefore=0, spaceAfter=10))
    
    # Skills as formatted list
    for category, skills in data['skills'].items():
        skill_row = Table(
            [[
                Paragraph(f"<b>{category}:</b>", styles['SkillLabel']),
                Paragraph(skills, styles['SkillItems'])
            ]],
            colWidths=[1.4*inch, 4.8*inch]
        )
        skill_row.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(skill_row)
    
    story.append(Spacer(1, 12))
    
    # Education
    story.append(Paragraph("EDUCATION", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_BORDER,
                           spaceBefore=0, spaceAfter=10))
    
    for edu in data['education']:
        edu_header = Table(
            [[
                Paragraph(f"<b>{edu['degree']}</b>", styles['CompanyName']),
                Paragraph(edu['duration'], styles['Duration'])
            ]],
            colWidths=[4.2*inch, 2*inch]
        )
        edu_header.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ]))
        story.append(edu_header)
        
        story.append(Paragraph(f"<i>{edu['university']}</i>", styles['Position']))
        story.append(Spacer(1, 8))

def generate_pdf_resume(output_path="resume.pdf"):
    """Generate the professional PDF resume"""
    
    # Create document with custom template
    doc = ResumeTemplate(output_path, pagesize=A4,
                        title="Resume - Pawarit Thareechan",
                        author="Pawarit Thareechan")
    
    # Create styles
    styles = create_styles()
    
    # Build story
    story = []
    
    # Build all sections
    build_header(story, styles, RESUME_DATA)
    build_experience(story, styles, RESUME_DATA)
    build_achievements(story, styles, RESUME_DATA)
    build_skills_and_education(story, styles, RESUME_DATA)
    
    # Build PDF
    doc.build(story)
    print(f"PDF resume generated: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_pdf_resume()