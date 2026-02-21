import math

# Cube
def cube_surface_area(a):
    return 6 * a * a

def cube_volume(a):
    return a * a * a


# Cuboid
def cuboid_surface_area(l, w, h):
    return 2 * (l*w + l*h + w*h)

def cuboid_volume(l, w, h):
    return l * w * h


# Cylinder
def cylinder_csa(r, h):
    return 2 * math.pi * r * h

def cylinder_tsa(r, h):
    return 2 * math.pi * r * (r + h)

def cylinder_volume(r, h):
    return math.pi * r * r * h


# Cone
def cone_csa(r, l):
    return math.pi * r * l

def cone_tsa(r, l):
    return math.pi * r * (r + l)

def cone_volume(r, h):
    return (1/3) * math.pi * r * r * h


# Sphere
def sphere_surface_area(r):
    return 4 * math.pi * r * r

def sphere_volume(r):
    return (4/3) * math.pi * r * r * r


# Hemisphere
def hemisphere_surface_area(r):
    return 3 * math.pi * r * r

def hemisphere_volume(r):
    return (2/3) * math.pi * r * r * r


# -------- Function Calling --------

a = 4
l = 5
w = 3
h = 6
r = 3
slant = 5

print("Cube Surface Area =", cube_surface_area(a))
print("Cube Volume =", cube_volume(a))

print("Cuboid Surface Area =", cuboid_surface_area(l, w, h))
print("Cuboid Volume =", cuboid_volume(l, w, h))

print("Cylinder CSA =", cylinder_csa(r, h))
print("Cylinder TSA =", cylinder_tsa(r, h))
print("Cylinder Volume =", cylinder_volume(r, h))

print("Cone CSA =", cone_csa(r, slant))
print("Cone TSA =", cone_tsa(r, slant))
print("Cone Volume =", cone_volume(r, h))

print("Sphere Surface Area =", sphere_surface_area(r))
print("Sphere Volume =", sphere_volume(r))

print("Hemisphere Surface Area =", hemisphere_surface_area(r))
print("Hemisphere Volume =", hemisphere_volume(r))