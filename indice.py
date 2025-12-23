#To return indices of two numbers that add up to a target sum
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter target sum: "))

found = False
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Indices:", i, j)
            found = True
            break
    if found:
        break