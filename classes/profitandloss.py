# Program to calculate Profit or Loss

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    profit = sp - cp
    print("Profit =", profit)

elif cp > sp:
    loss = cp - sp
    print("Loss =", loss)

else:
    print("No Profit No Loss")


# Example Output 1 (Profit case):
# Enter Cost Price: 500
# Enter Selling Price: 650
# Profit = 150.0


# Example Output 2 (Loss case):
# Enter Cost Price: 800
# Enter Selling Price: 600
# Loss = 200.0


# Example Output 3 (No profit no loss case):
# Enter Cost Price: 400
# Enter Selling Price: 400
# No Profit No Loss