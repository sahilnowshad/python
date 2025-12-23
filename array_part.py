
#Return True if array can be partitioned into two subsets of equal sum
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
total_sum = sum(arr)

# If total sum is odd, cannot partition
if total_sum % 2 != 0:
    print(False)
else:
    target = total_sum // 2

    # Recursive function to check subset sum
    def canPartition(index, current_sum):
        if current_sum == 0:
            return True
        if index < 0 or current_sum < 0:
            return False
        # Include current element or exclude it
        return canPartition(index - 1, current_sum - arr[index]) or canPartition(index - 1, current_sum)

    result = canPartition(len(arr) - 1, target)
    print(result)
