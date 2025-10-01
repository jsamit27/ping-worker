import os, requests
from datetime import datetime, timezone

urls = [u.strip() for u in os.getenv("TARGET_URLS", os.getenv("TARGET_URL","")).split(",") if u.strip()]
ts = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

for u in urls:
    try:
        r = requests.get(u, timeout=10)
        print(f"{ts} | {u} -> {r.status_code} | {(r.text or '')[:100].replace('\n',' ')}", flush=True)
    except Exception as e:
        print(f"{ts} | {u} FAILED: {e}", flush=True)
