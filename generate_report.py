from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_report(alerts, filename="zap_report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, "ZAP Vulnerability Report")

    y = 780
    for alert in alerts:
        text = f"- {alert['alert']} (Risk: {alert['risk']})"
        c.drawString(80, y, text)
        y -= 20
        if y < 50:
            c.showPage()
            y = 800
    c.save()
    print(f"[+] Report saved as {filename}")
