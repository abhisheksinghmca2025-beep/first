# Prices and quantities
notebooks = 3
notebook_price = 45

pens = 2
pen_price = 20

# Total bill calculation
total_bill = (notebooks * notebook_price) + (pens * pen_price)

# Amount given by customer
amount_given = 500

# Remaining balance
balance = amount_given - total_bill

# Output
print("Total Bill Amount: ₹", total_bill)
print("Remaining Balance: ₹", balance)

# Output:
# Total Bill Amount: ₹ 175
# Remaining Balance: ₹ 325