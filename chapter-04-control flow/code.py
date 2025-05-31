
# =========================================
# 🎯 Control Flow in Python - Let's Practice!
# =========================================

# 🔍 Age Comparison
age = 18
print(age == 18)  # True
print(age < 18)   # False
print(age > 18)   # False
print(age >= 18)  # True
print(age <= 18)  # True

# 🧠 Age Decision Structure
age = 20
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# 🍕 Likes Pizza Check
likes_pizza = True
if likes_pizza:
    print("Yum! Let's order pizza.")

# 🌦️ Weather Advisor
weather = "rainy"
if weather == "sunny":
    print("Wear sunglasses!")
elif weather == "rainy":
    print("Take an umbrella.")
elif weather == "snowy":
    print("Wear a warm coat!")
else:
    print("Check the weather app.")

# 🌡️ Temperature Check
temp = 12
if temp < 0:
    print("It's freezing!")
elif temp <= 15:
    print("Chilly day")
elif temp <= 25:
    print("Nice weather")
else:
    print("It's hot!")

# 🔢 Favorite Number Check
fav_num = 7
if fav_num == 7:
    print("That's a lucky number!")
elif 1 <= fav_num <= 10:
    print("Cool choice!")
else:
    print("Interesting number!")

# 🎟️ Movie Ticket Pricing
age = 16
if age < 13:
    print("Ticket: £5")
elif age <= 18:
    print("Ticket: £7")
else:
    print("Ticket: £10")

# 😴 Sleep Tracker
hours_slept = 9
if hours_slept < 6:
    print("Get more rest!")
elif hours_slept <= 8:
    print("Well rested")
else:
    print("You might be oversleeping")

# 😊 Mood Detector
mood = "excited"
if mood == "happy":
    print("Keep smiling!")
elif mood == "angry":
    print("Take a deep breath.")
elif mood == "tired":
    print("Maybe take a short nap.")
elif mood == "excited":
    print("That's the spirit!")
else:
    print("Let's talk more about how you're feeling.")

# 💬 Simple Chatbot
user_input = "hi"
if user_input == "hi":
    print("Hello there!")
elif user_input == "bye":
    print("Goodbye!")
elif user_input == "how are you":
    print("I'm just a bunch of code, but I'm good!")
else:
    print("I'm still learning to talk. Try another phrase!")

# 🐶 Pet Age Checker
pet_age = 5
if pet_age <= 2:
    print("Playful pup!")
elif pet_age <= 7:
    print("Calm adult")
else:
    print("Wise senior")

# 🏷️ Discount Calculator
age = 19
is_student = True
if is_student:
    print("You get a 15% student discount!")
elif age < 18:
    print("You get a 10% discount for being under 18.")
else:
    print("No discount applied.")

# 🎨 Theme Selector
theme = "dark"
if theme == "dark":
    print("Switching to dark mode...")
elif theme == "light":
    print("Light mode activated!")
elif theme == "blue":
    print("Blue theme loaded.")
else:
    print("Unknown theme. Loading default.")

# 🚶 Fitness Feedback
steps_walked = 8000
if steps_walked < 5000:
    print("Let's move a bit more today!")
elif steps_walked <= 10000:
    print("Great job! You're doing well!")
else:
    print("Wow! You're smashing your goals!")

# ✅ Goal Tracker
goals_done = 4
total_goals = 5
if goals_done == total_goals:
    print("All goals completed! Amazing!")
elif goals_done >= total_goals / 2:
    print("You're on track! Keep going!")
else:
    print("Let's focus and finish strong!")

# 🚦 Color Signal
color = "green"
if color == "red":
    print("Stop!")
elif color == "green":
    print("Go!")
elif color == "yellow":
    print("Slow down.")
else:
    print("Color not recognized")

