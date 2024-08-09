# Create a program that takes user input to add multiple elements to an array, then prints the final array. 

arr = [1,2,3,4, 5]
lis = list(input("Enter elements:").split(' '))
final_arr = arr + lis

print(final_arr)