# Program to check whether triangle is valid or not

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")


# Example Output 1:
# Enter first angle: 60
# Enter second angle: 60
# Enter third angle: 60
# Valid triangle

# Example Output 2:
# Enter first angle: 90
# Enter second angle: 45
# Enter third angle: 30
# Invalid triangle