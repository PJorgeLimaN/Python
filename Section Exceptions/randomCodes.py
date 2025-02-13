'''
value = int(input('Enter a natural number: '))
print('The reciprocal of', value, 'is', 1/value) #Definitivamente não dará erro se colocar letra.

try:
	# It's a place where
	# you can do something 
    # without asking for permission.
except:
	# It's a spot dedicated to 
    # solemnly begging for forgiveness.
'''

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I don\'t think this is a number.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 
except: # Remember the default option, musch like with Else, MUST BE the last oone
    print('Something strange has happened here... Sorry!')

try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")




