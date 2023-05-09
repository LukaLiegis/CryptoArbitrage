import numpy as np
import pandas as pd
import ccxt

binance = ccxt.binance()
market_binance = binance.load_markets()
print(list(market_binance.items())[:3])

