# # import json
# # import random
# # from datetime import datetime, timedelta

# # # Sample HSI stock list (can expand)
# # hsi_stocks = [
# #     "0001.HK", "0002.HK", "0003.HK", "0005.HK", "0006.HK", "0011.HK", "0012.HK",
# #     "0016.HK", "0017.HK", "0019.HK", "0023.HK", "0027.HK", "0066.HK", "0101.HK",
# #     "0108.HK", "0113.HK", "0129.HK", "0135.HK", "0144.HK", "0151.HK", "0175.HK",
# #     "0177.HK", "0207.HK", "0222.HK", "0231.HK", "0238.HK", "0267.HK", "0288.HK",
# #     "0291.HK", "0293.HK", "0308.HK", "0322.HK", "0386.HK", "0388.HK", "0606.HK",
# #     "0688.HK", "0700.HK", "0762.HK", "0803.HK", "0823.HK", "0836.HK", "0857.HK",
# #     "0883.HK", "0939.HK", "0941.HK", "0960.HK", "0968.HK", "0981.HK", "0992.HK",
# #     "1038.HK", "1044.HK", "1093.HK", "1109.HK", "1113.HK", "1171.HK", "1211.HK",
# #     "1299.HK", "1313.HK", "1336.HK", "1357.HK", "1378.HK", "1398.HK", "1928.HK",
# #     "1972.HK", "2007.HK", "2018.HK", "2313.HK", "2318.HK", "2319.HK", "2328.HK",
# #     "2331.HK", "2382.HK", "2388.HK", "2412.HK", "2628.HK", "2688.HK", "3690.HK",
# #     "3888.HK", "3988.HK", "6030.HK", "6098.HK", "6618.HK", "6690.HK", "6823.HK",
# #     "9618.HK", "9633.HK", "9988.HK", "9999.HK", "1024.HK"
# # ]


# # # HK market hours: 9:30–12:00 and 13:00–16:00
# # def get_intraday_minutes():
# #     minutes = []
# #     # Morning session
# #     current = datetime.strptime("09:30", "%H:%M")
# #     end = datetime.strptime("12:00", "%H:%M")
# #     while current < end:
# #         minutes.append(current.strftime("%H:%M"))
# #         current += timedelta(minutes=1)
# #     # Afternoon session
# #     current = datetime.strptime("13:00", "%H:%M")
# #     end = datetime.strptime("16:00", "%H:%M")
# #     while current < end:
# #         minutes.append(current.strftime("%H:%M"))
# #         current += timedelta(minutes=1)
# #     return minutes

# # def generate_stock_data(stock, date_str):
# #     intraday_minutes = get_intraday_minutes()
# #     data = []
# #     price = 100  # arbitrary base price
# #     cumulative_volume = 0
# #     cumulative_return = 0.0
# #     for t in intraday_minutes:
# #         # Simulate small return per minute
# #         ret = random.uniform(-0.0005, 0.0005)
# #         cumulative_return += ret
# #         price *= (1 + ret)
# #         # Simulate volume for the minute and add to cumulative
# #         volume = random.randint(1000, 5000)
# #         cumulative_volume += volume
# #         data_point = {
# #             "datetime": f"{date_str} {t}",
# #             "stock": stock,
# #             "price_change_percent": round(cumulative_return * 100, 3),
# #             "cumulative_volume": cumulative_volume
# #         }
# #         data.append(data_point)
# #     return data

# # def generate_json():
# #     dates = ["2025-06-23", "2025-06-24"]
# #     output = {}
# #     for stock in hsi_stocks:
# #         output[stock] = []
# #         for date in dates:
# #             output[stock].extend(generate_stock_data(stock, date))
# #     with open("hsi_intraday_data.json", "w") as f:
# #         json.dump(output, f, indent=2)

# # generate_json()

# # import os
# # print(f"File saved to: {os.path.abspath('hsi_intraday_data.json')}")

# import json
# import random
# from datetime import datetime, timedelta

