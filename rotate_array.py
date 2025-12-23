#rotate an array to right by k-steps
def rotate_array(nums, k):
    n = len(nums)

    k = k % n


    rotated = [0] * n

   
    for i in range(n):
        new_index = (i + k) % n
        rotated[new_index] = nums[i]

    return rotated


# Example
arr = [1, 2, 3, 4, 5]
k = 2
print("Original array:", arr)
print("Rotated array :", rotate_array(arr, k))