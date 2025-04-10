from flask import Flask, send_file, render_template_string, request
from run_tool import start_spider, start_active_scan, get_alerts
from generate_report import generate_report

app = Flask(__name__)

HTML = '''
<h1>🛡️ ZAP Vulnerability Scanner</h1>
<form method="POST">
    <button type="submit">Start Scan</button>
</form>
{% if ready %}
<p>✅ Scan complete. <a href="/download">Download Report</a></p>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    ready = False
    if request.method == 'POST':
        start_spider()
        start_active_scan()
        alerts = get_alerts()
        generate_report(alerts)
        ready = True
    return render_template_string(HTML, ready=ready)

@app.route('/download')
def download():
    return send_file("zap_report.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
