# Program to check digit or alphabet

ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Special Character")

# Example Output:
# Enter a character: 5
# Digit