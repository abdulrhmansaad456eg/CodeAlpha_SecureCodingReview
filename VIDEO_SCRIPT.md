# Video Script: Secure Coding Review Project
## Complete Walkthrough & Explanation Guide

**Duration:** 10-12 minutes  
**Target Audience:** Instructor/Evaluator for Cybersecurity Internship

---

## SECTION 1: INTRODUCTION (1 minute)

**[Scene: Project folder open, show README]**

**Script:**
"Hello, I'm presenting my Task 3 Secure Coding Review project for the cybersecurity internship. This project demonstrates a complete security assessment workflow on a Flask web application."

**Key Points to Cover:**
- Selected Python/Flask as the target language and framework
- Built a deliberately vulnerable application with 9 security flaws
- Performed both automated and manual security analysis
- Created a fully remediated secure version
- Duration: 4 weeks of work

**Visual:** Show the project structure with all folders

---

## SECTION 2: VULNERABLE APPLICATION DEMO (2 minutes)

**[Scene: Terminal - Start the vulnerable app]**

```bash
cd vulnerable_app
python app.py
```

**Script:**
"This is the vulnerable version of the application. Let me show you the intentional security flaws built into this code."

**Navigate to http://localhost:5000**

**Show:**
1. **Login Page** - "This is the login interface. Looks normal, but behind the scenes it has critical vulnerabilities."

2. **Open vulnerable_app/app.py and show:**
   - Line 7: Hardcoded secret key
   - Line 9: Debug mode enabled
   - Line 76: SQL injection vulnerability with string concatenation
   - Lines 134-138: Unsafe file upload
   - Line 175: Debug endpoint exposing sensitive info

**Demonstrate SQL Injection Live:**
```
Username: ' OR '1'='1' --
Password: anything
```

**Script:** 
"Watch what happens. By injecting SQL code into the username field, we bypass authentication completely. The query becomes 'select all users where 1 equals 1' - which is always true. We're now logged in as the first user in the database."

**Show Dashboard:**
- User directory visible
- File upload form
- Search functionality

---

## SECTION 3: SECURITY TOOLS & SCAN RESULTS (2 minutes)

**[Scene: Terminal with Bandit scan]**

**Script:**
"Now let's analyze the code with automated security tools. First, Bandit - a Python security linter."

**Run Command:**
```bash
bandit -r vulnerable_app/ -f txt
```

**Show Results:**
- Scroll through the output highlighting HIGH severity issues
- Point out: SQL injection (B608), hardcoded password (B105), debug mode (B201)
- Show summary: 9 total issues, 6 high severity

**Script:**
"Bandit found 9 security issues including critical SQL injection vulnerabilities and hardcoded secrets."

**[Scene: Terminal with Semgrep scan]**

**Run Command:**
```bash
semgrep --config=auto vulnerable_app/
```

**Show Results:**
- Error and warning findings
- OWASP Top 10 mapping (A03 Injection, A07 Auth Failures)
- CWE references for each finding

**Script:**
"Semgrep provides deeper analysis with 11 findings and maps them to OWASP categories and CWE references. The tools confirm our manual analysis."

**Show Saved Reports:**
```bash
cat scan_results/bandit_results.txt
cat scan_results/semgrep_results.txt
```

---

## SECTION 4: MANUAL CODE REVIEW FINDINGS (2 minutes)

**[Scene: Open manual_findings/detailed_findings.txt]**

**Script:**
"Beyond automated tools, I conducted a manual code review to find business logic vulnerabilities."

**Walk Through Each Finding:**

1. **SQL Injection (CWE-89)** - CRITICAL
   - Show vulnerable code with string concatenation
   - Explain impact: database compromise, auth bypass
   - Show exploitation scenario

2. **Hardcoded Secret (CWE-798)** - HIGH
   - Show line with hardcoded secret_key
   - Explain session forgery risk
   - Show how attacker could forge cookies

3. **Debug Mode (CWE-489)** - HIGH
   - Show debug=True
   - Explain RCE through Werkzeug debugger

4. **Plaintext Passwords (CWE-256)** - HIGH
   - Show sample_users with plaintext passwords
   - Explain compliance violations

5. **Unsafe File Upload (CWE-434)** - MEDIUM
   - Show file upload with no validation
   - Explain web shell upload risk

