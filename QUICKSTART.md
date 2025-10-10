# Quick Start Guide

## 🚀 How to Run Your Python PDF Resume

### Step 1: Make sure Python packages are installed
The packages should already be installed, but if you need to reinstall:
```bash
pip install -r requirements.txt
```

### Step 2: Run the application

#### Windows (Easiest):
Double-click: `start_resume.bat`

#### Or use PowerShell/Command Prompt:
```bash
python run_resume.py
```

### Step 3: Access your resume
Once the server starts, open your browser to:
```
http://127.0.0.1:5000
```

## 📝 What Happens

1. **PDF Generation**: A professional PDF resume is generated from your data
2. **Image Conversion**: The PDF is converted to high-quality PNG images
3. **Web Server**: A Flask web server starts showing your resume
4. **Ready to Use**: View, print, or download your resume!

## 🎨 Customizing Your Resume

### Update Content
Edit `resume_data.py` and change:
- Personal info (name, email, phone)
- Work experience
- Skills
- Education
- Achievements

After editing, just reload the page or click "Regenerate PDF"

### Change Styling
Edit `pdf_generator.py` to modify:
- Font sizes
- Colors
- Layout
- Spacing
- Section order

## 🖨️ Printing Your Resume

Two ways to get a perfect print:

### Method 1: From the Web Interface
1. Open http://127.0.0.1:5000
2. Click the "🖨️ Print Resume" button
3. Use browser print dialog
4. Select "Save as PDF" or print to your printer

### Method 2: Direct PDF
1. Open http://127.0.0.1:5000
2. Click "📥 Download PDF"
3. Open the downloaded PDF
4. Print from your PDF viewer

## 📂 Generated Files

After running, you'll find:
- `resume.pdf` - Your professional resume PDF
- `static/resume_page_1.png` - First page as image
- `static/resume_page_2.png` - Second page as image (if applicable)

## 🔄 Updating Your Resume

1. Edit `resume_data.py` with your changes
2. Visit http://127.0.0.1:5000/regenerate
3. Or restart the application

## ⚠️ Troubleshooting

### PDF images not showing?
You need poppler-utils for PDF-to-image conversion:
- Download: https://github.com/oschwartz10612/poppler-windows/releases/
- Extract and add to your PATH
- Or just use the PDF directly - click "Download PDF"

### Port already in use?
Edit `run_resume.py` and change the port number:
```python
run_web_server(host='127.0.0.1', port=5001, debug=False)
```

### Python not found?
Make sure Python is installed and in your PATH:
```bash
python --version
```

## 💡 Tips

1. **Keep Data Updated**: Edit `resume_data.py` regularly
2. **Test Print**: Always test print before important submissions
3. **PDF is Primary**: The PDF is the source of truth, images are for web viewing
4. **Backup**: Keep your `resume_data.py` backed up
5. **Version Control**: This is already in git, so all changes are tracked!

## 🎯 Next Steps

1. Update `resume_data.py` with your actual information
2. Run the application
3. Review the output
4. Adjust styling in `pdf_generator.py` if needed
5. Generate your final PDF

Enjoy your professional PDF resume! 🎉
