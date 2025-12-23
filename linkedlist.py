#Printing next to largest using linked list
# Input list of numbers
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Find next largest for each element
for i in range(len(arr)):
    found = False
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            print(f"Next largest for {arr[i]} is {arr[j]}")
            found = True
            break
    if not found:
        print(f"Next largest for {arr[i]} is None")