# import json
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the JSON data
# with open("hsi_aug21_22_final.json", "r") as f:
#     data = json.load(f)

# # Choose the stock
# stock = "0003.HK"
# stock_data = data[stock]

# # Convert to DataFrame
# df = pd.DataFrame(stock_data)
# df['datetime'] = pd.to_datetime(df['datetime'])
# df.set_index('datetime', inplace=True)

# # Plotting
# plt.figure(figsize=(14, 6))

# # Price Movement (%)
# plt.subplot(2, 1, 1)
# plt.plot(df.index, df['price_change_percent'], label='Price Change (%)')
# plt.ylabel('Price Change (%)')
# plt.title(f'{stock} - Intraday Price Change (%)')
# plt.grid(True)

# # Cumulative Volume
# plt.subplot(2, 1, 2)
# plt.plot(df.index, df['cumulative_volume'], color='orange', label='Cumulative Volume')
# plt.ylabel('Cumulative Volume')
# plt.xlabel('Datetime')
# plt.title(f'{stock} - Cumulative Volume')
# plt.grid(True)

# plt.tight_layout()
# plt.show()

import json
import pandas as pd
import matplotlib.pyplot as plt

# === CONFIG ===
json_file = "hsi_aug21_22_final.json"
stock = "0113.HK"  # change to any stock you want
# date_filter = ["2025-08-21", "2025-08-22"]  # optional, e.g., "2025-08-22"

# === LOAD & FILTER DATA ===
with open(json_file, "r") as f:
    all_data = json.load(f)

# Convert selected stock's data to DataFrame
df = pd.DataFrame(all_data[stock])
df["datetime"] = pd.to_datetime(df["datetime"])

# Optional: filter by a specific day
# if date_filter:
#     df = df[df["datetime"].dt.strftime("%Y-%m-%d") == date_filter]

# === PLOT ===
plt.figure(figsize=(14, 6))

# Price movement
plt.subplot(2, 1, 1)
plt.plot(df["datetime"], df["price_change_percent"], label="Price Change (%)", color="blue")
plt.ylabel("Price Change (%)")
plt.title(f"{stock} - Intraday Price Movement")
plt.grid(True)
plt.legend()

# Volume multiplier
plt.subplot(2, 1, 2)
plt.plot(df["datetime"], df["volume_multiplier"], label="Volume Multiplier", color="orange")
plt.ylabel("Volume / Avg")
plt.xlabel("Time")
plt.title(f"{stock} - Intraday Volume (as multiple of avg)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
