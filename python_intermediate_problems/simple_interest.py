# Program to calculate simple interest

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (years): "))

si = (p * r * t) / 100

print("Simple Interest =", si)

# Example Output:
# Enter principal amount: 1000
# Enter rate of interest: 5
# Enter time (years): 2
# Simple Interest = 100.0