6. **Information Disclosure (CWE-200)** - MEDIUM
   - Show /debug endpoint
   - Show it exposes secret key and env vars

7. **Path Traversal (CWE-22)** - MEDIUM
   - Show file serving without sanitization
   - Explain ../ attack to access /etc/passwd

**Script:**
"The manual review identified 7 detailed vulnerabilities with severity ratings, exploitation scenarios, and specific remediation steps."

---

## SECTION 5: SECURE VERSION & FIXES (2.5 minutes)

**[Scene: Open fixed_app/app.py side-by-side with vulnerable version]**

**Script:**
"Now let me show you the remediated secure version. I'll walk through each fix."

**Show Fixes:**

1. **Parameterized Queries:**
   - OLD: `query = f"SELECT...'{username}'"`
   - NEW: `cursor.execute("SELECT...?", (username,))`
   - Script: "Using parameterized queries eliminates SQL injection completely."

2. **Environment Secrets:**
   - OLD: `app.secret_key = 'hardcoded'`
   - NEW: `app.secret_key = os.environ.get('SECRET_KEY')`
   - Script: "Secrets are now loaded from environment variables, never in code."

3. **Password Hashing:**
   - OLD: Plaintext passwords
   - NEW: `generate_password_hash(password, method='pbkdf2:sha256')`
   - Show verification with `check_password_hash()`

4. **Debug Mode Disabled:**
   - OLD: `app.debug = True`
   - NEW: `app.debug = False`
   - Script: "Debug mode is disabled, preventing information leaks and RCE."

5. **File Upload Security:**
   - OLD: Direct save with user filename
   - NEW: `secure_filename()`, extension validation, size limits
   - Show ALLOWED_EXTENSIONS whitelist

6. **Input Validation:**
   - Show `validate_input()` function with length limits
   - Show character allowlisting

7. **Security Headers:**
   - Show `add_security_headers()` function
   - List: X-Frame-Options, CSP, X-Content-Type-Options

**Demonstrate Secure Version:**
```bash
cd fixed_app
set SECRET_KEY=my-secret-key
python app.py
```

**Try SQL Injection Again:**
- Script: "Now watch - the same SQL injection payload fails. The parameterized query treats it as literal text, not SQL code. Authentication properly fails."

---

## SECTION 6: PROFESSIONAL REPORT (1 minute)

**[Scene: Open reports/Secure_Coding_Review_Report.docx]**

**Script:**
"I've compiled all findings into a professional report suitable for academic or corporate submission."

**Show Report Sections:**
1. Title Page - "Secure Coding Review of a Flask Web Application"
2. Table of Contents
3. Executive Summary - 9 vulnerabilities found, all remediated
4. Methodology - Automated + Manual review
5. Tools Used - Bandit, Semgrep details
6. Vulnerability Findings - Detailed analysis of each flaw
7. Risk Assessment Matrix
8. Remediation Steps - Priority-based fix strategy
9. Best Practices Guide - OWASP Top 10 mapping
10. Comparison Analysis - Before/After
11. Conclusion & References

**Script:**
"The report follows industry standards with executive summary, technical findings, risk assessment, and actionable remediation guidance."

---

## SECTION 7: SCREENSHOTS & DELIVERABLES (30 seconds)

**[Scene: Open screenshots folder]**

**Script:**
"The project includes 8 screenshots documenting:"

1. Login page UI
2. Dashboard interface
3. SQL injection attack demonstration
4. Bandit scan terminal output
5. Semgrep scan results
6. Vulnerable code snippet
7. Fixed secure code
8. File upload vulnerability

**Script:**
"All screenshots are included in the submission for visual documentation."

---

## SECTION 8: CONCLUSION (30 seconds)

**[Scene: Back to project structure view]**

**Script:**
"To summarize this internship project:"

- Built vulnerable Flask app with 9 intentional security flaws
- Performed automated analysis with Bandit and Semgrep
- Conducted manual code review with detailed findings
- Implemented complete remediation in secure version
- Documented everything in professional report format

**Key Learning Outcomes:**
- SQL injection prevention through parameterized queries
- Secret management best practices
- Secure authentication implementation
- Static analysis tool usage
- Professional security documentation

**Script:**
"This project demonstrates practical application of secure coding principles, vulnerability assessment methodologies, and professional remediation workflows required in cybersecurity roles."

