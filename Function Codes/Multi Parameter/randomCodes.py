print('\n=== Section 5 - Multi Parameter Functions ===\n')

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

def lb_to_kg(lb):
    return lb * 0.45359237 # 1lb = 0.45359237 KG

#Feet and inches: 1 ft = 0.3048 m, and 1 in = 2.54 cm = 0.0254 m

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

''' First Version
def factorial_function(n): # Factorial Function
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
'''

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

def factorial(n):
    if n == 1: # The base case (termination condition.) 4 * (4-1) * (3-1) * (2-1) * 1
        return 1
    else:
        return n * factorial(n - 1) 

''' First Version
def fib(n): # Fibonacci Function
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
'''
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)



print('\n=== Module 4, Section 5, Part 1 - Multi Parameter Functions, BMI ===\n')

print(ft_and_inch_to_m(1, 1))
print(lb_to_kg(1))

print(bmi(352.5, 1.65))
print(bmi(52.5, 1.65))
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))) 

for n in range(1, 9):  # testing Factorial
    print(n, factorial_function(n))

for n in range(1, 15):  # testing Fibonacci
    print(n, "->", fib(n))

print(factorial(4)) # 4 * 3 * 2 * 1 = 24 