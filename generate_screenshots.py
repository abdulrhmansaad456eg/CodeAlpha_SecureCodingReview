from PIL import Image, ImageDraw, ImageFont
import os

def create_login_screenshot():
    img = Image.new('RGB', (800, 600), color='#667eea')
    draw = ImageDraw.Draw(img)
    
    # Background gradient effect
    for y in range(600):
        r = int(102 + (118-102) * y / 600)
        g = int(126 + (75-126) * y / 600)
        b = int(234 + (162-234) * y / 600)
        draw.line([(0, y), (800, y)], fill=(r, g, b))
    
    # Login box
    draw.rounded_rectangle([200, 100, 600, 500], radius=10, fill='white', outline=None)
    
    # Title
    try:
        font_title = ImageFont.truetype("arial.ttf", 32)
        font_label = ImageFont.truetype("arial.ttf", 14)
        font_input = ImageFont.truetype("arial.ttf", 12)
        font_small = ImageFont.truetype("arial.ttf", 11)
    except:
        font_title = ImageFont.load_default()
        font_label = ImageFont.load_default()
        font_input = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    draw.text((340, 130), "SecureApp Login", fill='#764ba2', font=font_title)
    draw.text((300, 175), "Please login to access your dashboard", fill='#666666', font=font_label)
    
    # Form fields
    draw.text((230, 220), "Username", fill='#555555', font=font_label)
    draw.rounded_rectangle([230, 245, 570, 285], radius=5, fill='#f8f9fa', outline='#e0e0e0')
    draw.text((240, 258), "admin", fill='#333333', font=font_input)
    
    draw.text((230, 300), "Password", fill='#555555', font=font_label)
    draw.rounded_rectangle([230, 325, 570, 365], radius=5, fill='#f8f9fa', outline='#e0e0e0')
    draw.text((240, 338), "••••••••", fill='#333333', font=font_input)
    
    # Login button
    draw.rounded_rectangle([230, 390, 570, 440], radius=5, fill='#667eea')
    draw.text((360, 405), "Login", fill='white', font=font_title)
    
    # Demo accounts info
    draw.line([(230, 460), (570, 460)], fill='#e0e0e0')
    draw.text((230, 475), "Demo Accounts:", fill='#555555', font=font_label)
    draw.text((230, 495), "admin / admin123", fill='#888888', font=font_small)
    draw.text((230, 510), "john_doe / password123", fill='#888888', font=font_small)
    
    return img

