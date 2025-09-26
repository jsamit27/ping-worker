import os, time, requests
from datetime import datetime, timezone

urls = [u.strip() for u in os.getenv("TARGET_URLS", os.getenv("TARGET_URL", "")).split(",") if u.strip()]
#interval = int(os.getenv("INTERVAL_SECONDS", "30"))

if not urls:
    print("No TARGET_URLS/TARGET_URL set. Exiting.")
    raise SystemExit(1)

print(f"pinger -> {urls} every {interval}s", flush=True)

while True:
    ts = datetime.now(timezone.utc).isoformat()
    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            body = (r.text or "")[:100].replace("\n", " ")
            print(f"{ts} | {url} -> {r.status_code} | {body}", flush=True)
        except Exception as e:
            print(f"{ts} | {url} FAILED: {e}", flush=True)
    #time.sleep(interval)
