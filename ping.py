import os, sys, requests
from datetime import datetime

URL = os.environ["TARGET_URL"]  # set in Render (e.g., https://timestamp-app-xxxx.onrender.com/hit)

ts = datetime.utcnow().isoformat() + "Z"
try:
    r = requests.get(URL, timeout=10)
    print(f"[CRON] {ts} -> {r.status_code} | {r.text[:120]}")
    sys.exit(0 if r.ok else 1)
except Exception as e:
    print(f"[CRON] {ts} FAILED: {e}")
    sys.exit(1)
