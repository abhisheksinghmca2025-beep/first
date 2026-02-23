import math

# functions
def cylinder_csa(r, h):
    return 2 * math.pi * r * h

def cylinder_tsa(r, h):
    return 2 * math.pi * r * (r + h)

def cylinder_volume(r, h):
    return math.pi * r * r * h


# input
r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))

# calling functions
print("Curved Surface Area =", cylinder_csa(r, h))
print("Total Surface Area =", cylinder_tsa(r, h))
print("Volume =", cylinder_volume(r, h))

# Example Output:
# Enter radius of cylinder: 3
# Enter height of cylinder: 5
# Curved Surface Area = 94.24777960769379
# Total Surface Area = 150.79644737231007
# Volume = 141.3716694115407