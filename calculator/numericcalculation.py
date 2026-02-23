# Numeric Calculation Program

# input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# division check
if num2 != 0:
    division = num1 / num2
else:
    division = "Not possible"

square1 = num1 ** 2
cube1 = num1 ** 3

average = (num1 + num2) / 2

# display results
print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)
print("Square of first number =", square1)
print("Cube of first number =", cube1)
print("Average =", average)


# Example Output:
# Enter first number: 10
# Enter second number: 5
# Addition = 15.0
# Subtraction = 5.0
# Multiplication = 50.0
# Division = 2.0
# Square of first number = 100.0
# Cube of first number = 1000.0
# Average = 7.5