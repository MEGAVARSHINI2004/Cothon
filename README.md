# Automated Vulnerability Scanning and Reporting Tool


A Python-based automated web vulnerability scanning tool that leverages OWASP ZAP and provides a Flask-based web interface. This tool allows users to input target URLs, initiate scans, and generate comprehensive vulnerability reports in PDF format — all in a few clicks.

# 🚀 Features:

✅ Integrates with OWASP ZAP (Zed Attack Proxy) for automated security scanning

✅ Flask Web Interface to easily input URLs and trigger scans

✅ Generates PDF vulnerability reports with scan results

✅ Supports multiple URL inputs through file upload (.txt)

✅ Built-in support for Windows Task Scheduler for automated scans (optional)

✅ Clean and modular Python codebase with clear separation of functionality



# 🧩 Project Structure:
.
├── zap_scanner.py         # Handles interactions with OWASP ZAP API
├── generate_report.py     # Generates PDF reports from scan results
├── run_tool.py            # CLI-based alternative to trigger scan and generate report
├── app.py                 # Flask web application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── static/ & templates/   # Flask assets (HTML, CSS, JS)



# 📸 Web Interface Overview:

Home Page: Input a single URL or upload a .txt file of multiple URLs.

Scan Trigger: Initiates the OWASP ZAP scan in the background.

Reports: Automatically generates and provides a downloadable PDF report.



# ⚙️ Installation & Setup:

## 1. Clone the repository
git clone https://github.com/your-username/vulnerability-scanner-zap.git
cd vulnerability-scanner-zap

## 2. Install Python dependencies
pip install -r requirements.txt

## 3. Install and Start OWASP ZAP
Download ZAP from the official site.

Run ZAP in daemon mode (no UI):
zap.sh -daemon -port 8090
Or on Windows:
zap.bat -daemon -port 8090

## 4. Run the Flask Appt
python app.py
Access the web app at: http://localhost:5000



# 🛡️ How It Works:

User inputs a URL (or uploads a .txt file).

The Flask app calls the OWASP ZAP API using zap_scanner.py.

After scanning, results are collected and parsed.

generate_report.py formats the findings into a structured PDF report.

The report is available for download.



# 📄 Example PDF Report:

The PDF includes:

URL scanned

Alerts and risk levels

Vulnerability descriptions

Recommended fixes

(Sample reports can be added in a reports/ folder or linked here)



# 📅 Scheduling Automated Scans (Optional):

You can automate scans using Windows Task Scheduler by scheduling run_tool.py or invoking specific endpoints of the Flask app using curl.



# 🔧 Tech Stack:

Python 3.8+

Flask

OWASP ZAP API

FPDF / ReportLab for PDF generation

HTML/CSS for frontend



# ✍️ Authors
Megavarshini – Developer
Linkedin : https://www.linkedin.com/in/a-megavarshini/
mail_id : megavarshini3031@gmail.com



# 🏁 Future Enhancements
Add authentication for web access

Support for scheduling via cron (Linux) or Task Scheduler (Windows)

GUI for managing scan history

Email reports feature

Integration with Slack or Discord for alerts
