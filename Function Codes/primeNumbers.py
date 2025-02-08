'''
A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.

Complicated? Not at all. For example, 8 isn't a prime number, as you can divide it by 2 and 4 (we can't use divisors equal to 1 and 8, as the definition prohibits this).

On the other hand, 7 is a prime number, as we can't find any legal divisors for it.

Your task is to write a function checking whether a number is prime or not.

The function:

    is called is_prime;
    takes one argument (the value to check)
    returns True if the argument is a prime number, and False otherwise.

Hint: try to divide the argument by all subsequent values (starting from 2) and check the remainder ‒ if it's zero, your number cannot be a prime; 
think carefully about when you should stop the process.

If you need to know the square root of any value, you can utilize the ** operator. Remember: the square root of x is the same as x**0.5

Complete the code in the editor.

Run your code and check whether your output is the same as ours.
THEIR CODE

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

What is happening here? Why is this happening here?

'''


def is_prime(num):
    prime = False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

for i in range(1, 100):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
