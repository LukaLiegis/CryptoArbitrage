import numpy as np
import pandas as pd
import ccxt

def getprices(exchange, symbol):
    inst = getattr(ccxt, exchange)
    df = pd.DataFrame(inst.fetchOHLCV(symbol, limit=60)) # 60 minutes
    df.columns = ["Time", "Open", "High", "Low", "Close", "Volume"]
    df.set_index("Time", inplace=True)
    df.index = pd.to_datetime(df.index, unit="ms")
    df = df.astype(float)
    return df

prices = []
fails = []

for exchange in ccxt.exchanges:
    try:
        prices.append(getprices(exchange, "BTC/USDT"))
        print("Prices successfully pulled from "+exchange)
    except:
        fails.append(exchange)
        print("Price pull failed for "+exchange)
