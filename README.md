# Secure Coding Review of a Flask Web Application

A comprehensive cybersecurity internship project focusing on secure software development, vulnerability assessment, and remediation of a Flask web application.

## Project Overview

This project demonstrates a complete secure coding review workflow, from identifying vulnerabilities in a deliberately insecure Flask application to implementing professional remediation measures. This project was built to practice identifying and fixing common Flask web application vulnerabilities.

## Project Structure

```
CodeAlpha_SecureCodingReview/
│
├── vulnerable_app/          # Insecure version with intentional vulnerabilities
│   ├── app.py              # Main Flask application (vulnerable)
│   ├── requirements.txt      # Python dependencies
│   ├── templates/           # HTML templates
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── static/             # CSS stylesheets
│       └── style.css
│   
│
├── fixed_app/              # Secure remediated version
│   ├── app.py              # Main Flask application (secure)
│   ├── requirements.txt    # Python dependencies
│   ├── templates/         # Secure HTML templates
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── static/           # CSS stylesheets
│       └── style.css
│           
│
├── screenshots/            # Application screenshots
│   ├── 01_login_page.png
│   ├── 02_dashboard_page.png
│   ├── 03_sql_injection_attack.png
│   ├── 04_terminal_bandit_scan.png
│   ├── 05_terminal_semgrep_scan.png
│   ├── 06_vulnerable_code.png
│   ├── 07_fixed_secure_code.png
│   └── 08_file_upload_page.png
│
├── scan_results/          # Security scan outputs
│   ├── bandit_results.txt
│   └── semgrep_results.txt
│
├── reports/               # Professional documentation
│   └── Secure_Coding_Review_Report.docx
│
├── screenshots.py    # Screenshot generation script
├── report.py         # Report generation script
└── README.md                  
```

## Features

### Vulnerable Application
The vulnerable version includes these features with security flaws:

- User login with SQL injection vulnerability
- SQLite database with plaintext password storage
- File upload without validation
- Session management with hardcoded secret key
- Debug information disclosure endpoint
- Search functionality with XSS potential

### Secure Application
The fixed version maintains all features with security improvements:

- Parameterized SQL queries preventing injection
- PBKDF2 password hashing with salt
- Environment-based secret management
- File upload validation and sanitization
- Secure session configuration
- Input validation and sanitization
- Security headers and error handling

## Vulnerabilities Identified

1. **SQL Injection (CWE-89)** - Critical
   - String concatenation in SQL queries allows authentication bypass
   - Affected: login and search functionality

2. **Hardcoded Secret Key (CWE-798)** - High
   - Flask secret key embedded in source code
   - Risk: Session forgery and unauthorized access

3. **Debug Mode Enabled (CWE-489)** - High
   - Flask running in debug mode exposes sensitive information
   - Risk: Remote code execution through Werkzeug debugger

4. **Plaintext Password Storage (CWE-256)** - High
   - Passwords stored without any hashing
   - Risk: Complete credential exposure if database compromised

5. **Unsafe File Upload (CWE-434)** - Medium
   - No file type validation or sanitization
   - Risk: Malicious file upload, remote code execution

6. **Information Disclosure (CWE-200)** - Medium
   - Debug endpoint exposes system configuration
   - Risk: Reconnaissance aid for attackers

7. **Path Traversal (CWE-22)** - Medium
   - Unsanitized filename parameter allows directory traversal
   - Risk: Unauthorized file system access

8. **Verbose Error Messages (CWE-209)** - Low
   - Detailed SQL errors displayed to users
   - Risk: Information leakage aiding further attacks

9. **Missing Input Validation (CWE-20)** - Medium
   - User input used without validation
   - Risk: Multiple injection attack vectors

## Tools Used

- **Bandit 1.7.5** - Python security linter detecting common security issues
- **Semgrep 1.45.0** - Static analysis engine for identifying code patterns
- **Flask 2.3.3** - Web framework for the application
- **SQLite** - Database engine for data storage
- **Werkzeug** - WSGI utility library with security functions

## Installation

1. Clone or download the project:
```bash
cd secure-coding-review
```

2. Install Python 3.10 or higher

3. Install dependencies:
```bash
# For vulnerable version
pip install -r vulnerable_app/requirements.txt

# For secure version
pip install -r fixed_app/requirements.txt
```

