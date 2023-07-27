def perfect(num):
    """ A function which finds whether the given number is perfect number or not
    Input: Give it a number 
    Output: Given number is not a perfect number """

    summ = 0
    
    for i in range(1, num):
        if num%i == 0:
            summ += i
    if summ == num:
        print(num, "Is a perfect number")
    else:
        print(num, "Is not a perfect number")

perfect(5)