import alpha_vantage
from alpha_vantage.timeseries import TimeSeries

# Replace YOUR_API_KEY with your Alpha Vantage API key
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')

# Replace SYMBOL with the stock symbol you want to retrieve (e.g. MS for Microsoft)
symbol = 'SYMBOL'

# Retrieve the daily stock prices for the symbol you want
data, meta_data = ts.get_daily(symbol=symbol)

# Print the last 5 rows of the data
print(data.tail())