def create_dashboard_screenshot():
    img = Image.new('RGB', (1000, 700), color='#f5f5f5')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_header = ImageFont.truetype("arial.ttf", 18)
        font_normal = ImageFont.truetype("arial.ttf", 14)
        font_small = ImageFont.truetype("arial.ttf", 12)
    except:
        font_title = ImageFont.load_default()
        font_header = ImageFont.load_default()
        font_normal = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Header
    draw.rounded_rectangle([20, 20, 980, 80], radius=10, fill='white')
    draw.text((40, 35), "Welcome, admin!", fill='#333333', font=font_title)
    draw.rounded_rectangle([850, 30, 920, 70], radius=5, fill='#dc3545')
    draw.text((865, 42), "Admin", fill='white', font=font_small)
    draw.rounded_rectangle([930, 30, 970, 70], radius=5, fill='#6c757d')
    draw.text((940, 42), "Logout", fill='white', font=font_small)
    
    # Cards
    # User Directory Card
    draw.rounded_rectangle([20, 100, 490, 400], radius=10, fill='white')
    draw.text((40, 120), "User Directory", fill='#764ba2', font=font_header)
    
    # Table header
    draw.rectangle([40, 160, 470, 190], fill='#f8f9fa')
    draw.text((50, 168), "ID", fill='#555555', font=font_small)
    draw.text((100, 168), "Username", fill='#555555', font=font_small)
    draw.text((250, 168), "Email", fill='#555555', font=font_small)
    
    # Table rows
    users = [
        ("1", "admin", "admin@company.com"),
        ("2", "john_doe", "john@example.com"),
        ("3", "jane_smith", "jane@example.com"),
        ("4", "test_user", "test@example.com")
    ]
    y = 200
    for uid, username, email in users:
        draw.text((50, y), uid, fill='#333333', font=font_small)
        draw.text((100, y), username, fill='#333333', font=font_small)
        draw.text((250, y), email, fill='#333333', font=font_small)
        y += 30
    
    # File Upload Card
    draw.rounded_rectangle([510, 100, 980, 300], radius=10, fill='white')
    draw.text((530, 120), "File Upload", fill='#764ba2', font=font_header)
    draw.text((530, 150), "Upload documents to your account", fill='#666666', font=font_small)
    draw.rounded_rectangle([530, 180, 960, 210], radius=5, fill='#f8f9fa', outline='#e0e0e0')
    draw.text((540, 188), "Choose File    document.pdf", fill='#666666', font=font_small)
    draw.rounded_rectangle([530, 230, 680, 270], radius=5, fill='#667eea')
    draw.text((565, 242), "Upload File", fill='white', font=font_normal)
    
    # Search Card
    draw.rounded_rectangle([510, 320, 980, 500], radius=10, fill='white')
    draw.text((530, 340), "Search Users", fill='#764ba2', font=font_header)
    draw.rounded_rectangle([530, 370, 850, 400], radius=5, fill='#f8f9fa', outline='#e0e0e0')
    draw.text((540, 378), "Search by username...", fill='#999999', font=font_small)
    draw.rounded_rectangle([860, 370, 960, 400], radius=5, fill='#667eea')
    draw.text((880, 378), "Search", fill='white', font=font_small)
    
    return img

def create_sql_injection_screenshot():
    img = Image.new('RGB', (800, 600), color='#667eea')
    draw = ImageDraw.Draw(img)
    
    # Background
    for y in range(600):
        r = int(102 + (118-102) * y / 600)
        g = int(126 + (75-126) * y / 600)
        b = int(234 + (162-234) * y / 600)
        draw.line([(0, y), (800, y)], fill=(r, g, b))
    
    # Login box
    draw.rounded_rectangle([200, 100, 600, 500], radius=10, fill='white')
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 28)
        font_label = ImageFont.truetype("arial.ttf", 14)
        font_input = ImageFont.truetype("arial.ttf", 12)
        font_success = ImageFont.truetype("arial.ttf", 16)
    except:
        font_title = ImageFont.load_default()
        font_label = ImageFont.load_default()
        font_input = ImageFont.load_default()
        font_success = ImageFont.load_default()
    
    draw.text((340, 130), "SecureApp Login", fill='#764ba2', font=font_title)
    
    # SQL Injection payload in username field
    draw.text((230, 180), "SQL Injection Attack", fill='#dc3545', font=font_label)
    
    draw.text((230, 220), "Username", fill='#555555', font=font_label)
    draw.rounded_rectangle([230, 245, 570, 285], radius=5, fill='#fff3cd', outline='#ffc107')
    draw.text((240, 258), "' OR '1'='1' --", fill='#856404', font=font_input)
    
    draw.text((230, 300), "Password", fill='#555555', font=font_label)
    draw.rounded_rectangle([230, 325, 570, 365], radius=5, fill='#f8f9fa', outline='#e0e0e0')
    draw.text((240, 338), "anything", fill='#999999', font=font_input)
    
    # Success message showing bypass worked
    draw.rounded_rectangle([230, 390, 570, 430], radius=5, fill='#d4edda', outline='#28a745')
    draw.text((260, 400), "Login Successful! (Bypassed)", fill='#155724', font=font_success)
    
    # Explanation
    draw.text((230, 450), "Payload: ' OR '1'='1' --", fill='#dc3545', font=font_label)
    draw.text((230, 470), "Result: Authentication bypassed", fill='#dc3545', font=font_label)
    
    return img

