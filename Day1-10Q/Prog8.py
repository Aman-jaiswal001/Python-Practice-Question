# 8.  Write a program to find the euclidean distance between two coordinates
# if 2 coordinate is (x1,y1) and (x2,y2) the d = underroot{(x2-x1)**2 + (y2 - y1)**2}

import math as m

x1 = int(input('enter x1 coordinate : '))
y1 = int(input('enter y1 coordinate : '))
x2 = int(input('enter x2 coordinate : '))
y2 = int(input('enter y2 coordinate : '))

# d = m.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
d = m.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f'Euclidean distance between coordinates {x1,y1} and {x2,y2} is {d}')