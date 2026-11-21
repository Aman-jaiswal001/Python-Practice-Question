# 17. Write a program that will take three digits from the user and add the square of each digit.

while True : 
    num = int(input('Enter a 3-digit number : '))
    if 100 <= abs(num) <= 999 :
        break
    print("Invalid input. Please enter a 3-digit number (e.g., 122 or 432)")

ones = num % 10
tens = (num // 10) % 10
hundredth = num // 100

print('Sum of square of each digit : ', ones**2 + tens**2 + hundredth**2)