# # List of 85 HSI tickers
# hsi_stocks = [
#     "0001.HK", "0002.HK", "0003.HK", "0005.HK", "0006.HK", "0011.HK", "0012.HK", "0016.HK", "0017.HK",
#     "0019.HK", "0023.HK", "0027.HK", "0066.HK", "0101.HK", "0108.HK", "0113.HK", "0129.HK", "0135.HK",
#     "0144.HK", "0151.HK", "0175.HK", "0177.HK", "0207.HK", "0222.HK", "0231.HK", "0238.HK", "0267.HK",
#     "0288.HK", "0291.HK", "0293.HK", "0308.HK", "0322.HK", "0386.HK", "0388.HK", "0606.HK", "0688.HK",
#     "0700.HK", "0762.HK", "0803.HK", "0823.HK", "0836.HK", "0857.HK", "0883.HK", "0939.HK", "0941.HK",
#     "0960.HK", "0968.HK", "0981.HK", "0992.HK", "1038.HK", "1044.HK", "1093.HK", "1109.HK", "1113.HK",
#     "1171.HK", "1211.HK", "1299.HK", "1313.HK", "1336.HK", "1357.HK", "1378.HK", "1398.HK", "1928.HK",
#     "1972.HK", "2007.HK", "2018.HK", "2313.HK", "2318.HK", "2319.HK", "2328.HK", "2331.HK", "2382.HK",
#     "2388.HK", "2412.HK", "2628.HK", "2688.HK", "3690.HK", "3888.HK", "3988.HK", "6030.HK", "6098.HK",
#     "6618.HK", "6690.HK", "6823.HK", "9618.HK", "9633.HK", "9988.HK", "9999.HK", "1024.HK"
# ]

# # Generate list of last 12 trading days skipping weekends
# def get_trading_days(end_date, num_days):
#     days = []
#     current = end_date
#     while len(days) < num_days:
#         if current.weekday() < 5:  # Weekday only
#             days.insert(0, current)
#         current -= timedelta(days=1)
#     return days

# # HK Market times
# def get_intraday_minutes():
#     minutes = []
#     # Morning
#     current = datetime.strptime("09:30", "%H:%M")
#     end = datetime.strptime("12:00", "%H:%M")
#     while current < end:
#         minutes.append(current.strftime("%H:%M"))
#         current += timedelta(minutes=1)
#     # Afternoon
#     current = datetime.strptime("13:00", "%H:%M")
#     end = datetime.strptime("16:00", "%H:%M")
#     while current < end:
#         minutes.append(current.strftime("%H:%M"))
#         current += timedelta(minutes=1)
#     return minutes

# # Simulate stock data
# def generate_stock_data(stock, dates):
#     intraday_minutes = get_intraday_minutes()
#     data = []
#     all_day_volumes = []
    
#     for i, date in enumerate(dates):
#         cumulative_return = 0.0
#         cumulative_volume = 0
#         price = 100  # arbitrary base price
#         date_str = date.strftime("%Y-%m-%d")

#         # Decide if today is a "big move" day
#         big_move_today = random.random() < 0.1  # ~10% of the days
#         move_multiplier = random.uniform(4, 8) if big_move_today else 1

#         # Use high volume on last 2 days
#         spike_volume = (i >= len(dates) - 2)
#         avg_volume = (sum(all_day_volumes) / len(all_day_volumes)) if all_day_volumes else 1000000
#         base_volume_per_min = avg_volume / len(intraday_minutes)
#         volume_multiplier = 10 if spike_volume else 1

#         for t in intraday_minutes:
#             ret = random.uniform(-0.0005, 0.0005) * move_multiplier
#             cumulative_return += ret
#             price *= (1 + ret)

#             vol = int(random.gauss(base_volume_per_min, 500)) * volume_multiplier
#             vol = max(0, vol)
#             cumulative_volume += vol

#             data_point = {
#                 "datetime": f"{date_str} {t}",
#                 "stock": stock,
#                 "price_change_percent": round(cumulative_return * 100, 3),
#                 "cumulative_volume": cumulative_volume
#             }
#             data.append(data_point)

#         all_day_volumes.append(cumulative_volume)

#     return data

# # Generate everything
# def generate_json():
#     end_date = datetime.strptime("2025-08-23", "%Y-%m-%d")  # today (or change)
#     dates = get_trading_days(end_date, 12)

#     output = {}
#     for stock in hsi_stocks:
#         output[stock] = generate_stock_data(stock, dates)

#     with open("hsi_12_day_intraday.json", "w") as f:
#         json.dump(output, f, indent=2)
#     print(f"✅ Data saved to: hsi_12_day_intraday.json")

# generate_json()

import json
import random
from datetime import datetime, timedelta

# Use a sample + filler list of HSI stocks
hsi_stocks = [
    "0001.HK", "0002.HK", "0003.HK", "0005.HK", "0006.HK", "0011.HK", "0012.HK", "0016.HK", "0017.HK",
    "0019.HK", "0023.HK", "0027.HK", "0066.HK", "0101.HK", "0108.HK", "0113.HK", "0129.HK", "0135.HK",
    "0144.HK", "0151.HK", "0175.HK", "0177.HK", "0207.HK", "0222.HK", "0231.HK", "0238.HK", "0267.HK",
    "0288.HK", "0291.HK", "0293.HK", "0308.HK", "0322.HK", "0386.HK", "0388.HK", "0606.HK", "0688.HK",
    "0700.HK", "0762.HK", "0803.HK", "0823.HK", "0836.HK", "0857.HK", "0883.HK", "0939.HK", "0941.HK",
    "0960.HK", "0968.HK", "0981.HK", "0992.HK", "1038.HK", "1044.HK", "1093.HK", "1109.HK", "1113.HK",
    "1171.HK", "1211.HK", "1299.HK", "1313.HK", "1336.HK", "1357.HK", "1378.HK", "1398.HK", "1928.HK",
    "1972.HK", "2007.HK", "2018.HK", "2313.HK", "2318.HK", "2319.HK", "2328.HK", "2331.HK", "2382.HK",
    "2388.HK", "2412.HK", "2628.HK", "2688.HK", "3690.HK", "3888.HK", "3988.HK", "6030.HK", "6098.HK",
    "6618.HK", "6690.HK", "6823.HK", "9618.HK", "9633.HK", "9988.HK", "9999.HK", "1024.HK"
]

# Two trading dates
target_dates = [datetime(2025, 8, 21), datetime(2025, 8, 22)]

# Trading minutes (HK market)
def get_intraday_minutes():
    minutes = []
    # Morning session
    current = datetime.strptime("09:30", "%H:%M")
    end = datetime.strptime("12:00", "%H:%M")
    while current < end:
        minutes.append(current.strftime("%H:%M"))
        current += timedelta(minutes=1)
    # Afternoon session
    current = datetime.strptime("13:00", "%H:%M")
    end = datetime.strptime("16:00", "%H:%M")
    while current < end:
        minutes.append(current.strftime("%H:%M"))
        current += timedelta(minutes=1)
    return minutes

intraday_minutes = get_intraday_minutes()

# Price spike config: (stock, datetime) -> % change
price_spike_config = {
    ("0001.HK", "2025-08-21 11:00"): 30,
    ("0002.HK", "2025-08-21 11:30"): 30,
    ("0003.HK", "2025-08-22 11:00"): 30,
    ("0005.HK", "2025-08-22 11:30"): 30,
}

# Volume spike config: (stock, datetime) -> multiplier
volume_spike_config = {
    ("9988.HK", "2025-08-21 15:59"): 100,
    ("9999.HK", "2025-08-22 15:59"): 100,
}

# Generate the data
def simulate_data():
    data = {}

    for stock in hsi_stocks:
        stock_data = []

        for date in target_dates:
            date_str = date.strftime("%Y-%m-%d")
            cumulative_return = 0.0
            cumulative_volume_ratio = 0.0001  # start small, simulate growth toward ~1.0–1.2
            max_normal_return = 0.0015  # for <15% total movement days
            max_normal_volume_increment = 0.0015  # to accumulate to ~1.0–1.2 by 15:59

            for time_str in intraday_minutes:
                full_timestamp = f"{date_str} {time_str}"
                key = (stock, full_timestamp)

                # --- PRICE LOGIC ---
                if key in price_spike_config:
                    cumulative_return = price_spike_config[key] / 100
                elif (stock, date_str) in [(s, dt_str.split(" ")[0]) for (s, dt_str) in price_spike_config.keys()]:
                    # If it's the same day as a spike for that stock but not the spike time, keep <15%
                    change = random.uniform(-max_normal_return, max_normal_return)
                    cumulative_return += change
                    cumulative_return = min(cumulative_return, 0.149)  # cap it
                else:
                    change = random.uniform(-max_normal_return, max_normal_return)
                    cumulative_return += change

                # --- VOLUME MULTIPLIER LOGIC ---
                if key in volume_spike_config:
                    cumulative_volume_ratio = volume_spike_config[key]
                else:
                    # If same day as a spike but not 15:59, cap below 2.0
                    if (stock, f"{date_str} 15:59") in volume_spike_config:
                        max_increment = 0.001
                    else:
                        max_increment = max_normal_volume_increment

                    cumulative_volume_ratio += random.uniform(0.0005, max_increment)
                    cumulative_volume_ratio = min(cumulative_volume_ratio, 1.5)

                stock_data.append({
                    "datetime": full_timestamp,
                    "stock": stock,
                    "price_change_percent": round(cumulative_return * 100, 3),
                    "volume_multiplier": round(cumulative_volume_ratio, 4)
                })

        data[stock] = stock_data

    return data

# Output to JSON
def generate_json():
    result = simulate_data()
    with open("hsi_aug21_22_final.json", "w") as f:
        json.dump(result, f, indent=2)
    print("✅ File saved as: hsi_aug21_22_final.json")

generate_json()