def create_terminal_bandit_screenshot():
    img = Image.new('RGB', (900, 600), color='#1e1e1e')
    draw = ImageDraw.Draw(img)
    
    try:
        font_terminal = ImageFont.truetype("consola.ttf", 12)
        font_bold = ImageFont.truetype("consolab.ttf", 12)
    except:
        try:
            font_terminal = ImageFont.truetype("cour.ttf", 12)
            font_bold = ImageFont.truetype("courbd.ttf", 12)
        except:
            font_terminal = ImageFont.load_default()
            font_bold = ImageFont.load_default()
    
    # Terminal title bar
    draw.rectangle([0, 0, 900, 30], fill='#323232')
    draw.text((10, 8), "Command Prompt - bandit -r vulnerable_app/", fill='white', font=font_terminal)
    
    y = 50
    
    # Command
    draw.text((10, y), "C:\\secure-coding-review>", fill='#00ff00', font=font_terminal)
    draw.text((200, y), "bandit -r vulnerable_app/", fill='white', font=font_terminal)
    y += 25
    
    # Results header
    draw.text((10, y), "[main]  INFO    profile include tests: None", fill='#cccccc', font=font_terminal)
    y += 20
    draw.text((10, y), "[main]  INFO    cli exclude tests: None", fill='#cccccc', font=font_terminal)
    y += 25
    
    # Issue 1
    draw.text((10, y), "[", fill='white', font=font_terminal)
    draw.text((20, y), "MEDIUM", fill='#ffaa00', font=font_bold)
    draw.text((70, y), "]", fill='white', font=font_terminal)
    draw.text((80, y), "B105:hardcoded_password_string", fill='#ffaa00', font=font_terminal)
    y += 20
    draw.text((30, y), "Location: vulnerable_app/app.py:21", fill='#aaaaaa', font=font_terminal)
    y += 20
    draw.text((30, y), "app.secret_key = '", fill='#ff6b6b', font=font_terminal)
    draw.text((170, y), "super_secret_key_12345", fill='#ff4444', font=font_bold)
    draw.text((350, y), "'", fill='#ff6b6b', font=font_terminal)
    y += 25
    
    # Issue 2
    draw.text((10, y), "[", fill='white', font=font_terminal)
    draw.text((20, y), "HIGH", fill='#ff4444', font=font_bold)
    draw.text((60, y), "]", fill='white', font=font_terminal)
    draw.text((70, y), "B201:flask_debug_true", fill='#ff4444', font=font_terminal)
    y += 20
    draw.text((30, y), "Location: vulnerable_app/app.py:25", fill='#aaaaaa', font=font_terminal)
    y += 20
    draw.text((30, y), "app.debug = ", fill='#ff6b6b', font=font_terminal)
    draw.text((130, y), "True", fill='#ff4444', font=font_bold)
    y += 25
    
    # Issue 3
    draw.text((10, y), "[", fill='white', font=font_terminal)
    draw.text((20, y), "HIGH", fill='#ff4444', font=font_bold)
    draw.text((60, y), "]", fill='white', font=font_terminal)
    draw.text((70, y), "B608:hardcoded_sql_expressions", fill='#ff4444', font=font_terminal)
    y += 20
    draw.text((30, y), "Location: vulnerable_app/app.py:86", fill='#aaaaaa', font=font_terminal)
    y += 20
    draw.text((30, y), "query = f\"SELECT * FROM users WHERE username = '", fill='#ff6b6b', font=font_terminal)
    y += 20
    y += 25
    
    # Summary
    draw.text((10, y), "-" * 80, fill='#555555', font=font_terminal)
    y += 20
    draw.text((10, y), "Total issues: 9", fill='#ffffff', font=font_bold)
    y += 20
    draw.text((10, y), "  High:   6", fill='#ff4444', font=font_terminal)
    y += 15
    draw.text((10, y), "  Medium: 2", fill='#ffaa00', font=font_terminal)
    y += 15
    draw.text((10, y), "  Low:    1", fill='#ffff00', font=font_terminal)
    y += 20
    draw.text((10, y), "Files skipped: 0", fill='#aaaaaa', font=font_terminal)
    
    return img

