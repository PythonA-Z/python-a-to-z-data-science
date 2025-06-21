# =========================================
# 📁 Files and Folders in Python
# =========================================

# -----------------------------------------
# Writing and Reading a CSV File
# -----------------------------------------

# Step 1: Create or overwrite scores.csv and write data
with open("scores.csv", "w") as f:
    # Write the header
    f.write("Name,Score\n")
    # Write some rows
    f.write("Alice,85\n")
    f.write("Bob,90\n")
    f.write("Charlie,78\n")

# Step 2: Open and read the CSV file
with open("scores.csv", "r") as f:
    content = f.read()
    print(content)

# -----------------------------------------
# Check Current Working Directory
# -----------------------------------------

import os
print(os.getcwd())  # Shows where your files are saved

# -----------------------------------------
# Download file in Google Colab (optional)
# -----------------------------------------

from google.colab import files
files.download("scores.csv")

# =========================================
# 📃 Create and Read a Text File
# =========================================

# Step 1: Write 3 favorite quotes to notes.txt
with open("notes.txt", "w") as f:
    f.write("Believe you can and you're halfway there.\n")
    f.write("Every moment is a fresh beginning.\n")
    f.write("Dream big and dare to fail.\n")

# Step 2: Read and print the file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# =========================================
# 📊 Create and Read a CSV for Student Grades
# =========================================

# Step 1: Write header and student grades
with open("grades.csv", "w") as f:
    f.write("Name,Grade\n")
    f.write("Tom,88\n")
    f.write("Jerry,92\n")
    f.write("Spike,75\n")

# Step 2: Read and display the CSV content
with open("grades.csv", "r") as f:
    content = f.read()
    print(content)

# =========================================
# 🗒️ Mini Project: File Logger
# =========================================

# Step 1: Create log.txt and write 3 user notes
with open("log.txt", "w") as log:
    for i in range(3):
        note = input("Enter a short note: ")
        log.write(note + "\n")

# Step 2: Read and show all notes
with open("log.txt", "r") as log:
    content = log.read()
    print("\nYour Notes:\n")
    print(content)

# Check where the log.txt file is saved
print(os.getcwd())

# Download in Colab (optional)
from google.colab import files
files.download("log.txt")

# =========================================
# 🗂️ Extra: Append Mode Example
# =========================================

# Example: Append new info instead of overwriting
name = input("Enter your name: ")
age = input("Enter your age: ")

with open("userinfo.txt", "a") as f:
    f.write("Name: " + name + "\n")
    f.write("Age: " + age + "\n")

with open("userinfo.txt", "r") as f:
    content = f.read()
    print("\nAll Saved Entries:\n")
    print(content)

