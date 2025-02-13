for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.
 
numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents. 

print("\nList length:", len(numbers))  # Printing the list's length.

print(numbers)  # Printing the whole list.

del numbers[1]
print(len(numbers))
print(numbers)

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

print('\n=== ===\n')

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
print('\n=== New List ===\n')

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i * 2 + 1) 

print(my_list)

print('\n=== Using For on List ===\n')

total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

print('\n=== Using For in List ===\n')

my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
    print(f"{i}, ", end="")
 
print("\n",total) 

variable_1 = 1
variable_2 = 2

print('\n=== Changing values ===\n')

print(variable_1, variable_2)

variable_1, variable_2 = variable_2, variable_1

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

'''

    we've assigned the length variable with the current list's length (this makes our code a bit clearer and shorter)
    we've launched the for loop to run through its body length // 2 times (this works well for lists with both even and odd lengths, 
    because when the list contains an odd number of elements, the middle one remains untouched)
    we've swapped the ith element (from the beginning of the list) with the one with an index equal to (length - i - 1) (from the end of the list); 
    in our example, for i equal to 0 the (length - i - 1) gives 4; for i equal to 1, it gives 3 ‒ this is exactly what we needed.

'''
print(my_list)

print('\n=== In and Not In ===\n')

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

print('\n=== Highest Number in a list ===\n')


my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)

# print('\n===  ===\n')

print('\n=== Finding a number in a List ===\n') 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Element found at index", i)
else:
    print("absent")
 
print('\n=== Lottery Check ===\n')

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

print('\n=== Random Number Generator ===\n')

from random import randrange 

for i in range(10):    print(randrange(8))