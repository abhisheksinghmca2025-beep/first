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