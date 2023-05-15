# Function for dollar to pound
def dollar_to_pound(amount):
    return amount * 0.72

# Function for pound to yuan
def pound_to_yuan(amount):
    return amount * 8.78

# Function for dollar to yuan
def dollar_to_yuan(amount):
    return amount * 6.43

# Function for dollar to yen
def dollar_to_yen(amount):
    return amount * 110.02

# Function for yen to dollar
def yen_to_dollar(amount):
    return amount * 0.0091

# Function for yen to pound
def yen_to_pound(amount):
    return amount * 0.0065

# Function for pound to yen
def pound_to_yen(amount):
    return amount * 153.52

# Function for pound to dollar
def pound_to_dollar(amount):
    return amount * 1.39

# Function for yuan to dollar
def yuan_to_dollar(amount):
    return amount * 0.16

# Function for yuan to pound
def yuan_to_pound(amount):
    return amount * 0.11

# Conversion examples for usage
usd_amount = 100
pounds_amount = 50
yuan_amount = 200
yen_amount = 5000

print(f"{usd_amount} USD = {dollar_to_pound(usd_amount):.2f} GBP")
print(f"{pounds_amount} GBP = {pound_to_yuan(pounds_amount):.2f} CNY")
print(f"{usd_amount} USD = {dollar_to_yuan(usd_amount):.2f} CNY")
print(f"{usd_amount} USD = {dollar_to_yen(usd_amount):.2f} JPY")
print(f"{yen_amount} JPY = {yen_to_dollar(yen_amount):.2f} USD")
print(f"{yen_amount} JPY = {yen_to_pound(yen_amount):.2f} GBP")
print(f"{pounds_amount} GBP = {pound_to_yen(pounds_amount):.2f} JPY")
print(f"{pounds_amount} GBP = {pound_to_dollar(pounds_amount):.2f} USD")
print(f"{yuan_amount} CNY = {yuan_to_dollar(yuan_amount):.2f} USD")
print(f"{yuan_amount} CNY = {yuan_to_pound(yuan_amount):.2f} GBP")
