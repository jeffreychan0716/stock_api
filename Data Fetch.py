import requests
import json
from datetime import datetime

# === CONFIG ===
API_KEY = "43edd3607624576fb682301db1165c5e-c-app"  # Replace with your actual AllTick API key
TICKER = "AAPL.US"
QUERY_KLINE_NUM = 390  # ~full US trading day
TRACE = "python_intraday"
BASE_URL = "https://quote.alltick.io/quote-stock-b-api/kline"

# === Construct query string manually (JSON URL-encoded)
query = {
    "trace": TRACE,
    "data": {
        "code": TICKER,
        "kline_type": 1,              # 1-minute
        "kline_timestamp_end": 0,     # 0 = latest available
        "query_kline_num": QUERY_KLINE_NUM,
        "adjust_type": 0              # 0 = no adjustment
    }
}

# Encode the query JSON and insert into URL
import urllib.parse
encoded_query = urllib.parse.quote(json.dumps(query))
url = f"{BASE_URL}?token={API_KEY}&query={encoded_query}"

# === Make request
resp = requests.get(url)
result = resp.json()

# === Check response
if result.get("code") != 0 or "klines" not in result.get("data", {}):
    print("❌ API error:", result.get("message"))
    exit()

# === Process result
klines = result["data"]["klines"]
parsed = []
base_close = float(klines[0][4])  # first close as base

for k in klines:
    timestamp = datetime.fromtimestamp(k[0])
    o, h, l, c, v = map(float, k[1:6])
    pct_change = (c - base_close) / base_close * 100
    parsed.append({
        "datetime": timestamp.isoformat(),
        "open": o,
        "high": h,
        "low": l,
        "close": c,
        "volume": int(v),
        "pct_change_vs_open": pct_change
    })

# === Save to JSON
output_file = f"{TICKER.replace('.', '_')}_intraday.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(parsed, f, indent=2)

print(f"✅ Saved intraday data to: {output_file}")
