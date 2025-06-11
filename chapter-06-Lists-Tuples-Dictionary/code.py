

# =========================================
# 🍎 Lists — Ordered and Editable
# =========================================

# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Accessing with negative indexes
print(fruits[-1])
print(fruits[-2])

# Adding items to a list
fruits.append("orange")
print(fruits)

fruits.insert(1, "grape")
print(fruits)

# Changing list items
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)

# Removing items
fruits = ["apple", "banana", "cherry", "orange"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "cherry", "orange"]
last_fruit = fruits.pop()
print("Removed:", last_fruit)
print(fruits)

# Checking the length of a list
fruits = ["apple", "cherry"]
print(len(fruits))

# Loop through list
fruits = ["apple", "cherry", "orange"]
for fruit in fruits:
    print(fruit)

# Exercises
favourite_movies = ["Inception", "Interstellar", "The Matrix"]
print(favourite_movies[1])

animals = ["cat", "dog", "rabbit"]
animals.append("hamster")
animals.remove("dog")
print(animals)

fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print("Fruit:", fruit)
print("Total fruits:", len(fruits))

# Modify a list
numbers = [12, 45, 67, 23, 89]
numbers.remove(max(numbers))
numbers.insert(1, 100)
print(numbers)

# =========================================
# 🌈 Tuples — Ordered but Immutable
# =========================================

colors = ("red", "green", "blue")
print(colors)
print(colors[0])
print(colors[2])

print(len(colors))

for color in colors:
    print(color)

# Tuple methods
colors = ("red", "blue", "red", "green", "red")
print(colors.count("red"))

numbers = (10, 20, 30, 20, 40)
print(numbers.index(20))

# Tuple unpacking
rgb = (255, 128, 64)
red, green, blue = rgb
print("Red:", red)
print("Green:", green)
print("Blue:", blue)

# One-item tuple
single = ("hello",)
not_a_tuple = ("hello")

# Tuple practice
coordinates = (51.5074, 0.1278)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print("Fruit:", fruit)

# List vs Tuple Example
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

colors = ("red", "green")
# colors.append("blue")  # Error

# =========================================
# 🔑 Dictionaries — Key-Value Pairs
# =========================================

student = {
    "name": "Alice",
    "age": 21,
    "grade": "A"
}
print(student["name"])
print(student["age"])
print(student.get("grade"))
# print(student["email"])  # Error
print(student.get("email"))
print(student.get("email", "Not Provided"))

# Update and add values
student["age"] = 22
student["email"] = "alice@example.com"
print(student)

# Remove items
student.pop("grade")
del student["email"]
print(student)

# Loop through dictionary
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}
for key in student:
    print(key, ":", student[key])

for key, value in student.items():
    print(key, "=", value)

# Dictionary methods
student = {
    "name": "Alice",
    "age": 22
}
print(student.keys())
print(student.values())
print(student.items())

# Mixed-type values
info = {
    "name": "Tom",
    "marks": [85, 90, 95],
    "active": True
}

# Key check
student = {"name": "Alice", "age": 21}
if "grade" in student:
    print(student["grade"])
else:
    print("Grade not found")

# Immutable key example
# data = {[1, 2]: "value"}  # TypeError
data = {(1, 2): "value"}  # Valid

# Sorted keys
for key in sorted(student):
    print(key, "=", student[key])

# =========================================
# 🧠 Interview & Mini Challenge Solutions
# =========================================

# 1. Modify list
numbers = [12, 7, 25, 18, 5]
numbers.remove(max(numbers))
numbers.insert(1, 10)
print(numbers)

# 2. Unpack tuple
rgb = (255, 100, 75)
r, g, b = rgb
print("Red:", r)
print("Green:", g)
print("Blue:", b)

# 3. Update dictionary values
scores = {"Alice": 80, "Bob": 75, "Cara": 90}
for student in scores:
    scores[student] += 5
print(scores)

# 4. Key check before access
person = {"name": "JP", "age": 30}
key = "hobby"
if key in person:
    print(person[key])
else:
    print(f"{key} not found.")

# 5. Merge dictionaries
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = {**a, **b}
print(merged)

# =========================================
# 📊 Mini Project: Data Science Word Counter
# =========================================

words = ["python", "sun", "data", "dog", "ai", "fun", "learning", "machine"]
ds_words = ["python", "data", "ai", "machine", "learning"]

count = 0
for word in words:
    if word in ds_words:
        print("Found:", word)
        count += 1
print("Total data science words:", count)
