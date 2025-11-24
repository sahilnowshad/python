# Create an empty list
my_list = []

# Get number of items from user
n = int(input("How many elements do you want to add? "))

for i in range(n):
    element = input("Enter element: ")
    my_list.append(element)

print("Final List:", my_list)
