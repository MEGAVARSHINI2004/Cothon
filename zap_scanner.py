import requests
import time

API_KEY = "testkey"
ZAP_URL = "http://127.0.0.1:8081"
TARGET = "http://testphp.vulnweb.com"

def start_spider():
    print("[*] Spidering target...")
    spider = requests.get(f"{ZAP_URL}/JSON/spider/action/scan/", params={
        "apikey": API_KEY, "url": TARGET
    }).json()
    scan_id = spider.get("scan")
    while True:
        status = requests.get(f"{ZAP_URL}/JSON/spider/view/status/", params={
            "apikey": API_KEY, "scanId": scan_id
        }).json()
        if status["status"] == "100":
            break
        time.sleep(2)
    print("[+] Spidering done.")

def start_active_scan():
    print("[*] Starting active scan...")
    scan = requests.get(f"{ZAP_URL}/JSON/ascan/action/scan/", params={
        "apikey": API_KEY, "url": TARGET
    }).json()
    scan_id = scan.get("scan")
    while True:
        status = requests.get(f"{ZAP_URL}/JSON/ascan/view/status/", params={
            "apikey": API_KEY, "scanId": scan_id
        }).json()
        if status["status"] == "100":
            break
        time.sleep(2)
    print("[+] Active scan complete.")

def get_alerts():
    print("[*] Fetching alerts...")
    response = requests.get(f"{ZAP_URL}/JSON/core/view/alerts/", params={
        "apikey": API_KEY, "baseurl": TARGET
    }).json()
    return response.get("alerts", [])
