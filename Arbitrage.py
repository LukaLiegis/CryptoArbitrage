import numpy as np
import pandas as pd
import ccxt

# Getting Binance market data
binance = ccxt.binance()
market_binance = binance.load_markets()

# Getting OKX market data
okx = ccxt.okx()
okx_market = okx.load_markets()

print(binance.fetch_ticker("DOGE/USDT"))