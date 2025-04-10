# run_tool.py
from zap_scanner import start_spider, start_active_scan, get_alerts
from generate_report import generate_report

def run_tool():
    start_spider()
    start_active_scan()
    alerts = get_alerts()
    generate_report(alerts)
    return alerts  # Return alerts so Flask knows when it's done




