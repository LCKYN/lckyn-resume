"""
Main script to run the PDF resume generator and web server
"""

import sys
from pdf_generator import generate_pdf_resume
from web_renderer import run_web_server, pdf_to_images

def main():
    """Main function to generate PDF and start web server"""
    
    print("=== PDF Resume Generator & Web Renderer ===")
    print()
    
    try:
        # Step 1: Generate PDF
        print("📄 Generating PDF resume...")
        pdf_path = generate_pdf_resume("resume.pdf")
        print(f"✅ PDF generated successfully: {pdf_path}")
        print()
        
        # Step 2: Convert to images  
        print("🖼️  Converting PDF to images...")
        image_paths = pdf_to_images(pdf_path, dpi=300)
        
        if image_paths:
            print(f"✅ Generated {len(image_paths)} image(s)")
            for i, path in enumerate(image_paths, 1):
                print(f"   Page {i}: {path}")
        else:
            print("⚠️  Warning: Could not generate images")
            print("   Note: pdf2image requires poppler-utils")
            print("   Download from: https://github.com/oschwartz10612/poppler-windows/releases/")
            print("   Extract and add to PATH, or use:")
            print("   conda install -c conda-forge poppler")
            
        print()
        
        # Step 3: Start web server
        print("🌐 Starting web server...")
        print("   Features:")
        print("   - High-quality PDF-rendered resume")
        print("   - Print-optimized layout")
        print("   - PDF download")
        print("   - Mobile responsive")
        print()
        
        run_web_server(host='127.0.0.1', port=5000, debug=False)
        
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()