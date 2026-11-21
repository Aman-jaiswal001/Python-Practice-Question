# 5.  Write a program that will reverse a four digit number.Also it checks whether the reverse is true. 

while True : 
    num = int(input('Enter a 4-digit number : '))
    if 1000 <= abs(num) <= 9999 :
        break
    print("Invalid input. Please enter a 4-digit number (e.g., 1221 or 4352)")


n = num

temp = 0

while n > 0 :
    digit = n % 10
    temp = (temp * 10) + digit
    n //= 10

print('reversed number : ',temp) # it show 1200 -> 21 only
print(f'reversed number : {temp:04d}') # it preserve zero like reverse 1200 -> 0021
