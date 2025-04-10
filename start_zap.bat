cd "C:\Program Files\ZAP\Zed Attack Proxy"
zap.bat -daemon -port 8080
zap.bat -daemon -host 127.0.0.1 -port 8080 -config api.addrs.addr.name=127.0.0.1 -config api.addrs.addr.regex=false

