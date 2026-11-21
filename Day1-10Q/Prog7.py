# 7.  Write a program that will tell whether the given year is a leap year or not. 
import calendar

year = int(input('Enter year to check leap year or not : '))

# method 1 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print('given year is Leap year')
else : 
    print('given year is not leap year')

# method 2 
if calendar.isleap(year) : 
    print(f"{year} is a leap year")
else : 
    print(f"{year} is not a leap year")

