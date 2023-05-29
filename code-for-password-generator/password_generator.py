import random

characters = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_"]

while True:
    pass_length = int(input("please enter your password length: "))
    pass_count = int(input("please enter number of passwords required:  "))

    for i in range(0, pass_count):
        password = ""
        for j in range(0, pass_length):
            pass_char = random.choice(characters)
            password = password + pass_char
        print(f"your generated password is: ", password)
    repeating = input("do you want more passwords? ")
    if repeating == "no" or repeating == "No" or repeating == "NO":
        break
print("thank you very much!! have a good day")