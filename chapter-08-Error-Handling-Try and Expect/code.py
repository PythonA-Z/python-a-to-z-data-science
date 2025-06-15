# =========================================
# ⚠️ Error Handling in Python (Try and Except)
# =========================================

# -------------------------------
# Basic Try-Except Example
# -------------------------------

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)
except:
    print("Something went wrong. Please check your input.")


# -------------------------------
# ZeroDivisionError and ValueError
# -------------------------------

try:
    number = int(input("Type a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You can't divide by zero. Try a different number.")
except ValueError:
    print("Please enter a valid number, not text.")


# -------------------------------
# ValueError Example
# -------------------------------

try:
    age = int(input("Enter your age: "))
    print("Next year you will be:", age + 1)
except ValueError:
    print("Please enter a valid number for your age.")


# -------------------------------
# FileNotFoundError Example
# -------------------------------

try:
    file = open("my_data.txt", "r")
    content = file.read()
    print("File content:", content)
    file.close()
except FileNotFoundError:
    print("Sorry, the file was not found. Please check the file name.")


# -------------------------------
# TypeError Example
# -------------------------------

try:
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    message = "Hello " + name + ", you are " + age + " years old."
    print(message)
except TypeError:
    print("Oops! You tried to mix text and a number. Please check your data types.")
except ValueError:
    print("Please enter a valid number for your age.")


# -------------------------------
# Practice 1: ZeroDivisionError (Modulus)
# -------------------------------

try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    remainder = dividend % divisor
    print("Remainder is:", remainder)
except ZeroDivisionError:
    print("You can't divide by zero. Please enter a non-zero divisor.")
except ValueError:
    print("Please enter valid numbers only.")


# -------------------------------
# Practice 2: ValueError
# -------------------------------

try:
    fav_number = int(input("What is your favorite number? "))
    print("Double your number is:", fav_number * 2)
except ValueError:
    print("That's not a valid number. Please enter a number.")


# -------------------------------
# Practice 3: FileNotFoundError
# -------------------------------

try:
    file = open("notes.txt", "r")
    first_line = file.readline()
    print("First line:", first_line)
    file.close()
except FileNotFoundError:
    print("File not found! Please check the file name.")


# -------------------------------
# Practice 4: TypeError
# -------------------------------

try:
    number = int(input("Enter a number: "))
    result = "Result: " + number  # This will raise TypeError
    print(result)
except TypeError:
    print("You can't add a number to a string without converting it!")
except ValueError:
    print("Please enter a valid number.")


# -------------------------------
# Interview Challenge Solution
# -------------------------------

save_result = "N/A"  # Safe default

try:
    x = int(input("Enter the numerator: "))
    y = int(input("Enter the denominator: "))
    result = x / y
    print("Result is:", result)
    save_result = result
except ZeroDivisionError:
    print("Cannot divide by zero.")
    save_result = "N/A"
except ValueError:
    print("Invalid input, please enter numbers only.")
    save_result = "N/A"

print("Saved Result:", save_result)


# -------------------------------
# Mini Data Science Project: Robust Data Cleaner
# -------------------------------

ages = []

while len(ages) < 5:
    try:
        age = int(input("Enter age (1-120): "))
        if 1 <= age <= 120:
            ages.append(age)
        else:
            print("Age must be between 1 and 120.")
    except ValueError:
        print("Invalid input, please enter a number.")

print("Collected Ages:", ages)

