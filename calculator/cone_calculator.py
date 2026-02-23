import math

# functions
def cone_csa(r, l):
    return math.pi * r * l

def cone_tsa(r, l):
    return math.pi * r * (r + l)

def cone_volume(r, h):
    return (1/3) * math.pi * r * r * h


# input
r = float(input("Enter radius of cone: "))
h = float(input("Enter height of cone: "))
l = float(input("Enter slant height of cone: "))

# calling functions
print("Curved Surface Area =", cone_csa(r, l))
print("Total Surface Area =", cone_tsa(r, l))
print("Volume =", cone_volume(r, h))


# Example Output:
# Enter radius of cone: 3
# Enter height of cone: 4
# Enter slant height of cone: 5
# Curved Surface Area = 47.12388980384689
# Total Surface Area = 75.39822368615503
# Volume = 37.69911184307752