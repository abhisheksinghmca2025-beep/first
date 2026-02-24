# Program to swap two numbers without using third variable

# input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# swapping without third variable
a = a + b
b = a - b
a = a - b

# output
print("After swapping:")
print("First number =", a)
print("Second number =", b)

# Example Output:
# Enter first number: 10
# Enter second number: 20
# After swapping:
# First number = 20
# Second number = 10