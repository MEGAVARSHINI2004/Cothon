from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def generate_report(alerts, filename="zap_report.pdf"):
    # Create the PDF
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, "ZAP Vulnerability Report")
    c.drawString(100, 780, "Report generated on: [Date]")

    # Summary Section
    y = 750
    c.setFont("Helvetica", 10)
    c.drawString(80, y, "Vulnerabilities Overview:")
    y -= 20
    severity_count = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}

    for alert in alerts:
        severity_count[alert['risk']] += 1

    # Bar chart of vulnerabilities by severity
    labels = list(severity_count.keys())
    counts = list(severity_count.values())

    fig, ax = plt.subplots()
    ax.bar(labels, counts, color=['green', 'yellow', 'orange', 'red'])
    ax.set_title("Vulnerabilities by Severity")
    ax.set_ylabel("Number of Vulnerabilities")
    
    # Save the chart to a buffer
    buf = io.BytesIO()
    FigureCanvas(fig).print_png(buf)
    buf.seek(0)
    
    # Embed the graph in the PDF
    c.drawImage(buf, 80, y - 100, width=400, height=200)
    
    y -= 200

    # Pie chart of vulnerability distribution
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['green', 'yellow', 'orange', 'red'])
    ax.set_title("Vulnerability Distribution by Risk Level")
    
    buf = io.BytesIO()
    FigureCanvas(fig).print_png(buf)
    buf.seek(0)
    
    # Embed the pie chart in the PDF
    c.drawImage(buf, 80, y - 100, width=400, height=200)
    
    y -= 200

    # Detailed description of top vulnerabilities
    c.setFont("Helvetica", 10)
    c.drawString(80, y, "Detailed Vulnerabilities:")
    y -= 20
    
    for alert in alerts[:5]:  # Displaying the top 5 vulnerabilities
        c.drawString(80, y, f"Alert: {alert['alert']}")
        c.drawString(80, y - 15, f"Risk: {alert['risk']}")
        c.drawString(80, y - 30, f"Description: {alert['description']}")
        y -= 60

        if y < 50:  # Prevent overflow by adding a new page
            c.showPage()
            y = 750

    # Save the PDF
    c.save()

    print(f"[+] Report saved as {filename}")


