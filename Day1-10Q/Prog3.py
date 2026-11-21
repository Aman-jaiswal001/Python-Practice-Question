# 3.  User will input (2numbers).Write a program to swap the numbers 

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
print('Before swapping')
print(f'num1 : {num1}, num2 : {num2}')

print('After swapping')
# method 1
num1 , num2 = num2, num1
print(f'num1 : {num1}, num2 : {num2}')

# method 2
temp = num1
num1 = num2
num2 = temp
print(f'num1 : {num1}, num2 : {num2}')

# method 3
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f'num1 : {num1}, num2 : {num2}')
