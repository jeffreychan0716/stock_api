# import time
# import requests
# import json
# import urllib.parse

# # Extra headers
# test_headers = {
#     'Content-Type': 'application/json'
# }

# '''
# # Special Note:
# # GitHub: https://github.com/alltick/realtime-forex-crypto-stock-tick-finance-websocket-api
# # Token Application: https://alltick.co
# # Replace "testtoken" in the URL below with your own token
# # API addresses for forex, cryptocurrencies, and precious metals:
# # https://quote.alltick.io/quote-b-ws-api
# # Stock API address:
# # https://quote.alltick.io/quote-stock-b-ws-api
# Encode the following JSON and copy it to the "query" field of the HTTP query string
# {"trace": "python_http_test1", "data": {"code": "700.HK", "kline_type": 1, "kline_timestamp_end": 0, "query_kline_num": 2, "adjust_type": 0}}
# {"trace": "python_http_test2", "data": {"symbol_list": [{"code": "700.HK"}, {"code": "UNH.US"}]}}
# {"trace": "python_http_test3", "data": {"symbol_list": [{"code": "700.HK"}, {"code": "UNH.US"}]}}
# '''

# payload = {
# #   "trace": "c2a8a146-a647-4d6f-ac07-8c4805bf0b74",
#   "data": {
#     "data_list": [
#       {
#         "code": "700.HK",
#         "kline_type": 1,
#         "kline_timestamp_end": 0,
#         "query_kline_num": 1,
#         "adjust_type": 0
#       }
#     ]
#   }
# }

# # Final URL
# test_url1 = f'https://quote.alltick.io/quote-stock-b-api/batch-kline?token=43edd3607624576fb682301db1165c5e-c-app'
# # test_url2 = 'https://quote.alltick.io/quote-stock-b-api/depth-tick?token=43edd3607624576fb682301db1165c5e-c-app&query=%7B%22trace%22%20%3A%20%22python_http_test2%22%2C%22data%22%20%3A%20%7B%22symbol_list%22%3A%20%5B%7B%22code%22%3A%20%22700.HK%22%7D%2C%7B%22code%22%3A%20%22UNH.US%22%7D%5D%7D%7D'
# # test_url3 = 'https://quote.alltick.io/quote-stock-b-api/trade-tick?token=43edd3607624576fb682301db1165c5e-c-app&query=%7B%22trace%22%20%3A%20%22python_http_test3%22%2C%22data%22%20%3A%20%7B%22symbol_list%22%3A%20%5B%7B%22code%22%3A%20%22700.HK%22%7D%2C%7B%22code%22%3A%20%22UNH.US%22%7D%5D%7D%7D'

# resp1 = requests.post(url=test_url1, headers=test_headers)
# print(resp1.url)
# # time.sleep(1)
# # resp2 = requests.get(url=test_url2, headers=test_headers)
# # time.sleep(1)
# # resp3 = requests.get(url=test_url3, headers=test_headers)

# # Decoded text returned by the request
# text1 = resp1.text
# print(text1)

# # text2 = resp2.text
# # print(text2)

# # text3 = resp3.text
# # print(text3)

import requests

# Payload
payload = {
    "data": {
        "data_list": [
            {
                "code": "700.HK",
                "kline_type": 1,
                "kline_timestamp_end": 0,
                "query_kline_num": 1,
                "adjust_type": 0
            }
        ]
    }
}

# URL and headers
test_url1 = 'https://quote.alltick.io/quote-stock-b-api/batch-kline?token=43edd3607624576fb682301db1165c5e-c-app'
test_headers = {
    'Content-Type': 'application/json'
}

# POST request with payload in body
resp1 = requests.post(url=test_url1, headers=test_headers, json=payload)

# Output
print(resp1.url)
print(resp1.text)