---

## CLOSING

**Script:**
"Thank you for reviewing my Task 3 Secure Coding Review project. All code, reports, and documentation are ready for submission."

**[End Screen: Show zip file ready for submission]**

---

## RECORDING TIPS

**Technical Setup:**
- Use OBS Studio or Camtasia for screen recording
- Record at 1080p (1920x1080) for clarity
- Use microphone for narration
- Keep terminal font size large (14-16pt) for readability

**Presentation Style:**
- Speak clearly and at moderate pace
- Pause between sections
- Use cursor to highlight specific code lines
- Zoom in on critical code sections
- Keep video under 15 minutes

**Alternative:** If you prefer, you can use this script with PowerPoint/Canva slides showing screenshots instead of live demo.

---

## QUICK REFERENCE: Terminal Commands to Show

```bash
# Start vulnerable app
cd vulnerable_app && python app.py

# Run security scans
bandit -r vulnerable_app/ -f txt
semgrep --config=auto vulnerable_app/

# Start secure app
cd fixed_app
set SECRET_KEY=my-secret-key
python app.py

# View reports
cat scan_results/bandit_results.txt
cat scan_results/semgrep_results.txt
```

---

**END OF VIDEO SCRIPT**

Total Estimated Runtime: 10-12 minutes
Recommended Recording Software: OBS Studio (free) or Camtasia
Output Format: MP4 (H.264 codec, 1080p)
File Name: secure_coding_review_video.mp4

Submit Along With:
- secure-coding-review-submission.zip
- secure_coding_review_video.mp4
- Any additional documentation

**Note:** If you cannot record video, this script can also be submitted as a written walkthrough document.

---

## BONUS: QUICK START GUIDE FOR RECORDING

**Step 1:** Open terminal, navigate to project
**Step 2:** Start recording
**Step 3:** Follow script sections in order
**Step 4:** Pause recording between sections if needed
**Step 5:** Stop recording and save as MP4
**Step 6:** Review and trim if necessary
**Step 7:** Submit video with zip file

**Estimated Total Recording Time:** 30-45 minutes including retakes
**Final Video Length:** 10-12 minutes after editing

Good luck with your submission!

---

*Script Version: 1.0*  
*Date: May 2026*  
*Project: Secure Coding Review - Task 3*

---

## VIDEO CHECKLIST

Before submitting, verify:

- [ ] Introduction covers project overview
- [ ] Vulnerable app is demonstrated live
- [ ] SQL injection attack shown working
- [ ] Bandit scan results displayed
- [ ] Semgrep scan results displayed
- [ ] At least 3 manual findings explained
- [ ] Secure version fixes shown side-by-side
- [ ] SQL injection properly blocked in secure version
- [ ] Professional report shown
- [ ] Screenshots mentioned/demonstrated
- [ ] Clear conclusion with learning outcomes
- [ ] Audio is clear and understandable
- [ ] Video quality is 1080p or higher
- [ ] File name is descriptive
- [ ] Under 15 minutes total runtime

**If any checkbox is missing, re-record that section.**

---

**SUBMISSION PACKAGE:**
1. secure-coding-review-submission.zip (code + docs)
2. secure_coding_review_video.mp4 (this recording)
3. VIDEO_SCRIPT.md (this script - optional)

Ready for evaluation!

---

END OF DOCUMENT
**TOTAL PAGES:** ~8 pages when printed
**READING TIME:** 15 minutes
**RECORDING TIME:** 30-45 minutes

---

*Generated for Cybersecurity Internship Task 3*
*Secure Coding Review Project*
*May 2026*

---

## VIDEO ALTERNATIVES

If you cannot create video, consider these alternatives:

**Option A: Slideshow with Voiceover**
- Create PowerPoint with screenshots
- Record audio narration
- Export as video (PPT can do this)

**Option B: Written Walkthrough**
- Expand this script into detailed document
- Add more screenshots
- Submit as PDF walkthrough

**Option C: Live Presentation**
- Present to instructor via Zoom/Teams
- Share screen and walk through live
- Record the session

**Recommended:** Option A or video recording for best results

---

**Remember:** The goal is demonstrating your understanding of the project, not professional video production quality. Clear explanation matters more than fancy editing.

---

*Good luck with your internship submission!*

---

END OF VIDEO SCRIPT DOCUMENT
