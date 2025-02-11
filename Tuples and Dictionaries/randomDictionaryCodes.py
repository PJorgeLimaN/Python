# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
phone_numbers = {'boss': 5551234567,
              'Suzy': 22657854310
}

empty_dictionary = {}
words = ['cat', 'lion', 'horse'] 

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

'''
    if the key is a string, you have to specify it as a string;
    keys are case-sensitive: 'Suzy' is something different from 'suzy'.
'''

print(dictionary['cat'])
print(phone_numbers['Suzy'])

dictionary['cat'] = 'minou'


for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary") 

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

for english, french in dictionary.items(): # Returns Keys and Values
    print(english, "->", french) 

dictionary['swan'] = 'cygne' #Adding items to Dictionaries 1
dictionary.update({"duck": "canard"}) #Adding items to Dictionaries 2

del dictionary['dog']  # Removing from Dictionaries (Specify the Key, and it removes Key AND Value)

dictionary.popitem() # Removes the last item in the dictionary, In older versions, removes a random item.

for french in dictionary.values():
    print(french) 

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)

colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)

