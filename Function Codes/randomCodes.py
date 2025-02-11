print('\n===  ===\n')

def gibMess():
    valu = input("Enter a value: ") # Changed from original print-only
    return valu # My Addition

print('\n=== Parameters ===\n')
def message(what, number):
    print("Enter", what, "number", number)
''' These two numbers (above and below) are different '''
number = 1234 
print(number)

message("telephone", 11)
message("price", 5)
message("number", "number")

# mess = gibMess()

# print(mess)

print('\n=== Positional Parameters ===\n')
# Parametrized Functions, Extra Details. Such as Default Value
def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Anakin")

introduction("Henry")
introduction(first_name="William")
introduction(last_name="Hopkins")

print('\n=== The Return Instruction ===\n')

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")
'''
happy_new_year()
happy_new_year(False)
'''

def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)

def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")

print('\n=== Lists and Functions ===\n')

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

print('\n=== Global Keyword ===\n')

def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)

print('\n=== Function and Argument Interactions ===\n')

def my_function(n):
    print("I got", n)
    n += 1 
    ''' A function should only change a variable if it returns its value.'''
    print("I have", n)

var = 1
my_function(var)
print(var)

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

