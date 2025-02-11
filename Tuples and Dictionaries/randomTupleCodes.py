tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000) # Tuples cannot be modified (i.e have elements added/appended or removed/deleted), but can be used to create new variables.
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)