numbers = [10, 20, 4, 45, 99, 67]

# Find the largest
largest = max(numbers)

# Remove the largest element
numbers.remove(largest)

# Now find the second largest
second_largest = max(numbers)

print("Second largest number is:", second_largest)
