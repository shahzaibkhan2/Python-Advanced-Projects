# Import requests module to fetch api
import requests

# Define the API endpoint and your API key
endpoint = "https://openexchangerates.org/api/latest.json"
api_key = "your_api_key_here"

# Define the currencies you want to compare
base_currency = "USD"
target_currency = "EUR"

# Make the API request
response = requests.get(endpoint, params={"app_id": api_key, "base": base_currency})

# Check if the request was successful
if response.status_code != 200:
    print("Error:", response.status_code)
else:
    # Extract the exchange rate for the target currency
    rates = response.json()["rates"]
    target_rate = rates[target_currency]
    print(f"The exchange rate from {base_currency} to {target_currency} is {target_rate}.")
