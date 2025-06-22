# ------------------------------------------
# Example: Manually calculating square root (without module)
# ------------------------------------------

number = 25
estimate = number / 2

for i in range(10):
    estimate = (estimate + number / estimate) / 2

print("Manual square root estimate:", estimate)


# ------------------------------------------
# Example: Using the math module
# ------------------------------------------

import math

print("Square root using math module:", math.sqrt(25))  # Output: 5.0


# ------------------------------------------
# Practice: Using math module
# ------------------------------------------

import math

print("Square root of 49:", math.sqrt(49))      # Output: 7.0
print("Factorial of 5:", math.factorial(5))     # Output: 120


# ------------------------------------------
# Practice: Using random module
# ------------------------------------------

import random

print("Random integer between 1 and 10:", random.randint(1, 10))

fruits = ["apple", "banana", "cherry"]
print("Random fruit choice:", random.choice(fruits))


# ------------------------------------------
# Practice: Using datetime module
# ------------------------------------------

import datetime

today = datetime.date.today()

print("Today's date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# ------------------------------------------
# Example: Creating your own module
# (In real use: Save this part in myutils.py)
# ------------------------------------------

# --- myutils.py ---
 def add(x, y):
     return x + y

 def subtract(x, y):
     return x - y

 def multiply(x, y):
     return x * y

 def divide(x, y):
     if y != 0:
         return x / y
     else:
         return "Cannot divide by zero"

# Note: The above should be saved in a separate file called myutils.py

# ------------------------------------------
# Example: Using your own module
# (Save this in main.py and ensure myutils.py is in the same folder)
# ------------------------------------------

 import myutils

 print(myutils.add(10, 5))         # Output: 15
 print(myutils.subtract(10, 5))    # Output: 5
 print(myutils.multiply(10, 5))    # Output: 50
 print(myutils.divide(10, 5))      # Output: 2.0


# ------------------------------------------
# Interview Challenge Solution
# (In real use: Save this part in mathstuff.py and main.py)
# ------------------------------------------

# --- mathstuff.py ---
 def double(x):
     return x * 2

# --- main.py ---
 import mathstuff
 print(mathstuff.double(7))   # Output: 14

