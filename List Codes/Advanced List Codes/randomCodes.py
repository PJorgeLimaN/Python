print('\n=== List Comprehension ===\n') # print('\n===  ===\n')

'''
 [expression for element in list if conditional] 
 OR
  for element in list:
    if conditional:
        expression 

EX: 
cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]


'''

row = ['WHITE_PAWN' for i in range(8)]

squares = [x ** 2 for x in range(10)]

twos = [2 ** i for i in range(8)]

odds = [x for x in squares if x % 2 != 0 ]

board = []

for i in range(8):
    row = ["_" for i in range(8)]
    board.append(row)
 # OR
'''
 board = [["_" for i in range(8)] for j in range(8)]


'''
board[0][0] = "RK"
board[0][7] = "RK"
board[7][0] = "RK"
board[7][7] = "RK"

board[4][2] = "KT"

board[3][4] = "P"

print(board, '\n\n')

for i in range(len(board)):
    print(board[i])

print('\n=== Multidimensional List ===\n')
'''
Then you take an arbitrary decision that the rows will record the readings every hour on the hour (so the row will have 24 elements) 
and each of the rows will be assigned to one day of the month (let's assume that each month has 31 days, so you need 31 rows). 
Here's the appropriate pair of comprehensions (h is for hour, d for day):
'''
# temps = [[0.0 for h in range(24)] for d in range(31)]

'''
Now it's time to determine the monthly average noon temperature. 
Add up all 31 readings recorded at noon and divide the sum by 31. 
You can assume that the midnight temperature is stored first.
'''
from random import randrange

temps = [[randrange(30) for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("The highest temperature was:", highest) 

hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "days were hot.") 

print('\n=== Three Dimensional Array ===\n')

'''
Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.

First step ‒ the type of the array's elements. In this case, a Boolean value (True/False) would fit.

Step two ‒ calm analysis of the situation. Summarize the available information: three buildings, 15 floors, 20 rooms.
'''
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

'''
The first index (0 through 2) selects one of the buildings; the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. 
All rooms are initially free.


'''
# Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:
rooms[1][9][13] = True
''' and release the second room on the fifth floor located in the first building: '''
rooms[0][4][1] = False
''' Check if there are any vacancies on the 15th floor of the third building: '''
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print(vacancy)

test_list = [i for i in range(-1, 2)]
print(test_list)



