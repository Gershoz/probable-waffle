#Credits - https://youtu.be/3oRF8hgEXmU - lines 2-17,20
from binance.client import Client #pip install python-binance
import unicorn_binance_websocket_api #pip install unicorn-binance-websocket-api
import time

client = Client()
info = client.get_exchange_info()

symbols = [i['symbol'] for i in info['symbols'] if i['symbol'].endswith('USDT')]
symbols = [i.lower() for i in symbols]

ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
ubwa.create_stream(['kline_1m'], symbols, output="UnicornFy")

count = 0 
while count<10:
    data = ubwa.pop_stream_data_from_stream_buffer()
    if data is not False:
        count = count + 1
        print(data)

# import spark to measure dataframe size in mb

# learn dictionaries to clean datafreame 