"""
Presentation Generator for Secure Coding Review
Creates a visual slideshow from screenshots for presentation
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_title_slide():
    """Create title slide for presentation"""
    img = Image.new('RGB', (1920, 1080), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Try to load fonts
    try:
        font_title = ImageFont.truetype("arial.ttf", 72)
        font_subtitle = ImageFont.truetype("arial.ttf", 48)
        font_normal = ImageFont.truetype("arial.ttf", 32)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_normal = ImageFont.load_default()
    
    # Title
    title = "Secure Coding Review"
    subtitle = "Flask Web Application Security Assessment"
    
    # Draw centered text
    draw.text((960, 400), title, fill='#667eea', font=font_title, anchor='mm')
    draw.text((960, 520), subtitle, fill='#ffffff', font=font_subtitle, anchor='mm')
    draw.text((960, 650), "Cybersecurity Internship Project - May 2026", 
              fill='#aaaaaa', font=font_normal, anchor='mm')
    
    return img

def create_section_slide(title, subtitle=""):
    """Create section divider slide"""
    img = Image.new('RGB', (1920, 1080), color='#16213e')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 64)
        font_subtitle = ImageFont.truetype("arial.ttf", 36)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
    
    # Draw title
    draw.text((960, 500), title, fill='#667eea', font=font_title, anchor='mm')
    
    if subtitle:
        draw.text((960, 600), subtitle, fill='#ffffff', font=font_subtitle, anchor='mm')
    
    # Decorative line
    draw.line([(400, 700), (1520, 700)], fill='#667eea', width=4)
    
    return img

def create_vulnerability_slide(title, severity, cwe, description, impact, fix):
    """Create vulnerability detail slide"""
    img = Image.new('RGB', (1920, 1080), color='#0f0f23')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 48)
        font_heading = ImageFont.truetype("arial.ttf", 32)
        font_text = ImageFont.truetype("arial.ttf", 24)
        font_code = ImageFont.truetype("consola.ttf", 20)
    except:
        font_title = ImageFont.load_default()
        font_heading = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_code = ImageFont.load_default()
    
    y = 80
    
    # Title with severity color
    severity_colors = {
        'CRITICAL': '#ff4444',
        'HIGH': '#ff8844',
        'MEDIUM': '#ffaa44',
        'LOW': '#44ff44'
    }
    color = severity_colors.get(severity, '#ffffff')
    
    draw.text((100, y), title, fill=color, font=font_title)
    y += 80
    
    # Severity and CWE
    draw.text((100, y), f"Severity: {severity}  |  CWE: {cwe}", fill='#aaaaaa', font=font_heading)
    y += 70
    
    # Description
    draw.text((100, y), "Description:", fill='#667eea', font=font_heading)
    y += 45
    
    # Wrap description text
    words = description.split()
    line = ""
    for word in words:
        test_line = line + word + " "
        if len(test_line) * 12 > 1700:  # Approximate pixel width
            draw.text((120, y), line, fill='#dddddd', font=font_text)
            y += 35
            line = word + " "
        else:
            line = test_line
    if line:
        draw.text((120, y), line, fill='#dddddd', font=font_text)
    y += 60
    
    # Impact
    draw.text((100, y), "Impact:", fill='#667eea', font=font_heading)
    y += 45
    draw.text((120, y), impact, fill='#ff6666', font=font_text)
    y += 60
    
    # Fix
    draw.text((100, y), "Remediation:", fill='#44ff44', font=font_heading)
    y += 45
    draw.text((120, y), fix, fill='#66ff66', font=font_text)
    
    return img

def create_tools_slide():
    """Create tools used slide"""
    img = Image.new('RGB', (1920, 1080), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 56)
        font_tool = ImageFont.truetype("arial.ttf", 36)
        font_desc = ImageFont.truetype("arial.ttf", 28)
    except:
        font_title = ImageFont.load_default()
        font_tool = ImageFont.load_default()
        font_desc = ImageFont.load_default()
    
    draw.text((960, 100), "Tools & Methodology", fill='#667eea', font=font_title, anchor='mm')
    
    tools = [
        ("Bandit 1.7.5", "Python security linter detecting common security issues"),
        ("Semgrep 1.45.0", "Static analysis engine for pattern-based vulnerability detection"),
        ("Manual Code Review", "Line-by-line analysis of authentication and data handling"),
        ("OWASP Guidelines", "Security standards and best practices framework"),
    ]
    
    y = 250
    for tool, desc in tools:
        # Tool name
        draw.rounded_rectangle([150, y, 1870, y+120], radius=15, fill='#16213e', outline='#667eea', width=2)
        draw.text((180, y+20), tool, fill='#667eea', font=font_tool)
        draw.text((180, y+70), desc, fill='#aaaaaa', font=font_desc)
        y += 150
    
    return img

def create_findings_summary_slide():
    """Create findings summary slide"""
    img = Image.new('RGB', (1920, 1080), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 56)
        font_stat = ImageFont.truetype("arial.ttf", 42)
        font_list = ImageFont.truetype("arial.ttf", 28)
    except:
        font_title = ImageFont.load_default()
        font_stat = ImageFont.load_default()
        font_list = ImageFont.load_default()
    
    draw.text((960, 100), "Vulnerability Summary", fill='#667eea', font=font_title, anchor='mm')
    
    # Statistics boxes
    stats = [
        ("9", "Total Vulnerabilities", '#667eea'),
        ("3", "Critical/High", '#ff4444'),
        ("4", "Medium", '#ffaa44'),
        ("2", "Low", '#44ff44'),
    ]
    
    x = 200
    for number, label, color in stats:
        draw.rounded_rectangle([x, 250, x+380, 450], radius=20, fill='#16213e', outline=color, width=3)
        draw.text((x+190, 320), number, fill=color, font=font_stat, anchor='mm')
        draw.text((x+190, 400), label, fill='#aaaaaa', font=font_list, anchor='mm')
        x += 430
    
    # List vulnerabilities
    vulns = [
        "1. SQL Injection (CWE-89) - CRITICAL",
        "2. Hardcoded Secret Key (CWE-798) - HIGH",
        "3. Debug Mode Enabled (CWE-489) - HIGH",
        "4. Plaintext Password Storage (CWE-256) - HIGH",
        "5. Unsafe File Upload (CWE-434) - MEDIUM",
        "6. Information Disclosure (CWE-200) - MEDIUM",
        "7. Path Traversal (CWE-22) - MEDIUM",
        "8. Verbose Error Messages (CWE-209) - LOW",
        "9. Missing Input Validation (CWE-20) - MEDIUM",
    ]
    
    y = 550
    for vuln in vulns[:5]:
        draw.text((300, y), vuln, fill='#dddddd', font=font_list)
        y += 50
    
    y = 550
    for vuln in vulns[5:]:
        draw.text((1100, y), vuln, fill='#dddddd', font=font_list)
        y += 50
    
    return img

def create_comparison_slide():
    """Create vulnerable vs secure comparison slide"""
    img = Image.new('RGB', (1920, 1080), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 48)
        font_heading = ImageFont.truetype("arial.ttf", 36)
        font_code = ImageFont.truetype("consola.ttf", 22)
    except:
        font_title = ImageFont.load_default()
        font_heading = ImageFont.load_default()
        font_code = ImageFont.load_default()
    
    draw.text((960, 80), "Vulnerable vs. Secure: SQL Injection Fix", 
              fill='#667eea', font=font_title, anchor='mm')
    
    # Vulnerable side
    draw.text((480, 150), "VULNERABLE", fill='#ff4444', font=font_heading, anchor='mm')
    draw.rounded_rectangle([100, 200, 860, 550], radius=15, fill='#3c1e1e', outline='#ff4444', width=3)
    
    vulnerable_code = [
        "# String concatenation - DANGEROUS",
        "query = f\"SELECT * FROM users WHERE",
        "           username = '{username}' AND",
        "           password = '{password}'\"",
        "cursor.execute(query)  # SQL INJECTION!"
    ]
    
    y = 250
    for line in vulnerable_code:
        draw.text((130, y), line, fill='#ff8888', font=font_code)
        y += 50
    
    # Secure side
    draw.text((1440, 150), "SECURE", fill='#44ff44', font=font_heading, anchor='mm')
    draw.rounded_rectangle([1060, 200, 1820, 550], radius=15, fill='#1e3c1e', outline='#44ff44', width=3)
    
    secure_code = [
        "# Parameterized query - SAFE",
        "cursor.execute(",
        "    'SELECT * FROM users WHERE",
        "    username = ? AND password = ?',",
        "    (username, password)",
        ")  # No injection possible"
    ]
    
    y = 250
    for line in secure_code:
        draw.text((1090, y), line, fill='#66ff66', font=font_code)
        y += 50
    
    # Key points
    draw.text((960, 650), "Key Improvements", fill='#ffffff', font=font_heading, anchor='mm')
    
    improvements = [
        "✓ User input treated as data, not executable code",
        "✓ Database driver handles proper escaping automatically",
        "✓ Attack payload treated as literal string (not code)",
        "✓ Authentication bypass impossible with parameterized queries"
    ]
    
    y = 720
    for improvement in improvements:
        draw.text((400, y), improvement, fill='#aaaaaa', font=font_code)
        y += 60
    
    return img

def create_best_practices_slide():
    """Create secure coding best practices slide"""
    img = Image.new('RGB', (1920, 1080), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 48)
        font_practice = ImageFont.truetype("arial.ttf", 32)
    except:
        font_title = ImageFont.load_default()
        font_practice = ImageFont.load_default()
    
    draw.text((960, 80), "Secure Coding Best Practices", 
              fill='#667eea', font=font_title, anchor='mm')
    
    practices = [
        ("1. Input Validation", "Never trust user input - validate type, length, format"),
        ("2. Parameterized Queries", "Always use ? placeholders, never string concatenation"),
        ("3. Password Hashing", "Use adaptive hashing (PBKDF2, bcrypt) - never plaintext"),
        ("4. Secret Management", "Load from environment - never hardcode in source"),
        ("5. Debug Mode", "Always disabled in production environments"),
        ("6. File Uploads", "Validate extensions, use secure_filename(), check MIME types"),
        ("7. Error Handling", "Generic messages to users, detailed logs internally"),
        ("8. Session Security", "HttpOnly, Secure, SameSite cookie attributes"),
    ]
    
    y = 180
    for title, desc in practices:
        draw.rounded_rectangle([100, y, 1820, y+90], radius=10, fill='#16213e', outline='#667eea', width=1)
        draw.text((130, y+15), title, fill='#667eea', font=font_practice)
        draw.text((130, y+50), desc, fill='#aaaaaa', font=font_practice)
        y += 105
    
    return img

def create_conclusion_slide():
    """Create conclusion slide"""
    img = Image.new('RGB', (1920, 1080), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 56)
        font_heading = ImageFont.truetype("arial.ttf", 40)
        font_text = ImageFont.truetype("arial.ttf", 32)
    except:
        font_title = ImageFont.load_default()
        font_heading = ImageFont.load_default()
        font_text = ImageFont.load_default()
    
    draw.text((960, 250), "Project Complete", fill='#667eea', font=font_title, anchor='mm')
    
    outcomes = [
        "9 Vulnerabilities Identified",
        "Automated + Manual Analysis Completed",
        "Fully Remediated Secure Version Created",
        "Professional Documentation Generated",
        "Industry Best Practices Implemented"
    ]
    
    y = 400
    for outcome in outcomes:
        draw.text((960, y), f"✓ {outcome}", fill='#ffffff', font=font_text, anchor='mm')
        y += 70
    
    draw.text((960, 850), "Thank You for Reviewing", fill='#aaaaaa', font=font_heading, anchor='mm')
    draw.text((960, 920), "Cybersecurity Internship - Task 3", fill='#667eea', font=font_text, anchor='mm')
    
    return img

def main():
    """Generate all presentation slides"""
    output_dir = "presentation_slides"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating presentation slides...")
    
    slides = [
        ("01_title.png", create_title_slide, "Title Slide"),
        ("02_overview.png", lambda: create_section_slide("Project Overview", "Flask Security Assessment"), "Overview"),
        ("03_tools.png", create_tools_slide, "Tools Used"),
        ("04_findings.png", create_findings_summary_slide, "Vulnerability Summary"),
        
        # Vulnerability detail slides
        ("05_vuln_sql.png", lambda: create_vulnerability_slide(
            "SQL Injection (CWE-89)", "CRITICAL", "CWE-89",
            "Application constructs SQL queries by directly concatenating user input into query strings, allowing attackers to inject malicious SQL syntax.",
            "Complete authentication bypass, database compromise, data exfiltration",
            "Use parameterized queries with ? placeholders instead of string concatenation"
        ), "SQL Injection"),
        
        ("06_vuln_secret.png", lambda: create_vulnerability_slide(
            "Hardcoded Secret Key (CWE-798)", "HIGH", "CWE-798",
            "Flask secret key is hardcoded in source code, enabling session forgery by anyone with code access.",
            "Session hijacking, authentication bypass, privilege escalation",
            "Load secret from environment variables: os.environ.get('SECRET_KEY')"
        ), "Hardcoded Secret"),
        
        ("07_vuln_debug.png", lambda: create_vulnerability_slide(
            "Debug Mode Enabled (CWE-489)", "HIGH", "CWE-489",
            "Flask runs with debug=True, exposing interactive debugger and detailed error pages.",
            "Remote code execution, information disclosure via stack traces",
            "Set app.debug = False in production configuration"
        ), "Debug Mode"),
        
        ("08_vuln_passwords.png", lambda: create_vulnerability_slide(
            "Plaintext Password Storage (CWE-256)", "HIGH", "CWE-256",
            "User passwords stored in plaintext without hashing or encryption.",
            "Immediate credential exposure if database compromised, compliance violations",
            "Use werkzeug.security.generate_password_hash() with PBKDF2 or bcrypt"
        ), "Plaintext Passwords"),
        
        ("09_comparison.png", create_comparison_slide, "Before/After Comparison"),
        ("10_best_practices.png", create_best_practices_slide, "Best Practices"),
        ("11_conclusion.png", create_conclusion_slide, "Conclusion"),
    ]
    
    generated = []
    for filename, func, description in slides:
        try:
            img = func()
            filepath = os.path.join(output_dir, filename)
            img.save(filepath, 'PNG')
            generated.append((filename, description))
            print(f"  ✓ Generated: {filename} - {description}")
        except Exception as e:
            print(f"  ✗ Failed: {filename} - {str(e)}")
    
    print(f"\n{'='*60}")
    print(f"PRESENTATION GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"\nTotal slides generated: {len(generated)}")
    print(f"Output directory: {output_dir}/")
    print(f"\nSlides created:")
    for filename, desc in generated:
        print(f"  - {filename}: {desc}")
    
    print(f"\nUsage Options:")
    print(f"  1. Present slides directly using image viewer")
    print(f"  2. Import into PowerPoint/Google Slides")
    print(f"  3. Convert to PDF: print slides to PDF")
    print(f"  4. Use as video recording background")
    
    print(f"\nResolution: 1920x1080 (Full HD)")
    print(f"Format: PNG images")
    
    return output_dir

if __name__ == '__main__':
    main()
