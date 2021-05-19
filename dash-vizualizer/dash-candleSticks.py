import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as plot
import pandas as pd
import requests 
import json
import os
import websocket

def url_build(symbol="ETHUSDT", interval="5m"):
    url_base = "https://api.binance.com"
    url_endpoint = "/api/v1/klines"
    url_final = url_base + url_endpoint + "?symbol={}&interval={}".format(symbol,interval)
    return url_final

response = requests.get(url_build())
response_req = json.loads(response.text)

df = pd.DataFrame.from_dict(response_req)

candle_columns = [
    "Open time",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Close Time",
    "Quote asset volume",
    "Number of Trades",
    "Taker buy base asset volume",
    "Taker buy quote asset volume",
    "Ignore."
]

df.columns = candle_columns
df['Open time'] = pd.to_datetime(df['Open time'],unit='ms')

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1000,
            n_intervals = 0
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
        [Input('graph-update', 'n_intervals')])

def update_graph_scatter(n):
    fig = plot.Figure(data=[plot.Candlestick(
        x=df['Open time'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'])])
    
    fig.update_layout(autosize=True,height=1000)
    return fig

if __name__ == '__main__':
    
    #websocket.enableTrace(True)
    #ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_error = on_error, on_message=on_message)
    #print(ws.on_message)
    app.run_server(debug=True)
    ws.run_forever()
