import ccxt

binance = ccxt.binance()

binance.options = {'defaultType': 'future',
                    'adjustForTimeDifference': True}

symbol = 'BTCUSDT'

funding = binance.fetch_funding_rate(symbol)

print(funding)