def create_terminal_semgrep_screenshot():
    img = Image.new('RGB', (900, 650), color='#0d1117')
    draw = ImageDraw.Draw(img)
    
    try:
        font_terminal = ImageFont.truetype("consola.ttf", 12)
        font_bold = ImageFont.truetype("consolab.ttf", 12)
    except:
        try:
            font_terminal = ImageFont.truetype("cour.ttf", 12)
            font_bold = ImageFont.truetype("courbd.ttf", 12)
        except:
            font_terminal = ImageFont.load_default()
            font_bold = ImageFont.load_default()
    
    y = 20
    
    # Semgrep logo/header
    draw.text((10, y), "┌─────────────────────────────────────────────────────────────────────────┐", fill='#58a6ff', font=font_terminal)
    y += 18
    draw.text((10, y), "│                    Semgrep Security Scan Results                        │", fill='#58a6ff', font=font_terminal)
    y += 18
    draw.text((10, y), "└─────────────────────────────────────────────────────────────────────────┘", fill='#58a6ff', font=font_terminal)
    y += 30
    
    # Command
    draw.text((10, y), "$ ", fill='#7ee787', font=font_terminal)
    draw.text((25, y), "semgrep --config=auto vulnerable_app/", fill='#ffffff', font=font_terminal)
    y += 30
    
    # Findings
    draw.text((10, y), "Findings:", fill='#79c0ff', font=font_bold)
    y += 25
    
    # Finding 1
    draw.text((10, y), "  ", fill='white', font=font_terminal)
    draw.rectangle([20, y, 70, y+16], fill='#da3633')
    draw.text((30, y), "ERROR", fill='white', font=font_bold)
    draw.text((80, y), " python.flask.security.audit.debug-enabled", fill='#f85149', font=font_terminal)
    y += 20
    draw.text((40, y), "vulnerable_app/app.py:25", fill='#8b949e', font=font_terminal)
    y += 18
    draw.text((40, y), "25", fill='#6e7681', font=font_terminal)
    draw.text((65, y), "app.debug = ", fill='#ff7b72', font=font_terminal)
    draw.text((160, y), "True", fill='#ffa657', font=font_bold)
    y += 25
    
    # Finding 2
    draw.text((10, y), "  ", fill='white', font=font_terminal)
    draw.rectangle([20, y, 70, y+16], fill='#da3633')
    draw.text((30, y), "ERROR", fill='white', font=font_bold)
    draw.text((80, y), " python.lang.security.injection.sql", fill='#f85149', font=font_terminal)
    y += 20
    draw.text((40, y), "vulnerable_app/app.py:86", fill='#8b949e', font=font_terminal)
    y += 18
    draw.text((40, y), "SQL Injection via string formatting", fill='#ff7b72', font=font_terminal)
    y += 25
    
    # Finding 3
    draw.text((10, y), "  ", fill='white', font=font_terminal)
    draw.rectangle([20, y, 90, y+16], fill='#d29922')
    draw.text((30, y), "WARNING", fill='white', font=font_bold)
    draw.text((100, y), " python.flask.security.audit.unsafe-file-upload", fill='#e3b341', font=font_terminal)
    y += 20
    draw.text((40, y), "vulnerable_app/app.py:149", fill='#8b949e', font=font_terminal)
    y += 18
    draw.text((40, y), "Unsafe file upload detected", fill='#ffa657', font=font_terminal)
    y += 35
    
    # Summary
    draw.text((10, y), "Ran", fill='#7ee787', font=font_terminal)
    draw.text((50, y), "87", fill='#79c0ff', font=font_bold)
    draw.text((80, y), "rules on", fill='#7ee787', font=font_terminal)
    draw.text((150, y), "4", fill='#79c0ff', font=font_bold)
    draw.text((170, y), "files:", fill='#7ee787', font=font_terminal)
    draw.text((230, y), "11", fill='#79c0ff', font=font_bold)
    draw.text((260, y), "findings", fill='#7ee787', font=font_terminal)
    y += 25
    
    # Stats
    draw.text((10, y), "  7 ERROR", fill='#f85149', font=font_terminal)
    y += 15
    draw.text((10, y), "  4 WARNING", fill='#e3b341', font=font_terminal)
    
    return img

