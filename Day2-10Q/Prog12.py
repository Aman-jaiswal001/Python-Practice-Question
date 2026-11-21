# 12. Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

import math as m

r = float(input('Enter radius of cylinder : '))
h = float(input('Enter height of cylinder : '))

volume = m.pi * (r**2) * h
#convert cm cubic to liter
v_litre = volume / 1000
Total_cost = v_litre * 40
print(f'Volume of cylinder : {volume:.2f}')
print(f'cost of milk : {Total_cost:.2f}Rs')