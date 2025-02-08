'''
Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, 
or returns None if any of the arguments is invalid.

Use the previously written and tested functions. Add your own test cases to the code.
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
    # print(is_year_leap(year), month)
    if month in threeOneDays:
        return 31
    elif month in threeZeroDays:
        return 30
    elif month == 2:
        if is_year_leap(year):
            return 28
        else: return 29
    else: return None

def day_of_year(year, month, day):
    days = 0

    if (days_in_month(year, month) - day) < 0:
        return None
    
    for mon in range(1, month):
        days += days_in_month(year ,mon)
        # print(mon)
        # print(days_in_month(year ,mon))
        # print(f'Month {mon} added {days_in_month(year, mon)} days. \nDays total is {days}')

    days += day

    return days

print('Days in year: ', day_of_year(2004, 10, 1))
print('Days in year: ', day_of_year(2000, 12, 31))
print('Days in year: ', day_of_year(1984, 2, 28))
print('Days in year: ', day_of_year(2023, 1, 5))
print('Days in year: ', day_of_year(2023, 5, 15))