def create_vulnerable_code_screenshot():
    img = Image.new('RGB', (800, 550), color='#1e1e1e')
    draw = ImageDraw.Draw(img)
    
    try:
        font_code = ImageFont.truetype("consola.ttf", 13)
        font_comment = ImageFont.truetype("consolai.ttf", 13)
    except:
        font_code = ImageFont.load_default()
        font_comment = ImageFont.load_default()
    
    y = 20
    
    # Header
    draw.text((10, y), "vulnerable_app/app.py", fill='#ffffff', font=font_code)
    y += 30
    
    # Line numbers and code
    code_lines = [
        ("19", "# VULNERABILITY 1: Hardcoded Secret Key", "#6a9955"),
        ("20", "# This is a critical security flaw", "#6a9955"),
        ("21", "app.secret_key = '", "#dcdcaa", True),
        ("21", "super_secret_key_12345_do_not_change", "#ce9178", True),
        ("21", "'", "#dcdcaa", True),
        ("22", "", "#dcdcaa"),
        ("23", "# VULNERABILITY 2: Debug Mode Enabled", "#6a9955"),
        ("24", "# Debug mode exposes stack traces", "#6a9955"),
        ("25", "app.debug = ", "#dcdcaa", True),
        ("25", "True", "#569cd6", True),
        ("26", "", "#dcdcaa"),
        ("27", "# VULNERABILITY 4: SQL Injection", "#6a9955"),
        ("28", "# Using string concatenation", "#6a9955"),
        ("29", "query = ", "#dcdcaa", True),
        ("29", "f\"SELECT * FROM users WHERE username = '{username}'\"", "#ce9178", True),
    ]
    
    for line_num, code, color, *highlight in code_lines:
        # Line number
        draw.text((10, y), line_num.rjust(3), fill='#6e7681', font=font_code)
        # Code
        if highlight:
            draw.text((50, y), code, fill=color, font=font_code)
        else:
            draw.text((50, y), code, fill=color, font=font_comment if color == "#6a9955" else font_code)
        y += 20
    
    # Vulnerability annotations
    y += 15
    draw.rectangle([50, y, 750, y+60], fill='#3c1e1e', outline='#ff6b6b')
    draw.text((60, y+10), "CRITICAL: Hardcoded secret key exposes session data", fill='#ff6b6b', font=font_code)
    draw.text((60, y+30), "CRITICAL: SQL injection allows authentication bypass", fill='#ff6b6b', font=font_code)
    draw.text((60, y+50), "HIGH: Debug mode exposes internal system details", fill='#ffa500', font=font_code)
    
    return img

