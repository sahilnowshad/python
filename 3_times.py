#To find all elements that appear more than n/3 times
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
n = len(arr)
result = []

for num in set(arr):  # check each unique number
    if arr.count(num) > n // 3:
        result.append(num)

print("Elements appearing more than n/3 times:", result)