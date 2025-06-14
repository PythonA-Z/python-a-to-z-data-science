
# =========================================
# 🧩 Functions and Lambdas in Python
# =========================================

# 1️⃣ Defining and Calling a Simple Function
def greet(name):
    print("Hello,", name)

greet("JP")
greet("Dina")

# 2️⃣ Function with a Return Value
def add(x, y):
    return x + y

result = add(3, 5)
print("Sum is:", result)

# 3️⃣ Putting It All Together: Make Tea with Options
def make_tea(type_of_tea, sugar):
    if sugar:
        print("Making", type_of_tea, "with sugar.")
    else:
        print("Making", type_of_tea, "without sugar.")

make_tea("Green Tea", True)
make_tea("Black Tea", False)

# 4️⃣ Function with No Parameters
def say_hello():
    print("Hello!")

say_hello()
say_hello()

# 5️⃣ Function with Three Parameters
def describe_person(name, age, city):
    print(name, "is", age, "years old and lives in", city)

describe_person("Dina", 28, "London")
describe_person("JP", 35, "NY")

# =========================================
# ⚡ Lambda Functions
# =========================================

# Lambda to square a number
square = lambda x: x * x
print(square(4))
print(square(7))

# Lambda to double a number
double = lambda x: x * 2
print(double(5))
print(double(10))

# =========================================
# ⚠️ Common Mistakes with Functions
# =========================================

# Forgetting return
def add_wrong(x, y):
    x + y  # Missing return

def add_correct(x, y):
    return x + y

# Calling without parentheses
def say_hi():
    print("Hi!")

say_hi  # Does nothing
say_hi()  # Calls the function

# Wrong number of arguments
def add_two(x, y):
    return x + y

# add_two(5)  # Error: missing one argument
print(add_two(5, 3))  # Correct

# =========================================
# ✅ Practice Exercises
# =========================================

# Exercise 1: Simple function
def say_hi():
    print("Hi there!")

say_hi()
say_hi()

# Exercise 2: Function with one parameter
def greet(name):
    print("Hello,", name)

greet("Dina")
greet("JP")

# Exercise 3: Function with multiple parameters
def multiply(a, b, c):
    return a * b * c

result = multiply(2, 3, 4)
print("Product is:", result)

# Exercise 4: Lambda function
double = lambda x: x * 2
print(double(5))
print(double(10))

# =========================================
# 🎓 Interview Confidence Builder Solutions
# =========================================

# is_even function
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(5))

# is_even as lambda
is_even_lambda = lambda num: num % 2 == 0
print(is_even_lambda(4))
print(is_even_lambda(5))