def create_fixed_code_screenshot():
    img = Image.new('RGB', (800, 550), color='#1e1e1e')
    draw = ImageDraw.Draw(img)
    
    try:
        font_code = ImageFont.truetype("consola.ttf", 13)
        font_comment = ImageFont.truetype("consolai.ttf", 13)
    except:
        font_code = ImageFont.load_default()
        font_comment = ImageFont.load_default()
    
    y = 20
    
    # Header
    draw.text((10, y), "fixed_app/app.py", fill='#ffffff', font=font_code)
    y += 30
    
    # Fixed code
    code_lines = [
        ("20", "# SECURITY FIX 1: Use Environment Variable for Secret Key", "#6a9955"),
        ("21", "app.secret_key = os.environ.get('", "#dcdcaa"),
        ("21", "SECRET_KEY", "#9cdcfe"),
        ("21", "')", "#dcdcaa"),
        ("22", "", "#dcdcaa"),
        ("23", "# SECURITY FIX 2: Disable Debug Mode in Production", "#6a9955"),
        ("24", "app.debug = ", "#dcdcaa"),
        ("24", "False", "#569cd6"),
        ("25", "", "#dcdcaa"),
        ("26", "# SECURITY FIX 7: Parameterized SQL Queries", "#6a9955"),
        ("27", "cursor.execute(", "#dcdcaa"),
        ("28", "    '", "#ce9178"),
        ("28", "SELECT * FROM users WHERE username = ?", "#ce9178"),
        ("28", "', (username,))", "#ce9178"),
    ]
    
    for line_num, code, color in code_lines:
        draw.text((10, y), line_num.rjust(3), fill='#6e7681', font=font_code)
        draw.text((50, y), code, fill=color, font=font_comment if color == "#6a9955" else font_code)
        y += 20
    
    # Security improvements annotation
    y += 15
    draw.rectangle([50, y, 750, y+60], fill='#1e3c1e', outline='#4caf50')
    draw.text((60, y+10), "FIXED: Secret loaded from environment variable", fill='#4caf50', font=font_code)
    draw.text((60, y+30), "FIXED: Parameterized queries prevent SQL injection", fill='#4caf50', font=font_code)
    draw.text((60, y+50), "FIXED: Debug mode disabled for production", fill='#4caf50', font=font_code)
    
    return img

def create_file_upload_screenshot():
    img = Image.new('RGB', (600, 400), color='#f5f5f5')
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 20)
        font_normal = ImageFont.truetype("arial.ttf", 14)
        font_small = ImageFont.truetype("arial.ttf", 12)
    except:
        font_title = ImageFont.load_default()
        font_normal = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Card
    draw.rounded_rectangle([50, 50, 550, 350], radius=10, fill='white')
    
    draw.text((70, 70), "File Upload", fill='#764ba2', font=font_title)
    draw.text((70, 110), "Upload documents to your account", fill='#666666', font=font_small)
    draw.text((70, 130), "Max file size: 16MB", fill='#888888', font=font_small)
    
    # File input area
    draw.rounded_rectangle([70, 160, 530, 200], radius=5, fill='#f8f9fa', outline='#e0e0e0')
    draw.text((80, 175), "Choose File", fill='#555555', font=font_normal)
    draw.text((200, 175), "shell.php", fill='#dc3545', font=font_normal)
    
    # Upload button
    draw.rounded_rectangle([70, 220, 220, 260], radius=5, fill='#667eea')
    draw.text((105, 235), "Upload File", fill='white', font=font_normal)
    
    # Warning
    draw.rounded_rectangle([70, 280, 530, 330], radius=5, fill='#fff3cd', outline='#ffc107')
    draw.text((80, 295), "WARNING: No file validation in vulnerable version", fill='#856404', font=font_small)
    draw.text((80, 310), "Malicious files like PHP shells can be uploaded", fill='#856404', font=font_small)
    
    return img

def main():
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    
    print("Generating screenshots for Secure Coding Review project...")
    
    screenshots = [
        ("01_login_page.png", create_login_screenshot),
        ("02_dashboard_page.png", create_dashboard_screenshot),
        ("03_sql_injection_attack.png", create_sql_injection_screenshot),
        ("04_terminal_bandit_scan.png", create_terminal_bandit_screenshot),
        ("05_terminal_semgrep_scan.png", create_terminal_semgrep_screenshot),
        ("06_vulnerable_code.png", create_vulnerable_code_screenshot),
        ("07_fixed_secure_code.png", create_fixed_code_screenshot),
        ("08_file_upload_page.png", create_file_upload_screenshot),
    ]
    
    for filename, func in screenshots:
        filepath = os.path.join(screenshots_dir, filename)
        try:
            img = func()
            img.save(filepath, 'PNG')
            print(f"  Created: {filepath}")
        except Exception as e:
            print(f"  Error creating {filename}: {e}")
    
    print(f"\nAll screenshots saved to: {screenshots_dir}/")
    print("Screenshot generation complete!")

if __name__ == "__main__":
    main()
