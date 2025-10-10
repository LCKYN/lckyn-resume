"""
PDF Generator using wkhtmltopdf
Converts the existing index.html website to PDF
"""

import os
import subprocess
import sys


def check_wkhtmltopdf_installed():
    """Check if wkhtmltopdf is installed and available"""
    try:
        result = subprocess.run(
            ["wkhtmltopdf", "--version"], capture_output=True, text=True, check=False
        )
        if result.returncode == 0:
            print(f"✅ wkhtmltopdf found: {result.stdout.split()[1]}")
            return True
        else:
            return False
    except FileNotFoundError:
        return False


def install_instructions():
    """Print installation instructions for wkhtmltopdf"""
    print("\n❌ wkhtmltopdf is not installed!")
    print("\n📥 Installation Instructions:")
    print("\n   Windows:")
    print("   1. Download from: https://wkhtmltopdf.org/downloads.html")
    print("   2. Install the Windows installer (64-bit recommended)")
    print("   3. Add to PATH or use full path to wkhtmltopdf.exe")
    print("\n   Alternative (using Chocolatey):")
    print("   choco install wkhtmltopdf")
    print("\n   Alternative (using winget):")
    print("   winget install wkhtmltopdf")
    print()


def generate_pdf_from_html(
    html_file="index.html", output_file="resume_wkhtmltopdf.pdf", options=None
):
    """
    Generate PDF from HTML file using wkhtmltopdf

    Args:
        html_file: Path to HTML file
        output_file: Output PDF filename
        options: Additional wkhtmltopdf options (list of strings)
    """
    if not check_wkhtmltopdf_installed():
        install_instructions()
        return False

    # Default options for good PDF output
    default_options = [
        "--page-size",
        "A4",
        "--margin-top",
        "0.5in",
        "--margin-bottom",
        "0.5in",
        "--margin-left",
        "0.5in",
        "--margin-right",
        "0.5in",
        "--enable-local-file-access",
        "--print-media-type",
        "--enable-javascript",
        "--javascript-delay",
        "2000",  # Wait 2 seconds for JS to execute
        "--no-stop-slow-scripts",
        "--debug-javascript",  # Show JS errors
    ]

    if options:
        default_options.extend(options)

    # Build command
    cmd = ["wkhtmltopdf"] + default_options + [html_file, output_file]

    print(f"\n🎨 Generating PDF from {html_file}...")
    print(f"   Command: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)

        if result.returncode == 0:
            file_size = os.path.getsize(output_file)
            print(f"✅ PDF generated successfully: {output_file}")
            print(f"📊 File size: {file_size:,} bytes")
            print("\n✨ Features:")
            print("   ✓ Rendered directly from HTML/CSS")
            print("   ✓ High-quality output")
            print("   ✓ Preserves web styling")
            print("   ✓ Professional print layout")
            return True
        else:
            print(f"❌ Error generating PDF:")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Main function"""
    print("=== wkhtmltopdf Resume Generator ===")
    print("Converting HTML to PDF using wkhtmltopdf\n")

    # Create static HTML first
    print("📝 Creating static HTML from resume data...")
    try:
        from create_static_html import create_static_html

        html_file = create_static_html()
    except Exception as e:
        print(f"⚠️  Could not create static HTML: {e}")
        print("   Falling back to index.html")
        html_file = "index.html"

        # Check if index.html exists
        if not os.path.exists(html_file):
            print("❌ index.html not found!")
            print("   Make sure you're running this from the project root directory.")
            sys.exit(1)

    # Generate PDF
    success = generate_pdf_from_html(
        html_file=html_file, output_file="resume_wkhtmltopdf.pdf"
    )

    if success:
        print(f"\n✅ Done! Open resume_wkhtmltopdf.pdf to view your resume.")
    else:
        print("\n❌ Failed to generate PDF. Please check the errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
