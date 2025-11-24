# Program to add items to the same list

# Creating an initial list
fruits = ["apple", "banana", "cherry"]

print("Original list:", fruits)

# Adding one item using append()
fruits.append("mango")

# Adding multiple items using extend()
fruits.extend(["orange", "grapes"])

# Adding an item at a specific position using insert()
fruits.insert(1, "kiwi")  # inserts 'kiwi' at index 1

print("Updated list:", fruits)
