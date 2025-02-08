'''
Your task is to write and test a function which takes two arguments (a year and a month) 
and returns the number of days for the given year-month pair (while only February is sensitive to the year value, your function should be universal).

The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). It may be very helpful. 
We encourage you to use a list filled with the months' lengths. You can create it inside the function ‒ this trick will significantly shorten the code.

We've prepared a testing code. Expand it to include more test cases.
'''

def is_year_leap(year):
    if year % 4 != 0:
        return False
        #common
    elif year % 100 != 0:
        return True
        #leap
    elif year % 400 != 0:
        return False
        #common
    else:
        return True
        #leap

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12: return None

    # print("=== Days In Month Function")
    threeOneDays = [1, 3, 5 ,7, 8, 10, 12]
    threeZeroDays = [4, 6, 9, 11]
    year = is_year_leap(year)
    # print(is_year_leap(year), month)
    if month in threeOneDays:
        return 31
    elif month in threeZeroDays:
        return 30
    elif month == 2:
        if year == False:
            return 28
        else: return 29

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    # print(result)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
