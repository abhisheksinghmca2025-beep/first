n = 4

# Upper pyramid
for i in range(1, n+1):
    spaces = n - i
    stars = 2*i - 1
    print(" " * spaces + "*" * stars)

# Lower pyramid
for i in range(n-1, 0, -1):
    spaces = n - i
    stars = 2*i - 1
    print(" " * spaces + "*" * stars)


# Output:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *