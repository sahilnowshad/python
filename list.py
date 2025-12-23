# Find the second largest number in a list

lst = list(map(int, input("Enter numbers separated by space: ").split()))

# Remove duplicates
lst = list(set(lst))

# Sort the list
lst.sort()

# Print second largest number
print("Second largest number is:", lst[-2])
