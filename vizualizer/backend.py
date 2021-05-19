from flask import Flask, render_template, request, flash, redirect, jsonify
import config, csv, datetime
from binance.client import Client
from binance.enums import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = Client(config.API_KEY, config.API_SECRET, tld='us')

# CMD W10: 
# > set FLASK_APP=backend.py
# > flask run

@app.route('/')
def index():
    title = 'Visualizer'

    #account = client.get_account()
    #balances = account['balances']

    #exchange_info = client.get_exchange_info()
    #symbols = exchange_info['symbols']

    #return render_template('index.html', title=title, my_balances=balances, symbols=symbols)

    return render_template('index.html', title=title)

@app.route('/history')
def history():
    # https://python-binance.readthedocs.io/en/latest/market_data.html
    candlesticks = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_30MINUTE, "May 17, 2021, UTC")

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = { 
            "time": data[0] / 1000, 
            "open": data[1],
            "high": data[2], 
            "low": data[3], 
            "close": data[4]
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)

# Private functionalities atm 
@app.route('/buy', methods=['POST'])
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'