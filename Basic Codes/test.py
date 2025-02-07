## input a float value for variable a here
#a = float(input("Insert Variable A: "))
## input a float value for variable b here
#b = float(input("Insert Variable B: "))
#
## output the result of addition here
#print("The result of " + str(a) + " + " + str(b) + " is ", (a+b))
## output the result of subtraction here
#print("The result of " + str(a) + " + " + str(b) + " is ", (a-b))
## output the result of multiplication here6
#print("The result of " + str(a) + " + " + str(b) + " is ", (a*b))
## output the result of division here
#print("The result of " + str(a) + " + " + str(b) + " is ", (a/b))
#
#print("\nThat's all, folks!")


#Question 15, Module 2 Completion Test
x = int(input("Value of X: "))
y = int(input("Value of Y: "))

print("Step; Value X; Value Y")

print(0, x, y, sep="; ")
x = x % y
print(1, x, y, sep="; ")
x = x % y
print(2, x, y, sep="; ")
y = y % x
print(3, x, y, sep="; ")

print("Final value of Y: " + str(y))

