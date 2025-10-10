# wkhtmltopdf Implementation Branch

This branch uses **wkhtmltopdf** to generate PDFs directly from your HTML/CSS website files (`index.html`, `styles.css`, `script.js`).

## Why wkhtmltopdf?

- ✅ **Renders your actual website** - Uses your existing HTML/CSS/JS files
- ✅ **High quality output** - WebKit rendering engine (same as Safari/Chrome)
- ✅ **No code duplication** - Single source of truth for your resume design
- ✅ **Easy maintenance** - Update HTML once, PDF auto-updates

## Installation

### Windows

**Option 1: Manual Download (Recommended)**
1. Download from: https://wkhtmltopdf.org/downloads.html
2. Choose "Windows (MSVC 2015) 64-bit" installer
3. Run the installer
4. Add to PATH or note the installation directory (usually `C:\Program Files\wkhtmltopdf\bin`)

**Option 2: Chocolatey**
```powershell
choco install wkhtmltopdf
```

### Verify Installation

```powershell
wkhtmltopdf --version
```

You should see output like:
```
wkhtmltopdf 0.12.6
```

## Usage

### Generate PDF from HTML

```powershell
python wkhtmltopdf_generator.py
```

This will:
1. Read your `index.html` file
2. Convert it to `resume_wkhtmltopdf.pdf`
3. Apply print-optimized settings (0.5in margins, A4 size)

### Output

- **File**: `resume_wkhtmltopdf.pdf`
- **Quality**: High-quality WebKit rendering
- **Size**: Varies based on content (typically 50-200KB)

## Features

The generator includes optimized settings:
- A4 page size
- 0.5 inch margins (top, bottom, left, right)
- Print media type CSS
- Local file access for styles and scripts

## Comparison with Other Methods

| Method | Quality | Maintenance | Dependencies |
|--------|---------|-------------|--------------|
| **wkhtmltopdf** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | External binary |
| xhtml2pdf | ⭐⭐⭐ | ⭐⭐⭐ | Python only |
| ReportLab | ⭐⭐ | ⭐ | Python only |
| WeasyPrint | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Complex (GTK) |

## Files

- **wkhtmltopdf_generator.py** - PDF generator script
- **index.html** - Your resume website (source file)
- **styles.css** - Styling including print-specific CSS
- **script.js** - JavaScript functionality

## Troubleshooting

### "wkhtmltopdf is not installed"
- Install wkhtmltopdf following instructions above
- Make sure it's in your PATH or provide full path

### "Error generating PDF"
- Check that `index.html` exists in the current directory
- Verify all CSS/JS files are properly linked
- Ensure print media queries are defined in `styles.css`

### PDF looks different from website
- Check `@media print` CSS rules in `styles.css`
- Add `--print-media-type` flag (already included in script)
- Test in browser print preview first

## Next Steps

1. Install wkhtmltopdf
2. Run `python wkhtmltopdf_generator.py`
3. Check `resume_wkhtmltopdf.pdf`
4. Adjust `styles.css` print media queries if needed
5. Commit and push changes

## GitHub Pages

Your website will continue to work on GitHub Pages from `index.html`. The PDF generation is separate and doesn't affect the live site.
