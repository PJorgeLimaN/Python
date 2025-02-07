# Program takes: Hour, Minutes, lenght of time in minutes. And shows when the "Timer" will end.

hour = int(input("Hour?\n"))
minutes = int(input("Minutes?\n"))

future = int(input("Advance by how many minutes?\n"))

minutes += future
hour += minutes // 60
minutes = minutes % 60
hour = hour % 24
print(hour, minutes, sep=":")