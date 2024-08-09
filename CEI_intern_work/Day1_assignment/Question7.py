# Create a program that prints the multiplication table of a given number using a while loop.
num = int(input("Enter a number:"))
i = 1
while i < 11:
    print(num, "*", i, "=", num*i)
    i+=1