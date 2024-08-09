'''Write a Python program that takes an integer input from the user and prints whether the number is
positive, negative, or zero.'''

number = int(input("Enter the number:"))
if number == 0:
    print("The number is zero")
elif number > 0:
    print("The number is positive")
else:
    print("The number is negative")