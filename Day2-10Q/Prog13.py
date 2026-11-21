# 13. Write  a program that will tell whether the given number is divisible by 3 & 6. 

num = int(input('Enter a number : '))

if num % 6 == 0 :
    print(f"{num} is divisible by both 3 and 6.")
elif num % 3 == 0:
    print(f'{num} is divisible by 3, but not by 6.')
else:
    print(f'{num} is not divisible by 3 and 6.')
