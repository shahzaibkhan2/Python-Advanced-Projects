# The code which is need to be debugged
def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    average = total / count
    return average

numbers = [5, 6, 3, 4, 8]
test = calculate_average(numbers)
print("The average is: " + test)




# Debugged code
def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    average = total / count
    return average

numbers = [5, 6, 3, 4, 8]
test = calculate_average(numbers)
print("The average is: " + str(test))
