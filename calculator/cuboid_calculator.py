# functions
def cuboid_csa(l, w, h):
    return 2 * h * (l + w)

def cuboid_tsa(l, w, h):
    return 2 * (l*w + l*h + w*h)

def cuboid_volume(l, w, h):
    return l * w * h


# input
l = float(input("Enter length of cuboid: "))
w = float(input("Enter width of cuboid: "))
h = float(input("Enter height of cuboid: "))

# calling functions
print("Curved Surface Area =", cuboid_csa(l, w, h))
print("Total Surface Area =", cuboid_tsa(l, w, h))
print("Volume =", cuboid_volume(l, w, h))


# Example Output:
# Enter length of cuboid: 5
# Enter width of cuboid: 4
# Enter height of cuboid: 3
# Curved Surface Area = 54.0
# Total Surface Area = 94.0
# Volume = 60.0