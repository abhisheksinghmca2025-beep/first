# Program to count number of special characters in a sentence

# taking input from user
sentence = input("Enter a sentence: ")

# variable to count special characters
count = 0

# checking each character
for ch in sentence:
    if not ch.isalnum() and not ch.isspace():
        count += 1

# display result
print("Number of special characters:", count)


# Example Output:
# Enter a sentence: Hello@ World! 2024#
# Number of special characters: 3