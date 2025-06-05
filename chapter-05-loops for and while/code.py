
# =========================================
# 🎯 For Loops in Python
# =========================================

# Print numbers 0 to 2
for i in range(3):
    print(i)

# Print numbers 1 to 5
for i in range(1, 6):
    print(i)

# Sum numbers from 2 to 11
total = 0
for i in range(2, 12):
    total = total + i
print(total)

# Simple for loop with message
for i in range(4):
    print("Loop number:", i)

# Skip the number 3 using continue
for i in range(5):
    if i == 3:
        continue
    print(i)

# Skip even numbers using continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

# Loop with pass as placeholder
for i in range(3):
    if i == 1:
        pass
    print(i)

# Using pass again with print message
for i in range(3):
    if i == 1:
        pass
    print("i is:", i)

# Modulo example
print(10 % 3)  # Output: 1


# =========================================
# 🔁 While Loops in Python
# =========================================

# Print numbers 0 to 2
count = 0
while count < 3:
    print(count)
    count = count + 1

# Print numbers 5 to 9
num = 5
while num <= 9:
    print(num)
    num = num + 1

# Infinite loop with break
while True:
    print(1)
    break

# Simple while loop with step count
count = 1
while count <= 3:
    print("Step", count)
    count += 1

# Break inside a while loop
count = 0
while True:
    if count == 4:
        break
    print("Counting:", count)
    count += 1

# Infinite loop example (missing update)
count = 1
while count < 5:
    print(count)
# count += 1  # This line is missing


# =========================================
# 🧠 Interview & Mini Challenge Solutions
# =========================================

# Interview: What is a loop?
for i in range(3):
    print("Hello")

# Interview: range(5) vs range(1, 5)
print(list(range(5)))     # [0, 1, 2, 3, 4]
print(list(range(1, 5)))  # [1, 2, 3, 4]

# Interview: Infinite while loop (missing update)
count = 1
while count < 5:
    print(count)
# count += 1  # This is needed to avoid infinite loop

# Interview: break vs continue
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

# Mini Challenge 1: Print 1 to 5
for num in range(1, 6):
    print(num)

# Mini Challenge 2: Print squares of 1 to 5
for num in range(1, 6):
    print(num ** 2)

# Mini Challenge 3: Factorial using for loop
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print("Factorial:", factorial)

# Mini Challenge 4: Print numbers divisible by 3 from 1 to 20
for num in range(1, 21):
    if num % 3 == 0:
        print(num)
