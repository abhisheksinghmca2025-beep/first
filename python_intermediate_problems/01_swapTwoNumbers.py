# Problem 1
# Problem Statement: Swap two numbers without using a third variable.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

# Input from user
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

# Before swapping values
print("Before swapping num1 :", num1)
print("Before swapping num2 :", num2)

# ---------------- SWAPPING LOGIC ----------------
# Step 1: Add both numbers and store in num1
# Formula: num1 = num1 + num2
# Example: num1=10, num2=20 → num1 becomes 30
num1 = num1 + num2

# Step 2: Subtract original num2 from new num1 to get original num1
# Formula: num2 = num1 - num2
# Example: num2 = 30 - 20 = 10
num2 = num1 - num2

# Step 3: Subtract new num2 from num1 to get original num2
# Formula: num1 = num1 - num2
# Example: num1 = 30 - 10 = 20
num1 = num1 - num2

# Now values are swapped

# After swapping values
print("After swapping num1 :", num1)
print("After swapping num2 :", num2)


# ---------------- OUTPUT EXAMPLE ----------------
# Enter first number : 10
# Enter second number : 20
#
# Before swapping num1 : 10
# Before swapping num2 : 20
#
# After swapping num1 : 20
# After swapping num2 : 10


# ---------------- LOGIC SUMMARY ----------------
# Suppose:
# num1 = 10
# num2 = 20
#
# Step 1:
# num1 = num1 + num2
# num1 = 10 + 20 = 30
#
# Step 2:
# num2 = num1 - num2
# num2 = 30 - 20 = 10  ← original num1 stored in num2
#
# Step 3:
# num1 = num1 - num2
# num1 = 30 - 10 = 20  ← original num2 stored in num1
#
# FINAL RESULT:
# num1 = 20
# num2 = 10
#
# Swapping done without using third variable.