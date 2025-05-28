# =========================================
# 🎯 Data Types in Python - Let's Practice!
# =========================================

# 🧮 Integer (int): Whole number (no decimal)
steps_walked = 8000
print("Steps walked:", steps_walked)  # Output: 8000

# ⚖️ Float (float): Number with a decimal
weight_kg = 72.5
print("Weight (kg):", weight_kg)  # Output: 72.5

# 📝 String (str): Text data
user_name = "JP"
print("User name:", user_name)  # Output: JP

# ✅ Boolean (bool): True or False
goal_reached = True
print("Goal reached today?", goal_reached)  # Output: True

# ➕ Custom Print: Add context for better readability
print("Hello,", user_name)  # Output: Hello, JP
print("Did you reach your goal?", goal_reached)  # Output: Did you reach your goal? True

# 💬 Comments help explain code (Python ignores them)
name = "JP"  # You can also add comments after code lines

# =========================================
# 🔍 How Python Handles Addition
# =========================================

# ➕ Adding numbers (int)
a = 5
b = 3
print("Sum of numbers:", a + b)  # Output: 8

# ➕ Adding strings (concatenation)
first_name = "Jonathan"
last_name = "Perrera"
print("Full name (no space):", first_name + last_name)  # Output: JonathanPerrera
print("Full name (with space):", first_name + " " + last_name)  # Output: Jonathan Perrera

# 🧪 String variables that look like numbers
a = "10"
b = "5"
print("Combined as strings:", a + b)  # Output: 105 (not 15!)

# =========================================
# 🧑‍💻 Practice: Create and Print Variables
# =========================================

name = "Jonathan"
age = 25
height = 5.9
is_student = True

# Print each variable
print(name)
print(age)
print(height)
print(is_student)

# Add context to make output clearer
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student status:", is_student)

# =========================================
# 🔎 Check the Type of Each Variable
# =========================================

print("Type of name:", type(name))        # Output: <class 'str'>
print("Type of age:", type(age))          # Output: <class 'int'>
print("Type of height:", type(height))    # Output: <class 'float'>
print("Type of is_student:", type(is_student))  # Output: <class 'bool'>

# =========================================
# 🎯 Interview Challenge Solutions
# =========================================

# Favorite food (string)
favorite_food = "Pasta"
print("Favorite food:", favorite_food)
print("Type:", type(favorite_food))  # Output: <class 'str'>

# Lucky number (int)
lucky_number = 7
print("Lucky number:", lucky_number)
print("Type:", type(lucky_number))  # Output: <class 'int'>

# Likes pizza? (boolean)
likes_pizza = True
print("Likes pizza:", likes_pizza)
print("Type:", type(likes_pizza))  # Output: <class 'bool'>

# =========================================
# 🌟 Mini Challenge Example
# =========================================

shoe_size = 9.5  # Float
print("Shoe size:", shoe_size)
print("Type:", type(shoe_size))  # Output: <class 'float'>

favorite_color = "green"  # String
print("Favorite color:", favorite_color)
print("Type:", type(favorite_color))  # Output: <class 'str'>

is_sunny = True  # Boolean
print("Is it sunny today?", is_sunny)
print("Type:", type(is_sunny))  # Output: <class 'bool'>
