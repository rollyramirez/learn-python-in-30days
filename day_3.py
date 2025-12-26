# -----------------------------
# Day 3 — Strings & Formatting in Python 
# -----------------------------

# Tutorial Output

# 2. What Are Strings?

name = "Rolly"
greeting = "Hello World!"

# 3. Common String Methods

text = "hello world"

print(text.upper()) # HELLO WORLD
print(text.lower()) # hello world
print(text.title()) # Hello World
print(text.capitalize()) # Hello world
print(text.replace("world","Python")) # hello Python

# 4. String Concatenation

first_name = "Rolly"
last_name = "Ramirez"

fullname = first_name + " " + last_name
print("Fullname:",fullname)

# 5. f-Strings (Recommended)

age = 32
name = "Rolly"

print(f"My name is {name} and I am {age} years old.")

# 6. String Length

sentence = "Python is awesome"
print(len(sentence)) # 17

# 7. Real-World Examples

# Example 1 — Greeting

user_name = input("Enter your name: ")
print(f"Hello {user_name}, welcome to Python!" )

# Example 2 — Formatting a Report

product = "Milk"
price = 50
quantity = 2

total = price * quantity
print(f"Total for {quantity} {product}(s): Php {total}")

# Example 3 — Reverse a Word

word = input("Enter a word:")
print("Reversed:", word[::-1])

# -----------------------------
# Exercise 1 — Sentence Analysis 
# -----------------------------

sentence = "hello world"

print("Sentence:", sentence.title())
print("UPPER:", sentence.upper())
print("lower:",sentence.lower())
print("Length:",len(sentence))

# -----------------------------
# Exercise 2 — Full Name
# -----------------------------

f_name = "Rolly"
l_name = "Ramirez"

full_name = f_name + " " + l_name

print("Your fullname is:", full_name)

# -----------------------------
# Exercise 3 (Challenge) — Reverse Word
# -----------------------------

word_input = input("Enter a word: ")
print("Reversed",word_input[::-1])

# -----------------------------
# Real-World Twist
# -----------------------------

name_input = input("Enter your name: ")

print(f"Welcome {name_input}! Your name has {len(name_input)} characters.")