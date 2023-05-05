import json

# Prompt the user for input
name = input("What is your name? ")
age = input("What is your age? ")
phone = input("What is your phone number? ")
email = input("What is your email? ")

# Create a dictionary to store the user's information
user_info = {
    "Name": name,
    "Age": age,
    "Phone": phone,
    "Email": email
}

# Save the user's information to a JSON file
with open("user_info.json", "w") as file:
    json.dump(user_info, file)

print("User info saved to user_info.json")
