# 11.  Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

P = float(input('Enter principle amount : '))
R = float(input('Enter Rate of interest : '))
T = int(input('Enter Time(month) : '))

print('Simple interest :',(P*R*T)/1000)