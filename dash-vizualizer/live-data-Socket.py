# live price via websocket.
# https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams
# The base endpoint is: wss://stream.binance.us:9443

# npm install -g wscat
# try to wscat -c wss://stream.binance.us:9443/ws/ethusdt@kline_5m

from websocket import create_connection

# Launch the connection to the server.
ws = create_connection('wss://stream.binance.us:9443/ws/ethusdt@kline_1m')

# Printing all the result
while True:
    try:
        result = ws.recv()
        print(result)
    except Exception as e:
        print(e)
        break

# Advanced Method

SOCKET = "wss://stream.binance.us:9443/ws/ethusdt@kline_1m"

x=df['Open time']
opens=df['Open']
high=df['High']
low=df['Low']
close=df['Close']

try:
    import thread
except ImportError:
    import _thread as thread

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_error(ws, error):
    print(error)

def on_message(ws, message):
    print(message)
    json_message = json.loads(message)
    df = pd.DataFrame.from_dict(json_message)

if __name__ == '__main__':
    
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_error = on_error, on_message=on_message)