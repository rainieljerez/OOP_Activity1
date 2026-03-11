#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
print ("This program prints the bigger number.")
#user is asked to input 2 numbers
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
#conditons then print results
if num1 > num2:
    print (str(num1) + " is the bigger number")
elif num1 == num2:
    print ("Both numbers are equal")
else:
    print (str(num2) + " is the bigger number")