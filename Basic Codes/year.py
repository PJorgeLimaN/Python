year = int(input("Enter a year: "))

   # if the year number isn't divisible by four, it's a common year;
  #  otherwise, if the year number isn't divisible by 100, it's a leap year;
 #   otherwise, if the year number isn't divisible by 400, it's a common year;
#    otherwise, it's a leap year.

#It would be good to verify if the entered year falls into the Gregorian era, 
#and output a warning otherwise: Not within the Gregorian calendar period.

if year < 1582:
	print("Not within the Gregorian calendar period")
#  Write the if-elif-elif-else block here.
if year % 4 != 0:
    print(f'The year {year} is a Common Year')
    #common
elif year % 100 != 0:
    print(f'The year {year} is a Leap Year')
    #leap
elif year % 400 != 0:
    print(f'The year {year} is a Common Year')
    #common
else:
    print(f'The year {year} is a Leap Year')
    #leap
    
    
    
    
    