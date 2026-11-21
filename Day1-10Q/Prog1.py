# 1.  User will input (3ages).Find the oldest one

age1 = int(input("Enter the first age: "))
age2 = int(input("Enter the second age: "))
age3 = int(input("Enter the third age: "))

oldest = max(age1, age2, age3)
print("The oldest age is:", oldest)
