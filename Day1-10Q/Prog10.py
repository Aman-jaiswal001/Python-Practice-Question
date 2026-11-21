# 10. Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit 

CP = float(input('Enter cost price of object : '))
SP = float(input('Enter selling price of object : '))

if SP >= CP : 
    print('Profit ',SP-CP)
else : 
    print('Loss ',CP-SP)