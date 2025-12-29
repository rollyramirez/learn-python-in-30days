# -----------------------------
# Day 7 — Python Data Structures
# -----------------------------

# 1. LISTS (Ordered, Changeable)
# A list stores multiple items in one variable.

fruits = ["apple","banana","mango"]
print(fruits)
print(fruits[1])

# Modify a list
fruits[0] = "grapes"
print(fruits)

# Add an item
fruits.append("orange")

# Remove an item
fruits.remove("banana")

# 2. TUPLES (Ordered, Unchangeable)
# Used for values that should NOT be modified.

colors = ("red","green","blue")
print(colors[0]) # red

# 3. DICTIONARIES (Key–Value Pairs)
# Most used in real backend + Django.

person = {
    "name": "Rolly",
    "age": 32,
    "city": "Manila"
}

print(person["name"])

# Add key-value

person["job"] = "Django Developer"

# Update value

person["age"] = 33

# Loop through dictionary

for key, value in person.items():
    print(key, value)
    
# 4. SETS (Unordered, Unique Items)
# Automatically removes duplicates.

