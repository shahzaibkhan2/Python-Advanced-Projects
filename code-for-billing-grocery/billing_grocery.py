# Defining the products and their prices
products_for_billing = {"apple": 2, "banana": 1.5, "orange": 3, "grape": 4, "dates": 5, "pineapples": 6, "mangoes": 4.3}

# Defining a function to calculate the total cost of items purchased
def calculate_total(items):
    total = 0.0
    for item in items:
        if item in products_for_billing:
            total += products_for_billing[item]
        else:
            print(f"Invalid item: {item}")
    return total

# Let the user to enter their items
items = input("Enter the items purchased, separate them by commas: ")
items = items.split(",")

# Calculate the total cost
total = calculate_total(items)

# Print the total cost
print(f"Total cost: ${total:.2f}")
