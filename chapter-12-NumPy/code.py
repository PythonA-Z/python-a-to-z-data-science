# ------------------------------------------
# Example: Import and Create NumPy Array
# ------------------------------------------

import numpy as np  # "np" is just a nickname used to shorten 'numpy'

my_list = [1, 2, 3, 4]  # This is a plain old Python list
my_array = np.array(my_list)  # Convert list into NumPy array
print(my_array)  # Output: [1 2 3 4]


# ------------------------------------------
# Example: Add to NumPy Array
# ------------------------------------------

scores_list = [80, 85, 90]  # This is a plain old Python list
scores = np.array(scores_list)  # Create a NumPy array of scores
bonus_scores = scores + 5  # Add 5 bonus points to every score
print(bonus_scores)  # Output: [85 90 95]

# Python list: Add 5 manually using list comprehension
scores_list = [80, 85, 90]
updated_scores_list = [x + 5 for x in scores_list] 

# NumPy array: Add 5 instantly
scores = np.array(scores_list)
new_scores = scores + 5  # Add 5 to all elements
print(new_scores)  # Output: [85 90 95]


# ------------------------------------------
# Example: NumPy Statistics
# ------------------------------------------

grades = np.array([70, 82, 89, 95])  # Create a NumPy array
print("Average:", np.mean(grades))  # Output: 84.0
print("Highest:", np.max(grades))   # Output: 95
print("Lowest:", np.min(grades))    # Output: 70


# ------------------------------------------
# Example: Large Dataset with NumPy
# ------------------------------------------

big_list = list(range(1000000))  # A regular Python list with 1 million numbers
big_array = np.array(big_list)   # Convert it into a NumPy array
result = big_array * 2  # Multiply every number by 2, instantly


# ------------------------------------------
# Example: np.zeros
# ------------------------------------------

zeros_array = np.zeros(5)  # Create an array with five zeros
print(zeros_array)  # Output: [0. 0. 0. 0. 0.]


# ------------------------------------------
# Example: np.ones
# ------------------------------------------

ones_array = np.ones((2, 3))  # Create a 2x3 array filled with ones
print(ones_array)  # Output: [[1. 1. 1.] [1. 1. 1.]]


# ------------------------------------------
# Example: np.arange with Step
# ------------------------------------------

step_array = np.arange(0, 10, 2)  # Create an array from 0 to 8, stepping by 2
print(step_array)  # Output: [0 2 4 6 8]


# ------------------------------------------
# Example: np.mean, np.max, np.min
# ------------------------------------------

scores = np.array([80, 85, 90])  # Create a NumPy array of scores
print(np.mean(scores))  # Output: 85.0 (the average)
print(np.max(scores))   # Output: 90
print(np.min(scores))   # Output: 80


# ------------------------------------------
# Example: np.shape
# ------------------------------------------

print(np.shape(ones_array))  # Output: (2, 3) — shows 2 rows, 3 columns


# ------------------------------------------
# Example: 2D NumPy Array
# ------------------------------------------

my_grid = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(my_grid.shape)  # Output: (2, 3)
print(my_grid[0][1])  # Output: 2 => from 1st row, 2nd column


# ------------------------------------------
# Practice: Add 10 to Every Score
# ------------------------------------------

scores = np.array([65, 70, 75])  # Create a NumPy array
updated = scores + 10  # Add 10 to each element
print(updated)  # Output: [75 80 85]


# ------------------------------------------
# Practice: Average Grade
# ------------------------------------------

grades = np.array([88, 92, 79, 85])  # Grades array
average = np.mean(grades)  # Find the mean
print(average)  # Output: 86.0


# ------------------------------------------
# Practice: Access Value in 2D Grid
# ------------------------------------------

grid = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(grid[1][2])  # Output: 60 — second row, third column


# ------------------------------------------
# Practice: Create Even Range with np.arange
# ------------------------------------------

evens = np.arange(0, 10, 2)  # Start at 0, step by 2
print(evens)  # Output: [0 2 4 6 8]


# ------------------------------------------
# Mini Challenge: Analyze Scores
# ------------------------------------------

scores = np.array([75, 80, 95, 100])  # Step 1: Create the scores array
print(np.mean(scores))  # Output: 87.5
print(np.max(scores))   # Output: 100
print(np.min(scores))   # Output: 75


# ------------------------------------------
# Mini Challenge: Access 2D Array Value
# ------------------------------------------

grid = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(grid[1][0])  # Output: 40 — second row, first column


# ------------------------------------------
# Mini Challenge: Use np.arange and Multiply
# ------------------------------------------

numbers = np.arange(0, 19, 3)  # Create a range from 0 to 18 (inclusive) with step 3
result = numbers * 10  # Multiply every value by 10
print(result)  # Output: [  0  30  60  90 120 150 180]

