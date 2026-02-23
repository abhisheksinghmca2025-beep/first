# Program for Class Distribution based on marks

marks = int(input("Enter marks: "))

if marks >= 75:
    print("Distinction")

elif marks >= 60:
    print("First Class")

elif marks >= 50:
    print("Second Class")

elif marks >= 40:
    print("Pass")

else:
    print("Fail")


# Example Output 1:
# Enter marks: 82
# Distinction

# Example Output 2:
# Enter marks: 65
# First Class

# Example Output 3:
# Enter marks: 55
# Second Class

# Example Output 4:
# Enter marks: 42
# Pass

# Example Output 5:
# Enter marks: 30
# Fail