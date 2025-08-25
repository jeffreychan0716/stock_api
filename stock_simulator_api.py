from fastapi import FastAPI
from fastapi.responses import JSONResponse
from threading import Thread
import time
import json
from datetime import datetime

app = FastAPI(title="HSI Real-Time Simulator API")

# Load data
with open("hsi_aug21_22_final.json", "r") as f:
    STOCK_DATA = json.load(f)

# Generate sorted unique timestamps across all stocks (from one example stock)
reference_stock = next(iter(STOCK_DATA))
timestamps = [entry["datetime"] for entry in STOCK_DATA[reference_stock]]

def is_valid_trading_time(ts):
    time_part = ts.split(" ")[1]
    hour, minute = map(int, time_part.split(":"))

    # Morning: 09:30–11:59, Afternoon: 13:00–15:59
    return (9 <= hour <= 11) or (13 <= hour <= 15)

timestamps = [ts for ts in timestamps if is_valid_trading_time(ts)]

# Sort timestamps to ensure order
timestamps = sorted(set(timestamps))

# Index to track current simulation position
current_index = 0

def advance_time():
    global current_index
    while True:
        time.sleep(2)  # 5 real seconds = 1 simulated minute
        current_index = (current_index + 1) % len(timestamps)  # loop

# Background thread to advance simulated time
Thread(target=advance_time, daemon=True).start()

@app.get("/stocks")
def get_current_market_data():
    current_time = timestamps[current_index]
    result = []

    for stock, entries in STOCK_DATA.items():
        for entry in entries:
            if entry["datetime"] == current_time:
                result.append({
                    "stock": stock,
                    "datetime": entry["datetime"],
                    "price_change_percent": entry["price_change_percent"],
                    "volume_multiplier": entry["volume_multiplier"]
                })
                break  # only one entry per stock

    return JSONResponse(content={"timestamp": current_time, "data": result})