4. Install security scanning tools (optional):
```bash
pip install bandit semgrep
```

## Running the Vulnerable Version

1. Navigate to the vulnerable app directory:
```bash
cd vulnerable_app
```

2. Run the application:
```bash
python app.py
```

3. Open a browser and navigate to:
```
http://localhost:5000
```

4. Default credentials:
   - admin / admin123
   - john_doe / password123
   - jane_smith / welcome2024

**Warning**: This version contains intentional security vulnerabilities. Only run in an isolated environment for educational purposes.

## Running the Secure Version

1. Navigate to the fixed app directory:
```bash
cd fixed_app
```

2. Set the secret key environment variable:
```bash
# Windows
set SECRET_KEY=your-secret-key-here

# Linux/Mac
export SECRET_KEY=your-secret-key-here
```

3. Run the application:
```bash
python app.py
```

4. Open a browser and navigate to:
```
http://localhost:5000
```

## Running Security Scans

### Bandit Scan
```bash
cd secure-coding-review
bandit -r vulnerable_app/ -o scan_results/bandit_results.txt
```

### Semgrep Scan
```bash
cd secure-coding-review
semgrep --config=auto vulnerable_app/ > scan_results/semgrep_results.txt
```

## Project Screenshots

The project includes the following screenshots in the `screenshots/` directory:

1. **Login Page** - The application login interface
2. **Dashboard Page** - Main application dashboard with user features
3. **SQL Injection Attack** - Demonstrating authentication bypass
4. **Bandit Scan Terminal** - Automated security scan results
5. **Semgrep Scan Terminal** - Static analysis findings
6. **Vulnerable Code** - Code snippets showing security flaws
7. **Fixed Secure Code** - Remediated code with security improvements
8. **File Upload Page** - Upload functionality interface

## Learning Outcomes

Through this project, the following cybersecurity concepts were explored:

- **Injection Attacks**: Understanding SQL injection mechanics and prevention through parameterized queries
- **Authentication Security**: Implementing secure password storage and session management
- **Secure Configuration**: Properly configuring applications for production environments
- **Input Validation**: Validating and sanitizing user input to prevent attacks
- **Static Analysis**: Using automated tools to identify security vulnerabilities
- **Secure Development Lifecycle**: Integrating security into the development process

## Security Best Practices Demonstrated

1. Use parameterized queries for all database operations
2. Store passwords using strong adaptive hashing (PBKDF2, bcrypt)
3. Load secrets from environment variables, never hardcode
4. Disable debug mode in production environments
5. Validate and sanitize all user input
6. Implement proper file upload validation and sanitization
7. Use security headers to protect against common attacks
8. Display generic error messages to users
9. Keep detailed logs for internal debugging

## OWASP Top 10 2021 Coverage

This project addresses the following OWASP Top 10 categories:

- **A01: Broken Access Control** - Path traversal, insecure direct object references
- **A02: Cryptographic Failures** - Plaintext password storage, hardcoded secrets
- **A03: Injection** - SQL injection vulnerabilities
- **A04: Insecure Design** - Unsafe file upload functionality
- **A05: Security Misconfiguration** - Debug mode enabled, verbose errors
- **A07: Identification and Authentication Failures** - Weak authentication mechanisms

## Report

A comprehensive professional report documenting the entire secure coding review process is available at:

```
reports/Secure_Coding_Review_Report.docx
```

The report includes:
- Detailed vulnerability analysis
- Risk severity assessment
- Remediation steps and code examples
- Comparison between vulnerable and secure versions
- Secure coding best practices
- References to security standards

## Disclaimer

The vulnerable application intentionally contains security flaws for educational purposes. It should never be deployed in a production environment or exposed to untrusted networks. Always use the secure version (fixed_app) as a reference for proper security implementation.

## References

- [OWASP Top 10:2021](https://owasp.org/Top10/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [Flask Security Documentation](https://flask.palletsprojects.com/en/2.3.x/security/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Semgrep Documentation](https://semgrep.dev/)

## Author

Cybersecurity Internship Project  
Date: May 2026  
Duration: 4 weeks

---

**Note**: This project was created for educational purposes as part of a cybersecurity internship program. The techniques and vulnerabilities demonstrated here are commonly found in real-world applications and understanding them is essential for building secure software.
