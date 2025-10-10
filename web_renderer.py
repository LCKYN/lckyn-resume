"""
Web renderer for PDF resume - converts PDF to images and creates web interface
"""

import os
from pdf2image import convert_from_path
import base64
from flask import Flask, render_template_string
from pdf_generator import generate_pdf_resume

def pdf_to_images(pdf_path, output_dir="static", dpi=300):
    """Convert PDF to high-quality images"""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # Convert PDF to images
        print(f"Converting PDF to images with DPI {dpi}...")
        images = convert_from_path(pdf_path, dpi=dpi)
        
        image_paths = []
        for i, image in enumerate(images):
            # Save as high-quality PNG
            image_path = os.path.join(output_dir, f"resume_page_{i+1}.png")
            image.save(image_path, "PNG", optimize=True, quality=95)
            image_paths.append(image_path)
            print(f"Generated: {image_path}")
        
        return image_paths
        
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        print("Note: pdf2image requires poppler-utils. Install it from:")
        print("https://github.com/oschwartz10612/poppler-windows/releases/")
        return []

def images_to_base64(image_paths):
    """Convert images to base64 for embedding in HTML"""
    base64_images = []
    
    for image_path in image_paths:
        try:
            with open(image_path, "rb") as img_file:
                img_data = img_file.read()
                base64_data = base64.b64encode(img_data).decode('utf-8')
                base64_images.append(f"data:image/png;base64,{base64_data}")
        except Exception as e:
            print(f"Error converting {image_path} to base64: {e}")
    
    return base64_images

# HTML template for the web resume
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume - Pawarit Thareechan</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
            position: relative;
        }
        
        .header {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            text-align: center;
            padding: 30px;
            position: relative;
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="75" cy="75" r="1" fill="rgba(255,255,255,0.05)"/><circle cx="50" cy="10" r="0.5" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }
        
        .controls {
            background: #f8f9fa;
            padding: 20px;
            border-bottom: 1px solid #e9ecef;
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }
        
        .btn {
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
        }
        
        .btn.print {
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            box-shadow: 0 4px 15px rgba(39, 174, 96, 0.3);
        }
        
        .btn.download {
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            box-shadow: 0 4px 15px rgba(231, 76, 60, 0.3);
        }
        
        .resume-content {
            padding: 0;
        }
        
        .page-image {
            width: 100%;
            height: auto;
            display: block;
            border-bottom: 1px solid #e9ecef;
        }
        
        .page-image:last-child {
            border-bottom: none;
        }
        
        .footer {
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 14px;
        }
        
        .footer a {
            color: #3498db;
            text-decoration: none;
        }
        
        .footer a:hover {
            text-decoration: underline;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            body {
                padding: 10px;
            }
            
            .header h1 {
                font-size: 2em;
            }
            
            .controls {
                flex-direction: column;
                align-items: center;
            }
            
            .btn {
                width: 200px;
                justify-content: center;
            }
        }
        
        /* Print styles */
        @media print {
            body {
                background: white !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            
            .container {
                box-shadow: none !important;
                border-radius: 0 !important;
                max-width: none !important;
            }
            
            .header, .controls, .footer {
                display: none !important;
            }
            
            .page-image {
                break-after: page;
                border: none !important;
                page-break-inside: avoid;
            }
            
            .page-image:last-child {
                break-after: avoid;
            }
        }
        
        /* Loading animation */
        .loading {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
            font-size: 18px;
            color: #666;
        }
        
        .spinner {
            border: 3px solid #f3f3f3;
            border-top: 3px solid #3498db;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin-right: 15px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Pawarit Thareechan</h1>
            <p>Data Scientist | Machine Learning Engineer</p>
        </div>
        
        <div class="controls">
            <button class="btn print" onclick="window.print()">
                🖨️ Print Resume
            </button>
            <a href="/download" class="btn download">
                📥 Download PDF
            </a>
            <a href="/regenerate" class="btn">
                🔄 Regenerate PDF
            </a>
        </div>
        
        <div class="resume-content">
            {% if images %}
                {% for image in images %}
                    <img src="{{ image }}" alt="Resume Page {{ loop.index }}" class="page-image">
                {% endfor %}
            {% else %}
                <div class="loading">
                    <div class="spinner"></div>
                    Loading resume...
                </div>
            {% endif %}
        </div>
        
        <div class="footer">
            <p>Generated with Python & ReportLab | 
            <a href="mailto:T.Pawarit@lckyn.com">T.Pawarit@lckyn.com</a> | 
            <a href="https://linkedin.lckyn.com">LinkedIn</a></p>
        </div>
    </div>
</body>
</html>
"""

# Flask app for serving the resume
app = Flask(__name__)

@app.route('/')
def index():
    """Main resume page"""
    try:
        # Check if images exist, if not generate them
        image_paths = []
        for i in range(1, 5):  # Check up to 4 pages
            img_path = f"static/resume_page_{i}.png"
            if os.path.exists(img_path):
                image_paths.append(img_path)
            else:
                break
        
        if not image_paths:
            # Generate PDF and convert to images
            print("No images found, generating PDF and converting...")
            pdf_path = generate_pdf_resume("resume.pdf")
            image_paths = pdf_to_images(pdf_path)
        
        # Convert to base64 for embedding
        base64_images = images_to_base64(image_paths)
        
        return render_template_string(HTML_TEMPLATE, images=base64_images)
        
    except Exception as e:
        return render_template_string(HTML_TEMPLATE, images=[], error=str(e))

@app.route('/download')
def download_pdf():
    """Download the PDF file"""
    from flask import send_file
    
    pdf_path = "resume.pdf"
    if not os.path.exists(pdf_path):
        generate_pdf_resume(pdf_path)
    
    return send_file(pdf_path, as_attachment=True, download_name="Pawarit_Thareechan_Resume.pdf")

@app.route('/regenerate')
def regenerate():
    """Regenerate the PDF and images"""
    try:
        # Remove existing files
        for file in ["resume.pdf"] + [f"static/resume_page_{i}.png" for i in range(1, 5)]:
            if os.path.exists(file):
                os.remove(file)
        
        # Generate new PDF and images
        pdf_path = generate_pdf_resume("resume.pdf")
        pdf_to_images(pdf_path)
        
        from flask import redirect, url_for
        return redirect(url_for('index'))
        
    except Exception as e:
        return f"Error regenerating: {str(e)}"

def run_web_server(host='127.0.0.1', port=5000, debug=True):
    """Run the Flask web server"""
    print(f"Starting resume web server at http://{host}:{port}")
    print("Features:")
    print("- PDF-rendered resume displayed as images")
    print("- Print-optimized layout")
    print("- PDF download")
    print("- Automatic regeneration")
    
    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    # Generate PDF and start web server
    print("Generating PDF resume...")
    pdf_path = generate_pdf_resume("resume.pdf")
    
    print("Converting PDF to images...")
    image_paths = pdf_to_images(pdf_path)
    
    if image_paths:
        print(f"Successfully generated {len(image_paths)} page(s)")
        run_web_server()
    else:
        print("Failed to generate images. Starting web server anyway...")
        run_web_server()