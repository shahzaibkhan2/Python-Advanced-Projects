# import forex_python module
from forex_python.converter import CurrencyRates

# Create a CurrencyRates object
c = CurrencyRates()

# Convert 200 USD to EUR
usd_amount = 200
eur_amount = c.convert('USD', 'EUR', usd_amount)
print(f"{usd_amount} USD = {eur_amount} EUR")

# Convert 1000 JPY to USD
jpy_amount = 1000
usd_amount = c.convert('JPY', 'USD', jpy_amount)
print(f"{jpy_amount} JPY = {usd_amount} USD")
