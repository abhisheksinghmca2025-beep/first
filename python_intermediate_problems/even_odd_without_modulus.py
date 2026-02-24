# Program to check even or odd without modulus operator

num = int(input("Enter a number: "))

if (num // 2) * 2 == num:
    print("Even number")
else:
    print("Odd number")

# Example Output:
# Enter a number: 8
# Even number