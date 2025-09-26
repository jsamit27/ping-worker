import os, time, requests
from datetime import datetime

TARGET_URL = os.environ["TARGET_URL"]  # set this in Render (example: https://your-web.onrender.com/hit)
INTERVAL = int(os.getenv("INTERVAL_SECONDS", "30"))

print(f"pinger -> {TARGET_URL} every {INTERVAL}s", flush=True)

while True:
    ts = datetime.utcnow().isoformat() + "Z"
    try:
        r = requests.get(TARGET_URL, timeout=10)
        print(f"ping {ts} -> {r.status_code} | {r.text[:100]}", flush=True)
    except Exception as e:
        print(f"ping {ts} FAILED: {e}", flush=True)
    time.sleep(INTERVAL)
