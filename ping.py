import os, time, requests
from datetime import datetime

TARGET_URLS = os.getenv("TARGET_URLS", "").split(",")  
# Example: set env var as "https://app1.onrender.com/hit,https://app2.onrender.com/hit"

INTERVAL = int(os.getenv("INTERVAL_SECONDS", "30"))

print(f"pinger -> {TARGET_URLS} every {INTERVAL}s", flush=True)

while True:
    ts = datetime.utcnow().isoformat() + "Z"
    for url in TARGET_URLS:
        url = url.strip()
        if not url:
            continue
        try:
            r = requests.get(url, timeout=10)
            print(f"ping {ts} -> {url} -> {r.status_code} | {r.text[:100]}", flush=True)
        except Exception as e:
            print(f"ping {ts} -> {url} FAILED: {e}", flush=True)
    time.sleep(INTERVAL)
