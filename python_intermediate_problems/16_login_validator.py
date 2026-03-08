# Program to validate username and password

correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid username or password")

# Example Output:
# Enter username: admin
# Enter password: 1234
# Login Successful