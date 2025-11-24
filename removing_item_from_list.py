# Create a sample list
my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)

# Remove item from the beginning
my_list.pop(0)
print("After removing from beginning:", my_list)

# Remove item from the end
my_list.pop()
print("After removing from end:", my_list)

# Remove item from a specific position
position = int(input("Enter the position to remove (starting from 0): "))
if 0 <= position < len(my_list):
    my_list.pop(position)
    print("After removing from position", position, ":", my_list)
else:
    print("Invalid position!")

