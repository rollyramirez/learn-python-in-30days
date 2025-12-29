# -----------------------------
# Day 5 — Python Loops (for, while, nested loops)
# -----------------------------

# 1. For Loop
for i in range(3):
    print(i)  # 0 1 2

# 2. Range() Pattern
for x in range(1, 11, 2):
    print(x)  # 1 3 5 7 9

# 3. Looping Through a String
word = "Python"
for letter in word:
    print(letter)

# 4. Looping Through a List
fruits = ['apple', 'banana', 'mango']
for f in fruits:
    print(f)

# 5. While Loop
count = 1
while count <= 5:
    print(count)
    count += 1

# -----------------------------
# Real-World Examples
# -----------------------------

# Example 1 — Login Attempts (3 tries only)
password = "admin123"
attempts = 0

while attempts < 3:
    p = input("Enter password: ")

    if p == password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        print(f"Wrong password! Attempts left: {3 - attempts}")

if attempts == 3:
    print("Account Locked")

# Example 2 — Countdown Timer
import time

for sec in range(5, 0, -1):
    print(sec)
    time.sleep(1)
print("Time's up!")

# Example 3 — Grocery List
items = ["rice", "eggs", "milk"]
for item in items:
    print(f"- {item}")

# Example 4 — Sum of 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Total Sum of 1 - 100:", total)


# -----------------------------
# Exercises
# -----------------------------

# Exercise 1 — Print numbers 1 to 10
for y in range(1, 11):
    print(y)

# Exercise 2 — Print “Hello” 5 times using while loop
counter = 1
while counter <= 5:
    print("Hello")
    counter += 1

# Exercise 3 — Sum of even numbers 1 to 50
total_even = 0
for z in range(1, 51):
    if z % 2 == 0:
        total_even += z
print("Sum of all even numbers:", total_even)

# Exercise 4 — Multiplication Table
number = int(input("Enter number: "))
for num in range(1, 11):
    print(f"{number} x {num} = {number * num}")


# -----------------------------
# Exercise 5 — ATM (Corrected Improved Version)
# -----------------------------

balance = 1000

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"Your balance is: {balance}")

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdraw successful! New balance: {balance}")
        else:
            print("Insufficient balance!")

    elif choice == "3":
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposit successful! New balance: {balance}")
        else:
            print("Invalid amount!")

    elif choice == "4":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid option! Please choose 1-4.")
