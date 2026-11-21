# 6.  Write a program that will tell whether the number entered by the user is odd or even.

num = int(input('Enter a number : '))

result = 'EVEN' if num % 2 == 0 else 'ODD'
print(f'Given number is {result}')