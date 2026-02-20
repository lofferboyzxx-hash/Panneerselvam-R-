# Program to calculate factorial of a number

# Taking input from the user
num = int(input("Enter a number: "))

# Checking if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print("The factorial of", num, "is:", factorial)
