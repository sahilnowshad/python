# Program to add another list to an existing list

# First list
fruits = ["apple", "banana", "cherry"]

# Second list
more_fruits = ["mango", "orange", "grapes"]

print("Original list:", fruits)
print("List to be added:", more_fruits)

# Adding another list using extend()
fruits.extend(more_fruits)

print("Combined list:", fruits)
