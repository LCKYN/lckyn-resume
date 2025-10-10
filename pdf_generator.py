"""
PDF Resume Generator using ReportLab
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib.colors import black, darkblue, gray
from reportlab.lib.enums import TA_RIGHT
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate

from resume_data import RESUME_DATA

class ResumeTemplate(BaseDocTemplate):
    """Custom template for resume with consistent margins"""
    
    def __init__(self, filename, **kwargs):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename, **kwargs)
        
        # Define page margins (0.75 inch all around)
        margin = 0.75 * inch
        frame = Frame(margin, margin, A4[0] - 2*margin, A4[1] - 2*margin,
                     leftPadding=0, bottomPadding=0, rightPadding=0, topPadding=0)
        
        template = PageTemplate(id='resume', frames=frame, onPage=self.add_page_number)
        self.addPageTemplates([template])
    
    def add_page_number(self, canvas, doc):
        """Add page number at bottom"""
        page_num = canvas.getPageNumber()
        if page_num > 1:
            canvas.setFont("Courier", 10)
            canvas.drawCentredString(A4[0]/2, 0.5*inch, f"Page {page_num}")

def create_styles():
    """Create custom paragraph styles"""
    styles = getSampleStyleSheet()
    
    # Header styles
    styles.add(ParagraphStyle(
        name='Name',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=2,
        textColor=darkblue,
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='JobTitle',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=8,
        textColor=darkblue,
        fontName='Helvetica'
    ))
    
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading2'],
        fontSize=11,
        spaceBefore=12,
        spaceAfter=6,
        textColor=darkblue,
        fontName='Helvetica-Bold',
        borderWidth=1,
        borderColor=gray,
        borderPadding=2
    ))
    
    styles.add(ParagraphStyle(
        name='CompanyName',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica-Bold',
        textColor=darkblue,
        spaceAfter=2
    ))
    
    styles.add(ParagraphStyle(
        name='Company',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Helvetica-Oblique',
        spaceAfter=4
    ))
    
    styles.add(ParagraphStyle(
        name='Duration',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Courier',
        alignment=TA_RIGHT,
        textColor=black
    ))
    
    styles.add(ParagraphStyle(
        name='Description',
        parent=styles['Normal'],
        fontSize=9,
        spaceBefore=2,
        spaceAfter=6,
        leftIndent=15,
        fontName='Helvetica'
    ))
    
    styles.add(ParagraphStyle(
        name='Contact',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Helvetica'
    ))
    
    return styles

def build_header(story, styles, data):
    """Build the header section"""
    personal = data['personal']
    
    # Name
    story.append(Paragraph(personal['name'], styles['Name']))
    
    # Title
    story.append(Paragraph(personal['title'], styles['JobTitle']))
    
    # Contact info as table for better layout
    contact_data = [
        [personal['email'], personal['phone']],
        [personal['linkedin'], personal['github']]
    ]
    
    contact_table = Table(contact_data, colWidths=[3*inch, 2*inch])
    contact_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    
    story.append(contact_table)
    story.append(Spacer(1, 8))
    
    # Add horizontal line
    from reportlab.platypus import HRFlowable
    story.append(HRFlowable(width="100%", thickness=2, lineCap='round', color=darkblue))
    story.append(Spacer(1, 4))

def build_experience(story, styles, data):
    """Build experience section"""
    story.append(Paragraph("EXPERIENCE", styles['SectionHeader']))
    
    for job in data['experience']:
        # Job header table
        job_data = [[
            Paragraph(f"<b>{job['company']}</b><br/><i>{job['position']}</i>", styles['Normal']),
            Paragraph(f"{job['duration']}<br/>{job['duration_detail']}", styles['Duration'])
        ]]
        
        job_table = Table(job_data, colWidths=[4*inch, 2*inch])
        job_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica'),
            ('FONTNAME', (1, 0), (1, 0), 'Courier'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        
        story.append(job_table)
        
        # Job descriptions
        for desc in job['description']:
            bullet = f"• {desc}"
            story.append(Paragraph(bullet, styles['Description']))
        
        story.append(Spacer(1, 8))

def build_achievements(story, styles, data):
    """Build key achievements section"""
    story.append(Paragraph("KEY ACHIEVEMENTS", styles['SectionHeader']))
    
    for achievement in data['achievements']:
        # Achievement header
        ach_data = [[
            Paragraph(f"<b>{achievement['title']}</b><br/>{achievement['details']}", styles['Normal']),
            Paragraph(achievement['year'], styles['Duration'])
        ]]
        
        ach_table = Table(ach_data, colWidths=[4.5*inch, 1*inch])
        ach_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica'),
            ('FONTNAME', (1, 0), (1, 0), 'Courier'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        
        story.append(ach_table)

def build_education(story, styles, data):
    """Build education section"""
    story.append(Paragraph("TECHNICAL SKILLS", styles['SectionHeader']))
    
    # Skills as table
    skills_data = []
    for category, skills in data['skills'].items():
        skills_data.append([f"{category}:", skills])
    
    skills_table = Table(skills_data, colWidths=[1.2*inch, 4.3*inch])
    skills_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TEXTCOLOR', (0, 0), (0, -1), darkblue),
    ]))
    
    story.append(skills_table)
    story.append(Spacer(1, 12))
    
    # Education
    story.append(Paragraph("EDUCATION", styles['SectionHeader']))
    
    for edu in data['education']:
        edu_data = [[
            Paragraph(f"<b>{edu['degree']}</b><br/><i>{edu['university']}</i>", styles['Normal']),
            Paragraph(edu['duration'], styles['Duration'])
        ]]
        
        edu_table = Table(edu_data, colWidths=[4*inch, 2*inch])
        edu_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica'),
            ('FONTNAME', (1, 0), (1, 0), 'Courier'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        
        story.append(edu_table)

def generate_pdf_resume(output_path="resume.pdf"):
    """Generate the PDF resume"""
    
    # Create document with custom template
    doc = ResumeTemplate(output_path, pagesize=A4)
    
    # Create styles
    styles = create_styles()
    
    # Build story
    story = []
    
    # Build sections
    build_header(story, styles, RESUME_DATA)
    build_experience(story, styles, RESUME_DATA)
    build_achievements(story, styles, RESUME_DATA)
    build_education(story, styles, RESUME_DATA)
    
    # Build PDF
    doc.build(story)
    print(f"PDF resume generated: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_pdf_resume()