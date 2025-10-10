# Project Structure & Usage Guide

This repository serves two purposes:
1. **GitHub Pages Website** - Live resume website
2. **Python PDF Tools** - PDF generation and processing

## 🌐 GitHub Pages (Primary)

The main resume is live at your GitHub Pages URL and uses these files:

### Core Website Files (Keep These!)
```
index.html      # Main resume page
styles.css      # Styling and print layout
script.js       # Resume content and interactivity
CNAME           # Custom domain (if configured)
accomplishment/ # Additional data folder
```

These files are essential for GitHub Pages to work. Do not delete them!

## 🐍 Python PDF Tools (Optional)

For developers who want to generate PDFs programmatically:

### PDF Generation Files
```
html2pdf_generator.py    # Recommended: HTML-to-PDF converter
pdf_generator.py         # Alternative: ReportLab PDF generator
resume_data.py           # Python resume data structure
```

### Web Application Files
```
web_renderer.py          # Flask web server for PDF viewing
run_resume.py           # Main application launcher
start_resume.bat        # Windows quick-start script
requirements.txt        # Python dependencies
```

### Documentation Files
```
README.md               # Main project README
QUICKSTART.md           # Quick start for Python tools
README_PDF.md           # Detailed PDF documentation
PDF_QUALITY_FIX.md      # PDF quality improvements
IMPROVEMENTS.md         # Improvement changelog
```

## 🧹 Cleanup Guidelines

### Files to Keep
✅ **Essential for GitHub Pages:**
- index.html
- styles.css
- script.js
- CNAME (if using custom domain)
- README.md

✅ **Useful Python Tools:**
- html2pdf_generator.py (recommended PDF generator)
- resume_data.py
- requirements.txt

✅ **Documentation:**
- README.md
- QUICKSTART.md (for Python users)

### Files to Remove/Ignore
❌ **Generated Files (already in .gitignore):**
- *.pdf (all PDF files)
- static/ (generated images)
- __pycache__/ (Python cache)
- .vscode/ (editor config)

❌ **Optional - Can Remove:**
- weasyprint_generator.py (doesn't work on Windows easily)
- pdf_generator.py (replaced by html2pdf_generator.py)
- README_PDF.md (redundant with QUICKSTART.md)
- IMPROVEMENTS.md (changelog, not essential)
- PDF_QUALITY_FIX.md (historical, not needed)

## 🔧 Quick Cleanup

### Remove unnecessary Python generators:
```bash
git rm weasyprint_generator.py
git rm pdf_generator.py
```

### Remove redundant documentation:
```bash
git rm IMPROVEMENTS.md
git rm PDF_QUALITY_FIX.md
git rm README_PDF.md
```

### Keep consolidated docs:
- README.md (main)
- QUICKSTART.md (Python PDF tools)
- This file (project structure)

## ✅ Recommended Final Structure

```
lckyn-resume/
├── 📄 Website (GitHub Pages)
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── CNAME
│
├── 🐍 Python Tools (Optional)
│   ├── html2pdf_generator.py
│   ├── resume_data.py
│   ├── web_renderer.py
│   ├── run_resume.py
│   ├── start_resume.bat
│   └── requirements.txt
│
├── 📚 Documentation
│   ├── README.md
│   ├── QUICKSTART.md
│   └── PROJECT_STRUCTURE.md (this file)
│
└── 🚫 Ignored (.gitignore)
    ├── *.pdf
    ├── static/
    ├── __pycache__/
    └── .vscode/
```

## 🎯 Usage

### View Resume Online
Just visit your GitHub Pages URL - that's it!

### Generate PDF Locally
```bash
pip install -r requirements.txt
python html2pdf_generator.py
```

### Run Web App
```bash
python run_resume.py
# Visit http://127.0.0.1:5000
```

## ⚠️ Important Notes

1. **Don't break GitHub Pages**: Keep index.html, styles.css, and script.js
2. **PDFs are ignored**: .gitignore prevents PDFs from being committed
3. **Python tools are optional**: Website works without them
4. **Clean separation**: Website files vs. Python tools

## 🔄 Updating

### Update Website
Edit `script.js` to change resume content

### Update PDF Generator
Edit `resume_data.py` to change resume content

### Sync Both
Update both files to keep them in sync (they use different formats)