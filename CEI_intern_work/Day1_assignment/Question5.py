# Create a program that checks if a given year is a leap year.
year = int(input("Enter year:"))

if year % 100 != 0 and year % 4 == 0:
    print("Leap Year")

elif year % 400 == 0:
    print("Leap Year")


else:
    print("Non leap year")