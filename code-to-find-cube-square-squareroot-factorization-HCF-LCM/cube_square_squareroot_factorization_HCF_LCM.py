# Import math module
import math

# define a function for cube
def cube(num):
    return num**3

# define a function for square
def square(num):
    return num**2

# define a function for square root
def square_root(num):
    return math.sqrt(num)

# define a function for factorization
def factors(num):
    factors_list = []
    for i in range(1, num+1):
        if num % i == 0:
            factors_list.append(i)
    return factors_list

# define a function for HCF
def hcf(num1, num2):
    return math.gcd(num1, num2)

# define a function for LCM
def lcm(num1, num2):
    return (num1 * num2) // math.gcd(num1, num2)

# Example for usage
num = 12
print(f"Cube of {num} is: {cube(num)}")
print(f"Square of {num} is: {square(num)}")
print(f"Square root of {num} is: {square_root(num)}")
print(f"Factors of {num} are: {factors(num)}")
print(f"HCF of 24 and 36 is: {hcf(28, 56)}")
print(f"LCM of 24 and 36 is: {lcm(34, 66)}")
