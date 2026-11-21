# 4.  Write a program that will give you the sum of 3 digits

num = int(input("Enter a three-digit number: "))
num = abs(num) # protect from negative number
# Method 1 Suitable for Python Program
# Extracting the digits
hundredth = num // 100
tens = (num // 10) % 10
units = num % 10

sum = hundredth + tens + units
print(f'sum of {hundredth} + {tens} + {units} = {sum}')

#method 2 suitable for other programming languages also
num = int(input('Enter a 3-digit number : '))
n = num

digit_sum = 0

while num > 0:
    digit = num % 10 # get last digit
    digit_sum += digit
    num //= 10 # Drop last digit

print(f'Sum of digits of {n} is : {digit_sum}')
