#find the element that appears n/2 times
def majority_element(nums):
    # 1
    counts = {}

    # 2
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # 3
    n = len(nums)

    # 4
    for key, value in counts.items():
        if value > n // 2:
            return key

    # 5
    return None


# Example
arr = [2, 2, 1, 1, 1, 2, 2]
print("Majority element:", majority_element(arr))
