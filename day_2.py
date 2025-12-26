# -----------------------------
# Day 2 - Python Basics Tutorial 
# -----------------------------

# Tutorial Output
name = "Rolly"
age = 32
price = 99.50
is_student = True

# Type Conversion
converted_age = int("25")
weight = float("65")
year_string = str(2025)

# Basic Math Operators
a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division (float)
print(a // b)  # floor division
print(a % b)   # remainder
print(a ** b)  # exponent

# -----------------------------
# Example 1 — Salary Calculator
# -----------------------------
monthly_salary = 20000
months = 12

annual_salary = monthly_salary * months
print("Your annual salary is: Php", annual_salary)

# -----------------------------
# Example 2 — Grocery Budget
# -----------------------------
rice = 50
milk = 30
eggs = 70

total_grocery = rice + milk + eggs
print(f"Total grocery cost: {total_grocery} pesos")

# -----------------------------
# Example 3 — Age Calculator
# -----------------------------
current_year = 2025
birth_year = 1993

calculated_age = current_year - birth_year
print("Your age is:", calculated_age)

# -----------------------------
# Exercise 1 — User Introduction
# -----------------------------
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hi {name}, you are {age} years old.")

# -----------------------------
# Exercise 2 — Simple Calculator
# -----------------------------
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

total_sum = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
quotient = first_number / second_number

print("Sum:", total_sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# -----------------------------
# Exercise 3 — Birth Year → Age Calculator (Challenge)
# -----------------------------
current_year_input = int(input("Enter current year: "))
birth_year_input = int(input("Enter your birth year: "))

age_result = current_year_input - birth_year_input
print("You are", age_result, "years old.")
