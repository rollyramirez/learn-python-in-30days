# -----------------------------
# Day 4 — Python Conditionals & Logic 
# -----------------------------

# 1. What Are Conditionals?

age = 18

if age >=18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 2. Comparison Operators

# | Operator | Meaning          |
# | -------- | ---------------- |
# | ==       | equal to         |
# | !=       | not equal        |
# | >        | greater than     |
# | <        | less than        |
# | >=       | greater or equal |
# | <=       | less or equal    |

print(5 > 3) # True
print(5 == 10) # False

# 3. If-Else Example

password = "1234"

user_input = input("Enter password: ").strip()

if user_input == password:
    print("Access granted.")
else:
    print("Wrong password.")

# 4. If – Elif – Else Chain

grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("Failed")

# 5. Logic Operators

# | Operator | Description       | Example           |
# | -------- | ----------------- | ----------------- |
# | and      | both must be True | x > 10 and x < 20 |
# | or       | at least one True | x == 0 or x == 10 |
# | not      | reverses value    | not True          |

age = 25
has_id = True

if age >= 18 and has_id:
    print("You may enter.")
else:
    print("Restricted area")
    
    
# Real-World Examples

# 1. Simple Login System

user_name = "admin"
password = "1234" 

u = input("Username: ").strip()
p = input("Password: ").strip()

if u == user_name and p == password:
    print("Login successful!")
else:
    print("Invalid username or password")
    
# 2. Store Discount System

amount = int(input("Enter total amount: "))

if amount >= 1000:
    total_discount = amount * 0.1
    total_amount = amount - total_discount
    print(f"You got 10% discount!, Please pay this amount Php {total_amount} to cashier.")
else:
    print("No discount applied.")

# 3. Temperature Checker

temp = int(input("Enter temperature: "))

if temp > 30:
    print("It's hot today.")
elif temp >= 20:
    print("Weather is good.")
else:
    print("It's cold today.")


# -----------------------------
# Exercise 1 — Even or Odd
# -----------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
# -----------------------------
# Exercise 2 — Simple Grading
# -----------------------------

score_input = int(input("Enter your score: "))

if score_input >= 90:
    print("A")
elif score_input >= 80:
    print("B")
elif score_input >= 70:
    print("C")
else:
    print("F")

# -----------------------------
# Exercise 3 - Age checker
# -----------------------------

age_input = int(input("Enter your age: "))

if age_input <= 12:
    print("Child")
elif age_input <= 17:
    print("Teen")
elif age_input <= 59:
    print("Adult") 
else:
    print("Senior")
    
# -----------------------------
# Exercise 4 - ATM Withdrawal
# -----------------------------

balance = 1000
withdraw_amount = int(input("Enter amount to withdraw: "))

if withdraw_amount > balance:
    print("Insufficient Balance")
elif withdraw_amount <= 0:
    print("Invalid amount")
else:
    new_balance = balance - withdraw_amount
    print(f"Withdrawal Successful, Your new balance is: {new_balance}")