# Problem 34
# Problem Statement: Find sum of first N natural numbers.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

num = int(input("Enter a number : "))
totalSum = 0

for i in range(1, num+1):
    totalSum = totalSum + i

print("Sum of first ", num, " natural numbers is : ", totalSum)


# ---------------- OUTPUT EXAMPLE ----------------
# Enter a number : 5
# Sum of first  5  natural numbers is :  15


# ---------------- HOW IT WORKS ----------------
# If user enters 5

# Loop runs from 1 to 5
# i = 1 → totalSum = 0 + 1 = 1
# i = 2 → totalSum = 1 + 2 = 3
# i = 3 → totalSum = 3 + 3 = 6
# i = 4 → totalSum = 6 + 4 = 10
# i = 5 → totalSum = 10 + 5 = 15

# Final Output:
# Sum = 15