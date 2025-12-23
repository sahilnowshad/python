# Find the second largest number in an array

n = int(input("Enter number of elements: "))

arr = []

# Input elements
for i in range(n):
    arr.append(int(input("Enter element: ")))

largest = arr[0]
second = arr[0]

# Find second largest
for i in range(n):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] > second and arr[i] != largest:
        second = arr[i]

print("Second largest number is:", second)