'''
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

print(my_list)

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            print(f"Swapping {my_list[i]} with {my_list[i + 1]}")
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

'''

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            print(f"Swapping {my_list[i]} with {my_list[i + 1]}")
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

print('\n=== Python Sort Function ===\n')

sortedList = [10, 8, 19, 2, 4, 1]
print(sortedList)

sortedList.sort()

print(sortedList)

