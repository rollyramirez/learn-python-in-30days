# -----------------------------
# Day 6 — Day 6 — Python Functions (Beginner to Intermediate)
# -----------------------------

# 1. Defining a Function

def greet():
    print("Hello! Welcome to Python")

greet()

# 2. Function with Parameters

def greet_user(name):
    print(f"Hello {name}, welcome!")

greet_user("Rolly")
greet_user("Reinalyn")

# 3. Function With Return Value

def add(a, b):
    return a + b

result = add (5, 3)
print(result)

# 4. Default Parameters
def greet(name="Guest"):
    print(f"Hello {name}")

greet("Rolly")
greet()

# 5. Multiple Parameters
def full_name (first, last):
    return first + " " + last

print(full_name("Rolly","Ramirez"))

# 6. Functions with Conditions
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(29))

# -----------------------------
# 7. Real-World Example — Simple Calculator
# -----------------------------
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid Operator"

print(calculator(10 , 5, "-"))

# Exercise 1 — Create a function that prints your info

def my_info(name="Rolly", age="32", favorite_food="Adobo"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Favorite Food: {favorite_food}")
    
my_info()

# Exercise 2 — Function that returns the square of a number
def square(number):
    return number ** 2

result = square(5)
print(result)    

# Exercise 3 — Create a function that checks if a number is even or odd

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number_result = even_or_odd(111)
print(number_result)

# Exercise 4 — Function that returns the sum of numbers 1 to n

def sum_to_m(m):
    total_sum = 0
    for a in range(1, m+1):
        total_sum += a
    return total_sum

result = sum_to_m(10)
print(result)

# Exercise 5 (Challenge) — Create a function ATM()

def check_balance(balance):
    print(f"\n Your current balance is: {balance}")
    return balance

def withdraw(balance):
    amount = int(input("Enter amount to withraw: "))    
    if amount <= 0:
        print("Invalid amount!")
        return balance

    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful! New balance: {balance}")
    else:
        print("Insufficient funds!")

    return balance
    
def deposit(balance):
    amount = int(input("\n Enter amount to deposit: "))
    balance += amount
    print(f"Deposit successful! New balance: {balance}")
    return balance

def ATM():
    balance = 1000
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            balance = check_balance(balance)
        
        elif choice == "2":
            balance = withdraw(balance)
            
        elif choice == "3":
            balance = deposit(balance) 
        
        elif choice == "4":
            print("Thank you for using ATM!")
            break
        
        else:
            print("Invalid option. Please choose 1-4")
            
ATM()