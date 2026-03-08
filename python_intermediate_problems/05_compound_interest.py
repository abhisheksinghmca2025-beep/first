# Program to calculate compound interest

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (years): "))

amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest =", ci)

# Example Output:
# Enter principal amount: 1000
# Enter rate of interest: 10
# Enter time (years): 2
# Compound Interest = 210.00000000000023