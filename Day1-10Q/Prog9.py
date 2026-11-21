# 9.  Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not. 

print('Enter positive value only')
angle1 = float(input('Enter 1st angle : '))
angle2 = float(input('Enter 2nd angle : '))
angle3 = float(input('Enter 3rd angle : '))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and ( angle1 + angle2 + angle3 == 180) : 
    print('Given all three angle form a triangle')
else : 
    print('Given angle not form a triangle')


