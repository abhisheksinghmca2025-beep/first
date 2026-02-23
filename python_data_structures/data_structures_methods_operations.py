# ================= STRING =================
print("===== STRING METHODS & OPERATIONS =====")

text = "python programming"

print("Original:", text)
# Output: Original: python programming

# methods
print("Upper:", text.upper())
# Output: Upper: PYTHON PROGRAMMING

print("Lower:", text.lower())
# Output: Lower: python programming

print("Title:", text.title())
# Output: Title: Python Programming

print("Capitalize:", text.capitalize())
# Output: Capitalize: Python programming

print("Count of 'm':", text.count("m"))
# Output: Count of 'm': 2

print("Find 'prog':", text.find("prog"))
# Output: Find 'prog': 7

print("Replace:", text.replace("python", "java"))
# Output: Replace: java programming

# operations
print("Length:", len(text))
# Output: Length: 18

print("First char:", text[0])
# Output: First char: p

print("Last char:", text[-1])
# Output: Last char: g

print("Slice:", text[0:6])
# Output: Slice: python


# ================= TUPLE =================
print("\n===== TUPLE METHODS & OPERATIONS =====")

t = (10, 20, 30, 40, 20)

print("Tuple:", t)
# Output: Tuple: (10, 20, 30, 40, 20)

# methods
print("Count of 20:", t.count(20))
# Output: Count of 20: 2

print("Index of 30:", t.index(30))
# Output: Index of 30: 2

# operations
print("Length:", len(t))
# Output: Length: 5

print("First element:", t[0])
# Output: First element: 10

print("Last element:", t[-1])
# Output: Last element: 20

print("Slice:", t[1:4])
# Output: Slice: (20, 30, 40)


# ================= SET =================
print("\n===== SET METHODS & OPERATIONS =====")

set1 = {10, 20, 30}
set2 = {30, 40, 50}

print("Set1:", set1)
# Output: Set1: {10, 20, 30}

print("Set2:", set2)
# Output: Set2: {40, 50, 30}

# methods
set1.add(60)
print("After add:", set1)
# Output: After add: {10, 20, 30, 60}

set1.remove(20)
print("After remove:", set1)
# Output: After remove: {10, 30, 60}

print("Union:", set1.union(set2))
# Output: Union: {10, 30, 40, 50, 60}

print("Intersection:", set1.intersection(set2))
# Output: Intersection: {30}

print("Difference:", set1.difference(set2))
# Output: Difference: {10, 60}

# ================= DICTIONARY =================
print("\n===== DICTIONARY METHODS & OPERATIONS =====")

student = {
    "id": 101,
    "name": "Rahul",
    "course": "Python",
    "marks": 85
}

print("Original Dictionary:", student)
# Output: Original Dictionary: {'id': 101, 'name': 'Rahul', 'course': 'Python', 'marks': 85}

# methods
print("Keys:", student.keys())
# Output: Keys: dict_keys(['id', 'name', 'course', 'marks'])

print("Values:", student.values())
# Output: Values: dict_values([101, 'Rahul', 'Python', 85])

print("Items:", student.items())
# Output: Items: dict_items([('id', 101), ('name', 'Rahul'), ('course', 'Python'), ('marks', 85)])

# get method
print("Get name:", student.get("name"))
# Output: Get name: Rahul

# update method
student.update({"marks": 90})
print("After update:", student)
# Output: After update: {'id': 101, 'name': 'Rahul', 'course': 'Python', 'marks': 90}

# add new key
student["city"] = "Delhi"
print("After adding city:", student)
# Output: After adding city: {'id': 101, 'name': 'Rahul', 'course': 'Python', 'marks': 90, 'city': 'Delhi'}

# remove element
student.pop("course")
print("After removing course:", student)
# Output: After removing course: {'id': 101, 'name': 'Rahul', 'marks': 90, 'city': 'Delhi'}

# operations
print("Length:", len(student))
# Output: Length: 4

print("Access name:", student["name"])
# Output: Access name: Rahul

print("Check key exists:", "id" in student)
# Output: Check key exists: True