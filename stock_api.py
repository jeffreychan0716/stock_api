from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
import json
from datetime import datetime

# === Load data on startup ===
with open("hsi_aug21_22_final.json", "r") as f:
    STOCK_DATA = json.load(f)

app = FastAPI(title="HSI Intraday Data API")

class StockResponse(BaseModel):
    stock: str
    datetime: str
    price_change_percent: float
    volume_multiplier: float

@app.get("/stock", response_model=StockResponse)
def get_stock_data(
    stock: str = Query(..., exmaple="0001.HK"),
    dt: str = Query(..., example="2025-08-21 11:00")
):
    """
    Retrieve intraday stock data (price movement and volume multiplier)
    """
    if stock not in STOCK_DATA:
        raise HTTPException(status_code=404, detail="Stock not found")

    try:
        query_dt = datetime.strptime(dt, "%Y-%m-%d %H:%M")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format. Use YYYY-MM-DD HH:MM")

    for entry in STOCK_DATA[stock]:
        if entry["datetime"] == dt:
            return {
                "stock": stock,
                "datetime": dt,
                "price_change_percent": entry["price_change_percent"],
                "volume_multiplier": entry["volume_multiplier"]
            }

    raise HTTPException(status_code=404, detail="Datetime not found for this stock")
