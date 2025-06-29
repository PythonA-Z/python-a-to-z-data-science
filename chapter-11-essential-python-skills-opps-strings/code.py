# ------------------------------------------
# Example: Simple class with a method
# ------------------------------------------

class Car:
    def start_engine(self):
        return "Engine started"  # A method to simulate starting a car engine


# ------------------------------------------
# Example: Class with constructor and method
# ------------------------------------------

class Car:
    def __init__(self, model):
        self.model = model  # Store the model name of the car

    def accelerate(self):
        return f"{self.model} is speeding up!"  # Simulate acceleration

my_car = Car("TurboX")
print(my_car.accelerate())


# ------------------------------------------
# Example: Full Car class with multiple attributes
# ------------------------------------------

class Car:
    def __init__(self, model, color, top_speed):
        self.model = model        # Car model
        self.color = color        # Car color
        self.top_speed = top_speed  # Top speed in km/h

    def accelerate(self):
        return f"{self.model} is accelerating to {self.top_speed} km/h!"  # Simulate acceleration

my_car = Car("SpeedX", "Red", 320)
print(my_car.accelerate())


# ------------------------------------------
# Example: Using pandas and scikit-learn
# ------------------------------------------

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame(data={})  # Create an empty DataFrame
model = LinearRegression()  # Create a regression model object


# ------------------------------------------
# Example: Book class with method
# ------------------------------------------

class Book:
    def __init__(self, title, author, pages):
        self.title = title      # Book title
        self.author = author    # Author name
        self.pages = pages      # Number of pages

    def description(self):
        return f"{self.title} by {self.author}"  # Return a short description

my_book = Book("The Alchemist", "Paulo Coelho", 197)
print(my_book.description())


# ------------------------------------------
# Example: Book class with reading_time method
# ------------------------------------------

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"{self.title} by {self.author}"

    def reading_time(self):
        return f"Estimated reading time: {self.pages} minutes"  # Reading time estimate

book2 = Book("Atomic Habits", "James Clear", 250)
print(book2.description())
print(book2.reading_time())


# ------------------------------------------
# Practice: String methods
# ------------------------------------------

name = "DataScience"
print(name.lower())  # Convert to lowercase
print(name.upper())  # Convert to uppercase

email = "   user@example.com   "
print(email.strip())  # Remove leading/trailing spaces

message = "Data Science is hard"
print(message.replace("hard", "fun"))  # Replace 'hard' with 'fun'

sentence = "Python is powerful"
print(sentence.split(" "))  # Split sentence into words

words = ["Python", "for", "Data", "Science"]
print(" ".join(words))  # Join words into a sentence

name = "   Alice Smith   "
cleaned = name.strip().lower().replace(" ", "_")  # Clean and format name
print(cleaned)

name = "   Alice Johnson   "
cleaned_name = name.strip()  # Remove extra spaces
lower_name = cleaned_name.lower()  # Convert to lowercase
print(lower_name)

sentence = "Data_Science_is_awesome!"
fixed_sentence = sentence.replace("_", " ")  # Replace underscores with spaces
words = fixed_sentence.split(" ")  # Split sentence into words
print(words)

words = ["learning", "Python", "is", "fun"]
sentence = " ".join(words)  # Join words with space
print(sentence)


# ------------------------------------------
# Practice: List comprehension
# ------------------------------------------

numbers = [1, 2, 3]
new = [x + 1 for x in numbers]  # Add 1 to each number
print(new)


# ------------------------------------------
# Practice: Lambda function
# ------------------------------------------

double = lambda x: x * 2  # Define a small function to double a number
print(double(5))


# ------------------------------------------
# Practice: help() function
# ------------------------------------------

help(len)  # Show help information about the len() function


# ------------------------------------------
# Practice: List comprehension for squares
# ------------------------------------------

nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]  # Square each number
print(squares)


# ------------------------------------------
# Practice: Lambda to uppercase
# ------------------------------------------

to_upper = lambda word: word.upper()  # Convert text to uppercase
print(to_upper("data"))


# ------------------------------------------
# Practice: help on sum function
# ------------------------------------------

help(sum)  # Show help documentation for the sum() function


# ------------------------------------------
# Example: Movie class with description method
# ------------------------------------------

class Movie:
    def __init__(self, title, director, year):
        self.title = title        # Movie title
        self.director = director  # Director's name
        self.year = year          # Release year

    def description(self):
        return f"{self.title} was directed by {self.director} in {self.year}"

m = Movie("Inception", "Christopher Nolan", 2010)
print(m.description())

# Create a list of Movie objects
movies = [
    Movie("Inception", "Christopher Nolan", 2010),
    Movie("The Matrix", "The Wachowskis", 1999),
    Movie("Interstellar", "Christopher Nolan", 2014)
]

# Extract titles using list comprehension
titles = [m.title for m in movies]
print(titles)


# ------------------------------------------
# Practice: Clean full name (commented out for safety)
# ------------------------------------------

# name = input("Enter your full name: ")  # User input with extra spaces
# cleaned = name.strip().lower().replace(" ", "_")  # Clean and format name
# print(cleaned)


# ------------------------------------------
# Mini Project: Book library with summary
# ------------------------------------------

class Book:
    def __init__(self, title, author):
        self.title = title      # Book title
        self.author = author    # Author name

    def summary(self):
        return f"{self.title} by {self.author}"  # Summary of the book

library = []

# Ask user for 3 books 
 for i in range(3):
     print(f"\nBook {i + 1}")
     title = input("Enter book title: ")
     author = input("Enter author name: ")
     library.append(Book(title, author))

# Print summaries of all books
 print("\nYour Library:")
 for book in library:
     print(book.summary())
