# PDF Resume Generator & Web Renderer

A professional resume generator that creates high-quality PDF resumes using Python and ReportLab, then renders them as web-viewable images for perfect print consistency.

## Features

- **📄 Professional PDF Generation**: Creates beautifully formatted PDF resumes using ReportLab
- **🖼️ Web Image Rendering**: Converts PDF to high-quality images for web display
- **🌐 Modern Web Interface**: Responsive Flask-based web app with print optimization
- **📱 Mobile Friendly**: Responsive design that works on all devices
- **🖨️ Print Perfect**: Exact PDF rendering ensures WYSIWYG printing
- **⬇️ PDF Download**: Direct PDF download functionality
- **🔄 Auto Regeneration**: Easy content updates and regeneration

## Quick Start

### Option 1: Double-click to run (Windows)
```bash
# Just double-click this file:
start_resume.bat
```

### Option 2: Python command line
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python run_resume.py
```

### Option 3: Individual components
```bash
# Generate PDF only
python pdf_generator.py

# Start web server only
python web_renderer.py
```

## What You Get

1. **High-Quality PDF**: Professional resume in PDF format with exact typography
2. **Web Version**: Modern web interface showing the exact PDF content
3. **Print Ready**: Perfect printing from both PDF and web versions
4. **Mobile Optimized**: Works great on phones and tablets

## File Structure

```
├── resume_data.py          # Resume content and data structure
├── pdf_generator.py        # PDF generation using ReportLab
├── web_renderer.py         # Flask web app and PDF-to-image conversion
├── run_resume.py          # Main application launcher
├── start_resume.bat       # Windows batch file launcher
├── requirements.txt       # Python dependencies
└── static/               # Generated images (auto-created)
    ├── resume_page_1.png
    └── resume_page_2.png
```

## Technologies Used

- **ReportLab**: Professional PDF generation
- **Flask**: Web application framework
- **pdf2image**: PDF to image conversion
- **Pillow**: Image processing
- **Jinja2**: Template rendering

## Customization

### Update Resume Content
Edit `resume_data.py` to modify:
- Personal information
- Work experience
- Skills
- Education
- Achievements

### Modify PDF Layout
Edit `pdf_generator.py` to change:
- Typography and fonts
- Colors and styling
- Page layout
- Section organization

### Customize Web Interface
Edit `web_renderer.py` to modify:
- Web design and styling
- Responsive behavior
- Print optimization

## Requirements

- Python 3.8+
- Windows/macOS/Linux
- For PDF-to-image conversion: poppler-utils
  - Windows: Download from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases/)
  - macOS: `brew install poppler`
  - Linux: `apt-get install poppler-utils`

## Advantages Over HTML/CSS Resume

1. **Consistent Rendering**: PDF ensures identical appearance across all devices and browsers
2. **Print Reliability**: No browser print dialog issues or margin problems
3. **Professional Quality**: ReportLab produces publication-quality documents
4. **Exact Control**: Precise typography, spacing, and layout control
5. **Universal Compatibility**: PDF works everywhere, no font or CSS compatibility issues

## Support

If you encounter any issues:

1. **PDF Generation Fails**: Check that all required packages are installed
2. **Image Conversion Fails**: Install poppler-utils for your operating system
3. **Web Server Issues**: Ensure Flask is properly installed
4. **Port Conflicts**: The app runs on port 5000 by default

## License

This project is open source and available under the MIT License.