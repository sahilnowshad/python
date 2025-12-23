def find_median(A, B):

   
    m, n = len(A), len(B)
    total_length = m + n
    
    
    half = (total_length + 1) // 2 
    
  
    i, j = 0, 0   #pointers
    
    prev_element = -1  
    curr_element = -1  

    for _ in range(half):
        prev_element = curr_element
        
        if i < m and (j >= n or A[i] <= B[j]):
            curr_element = A[i]
            i += 1
        else:
            curr_element = B[j]
            j += 1


    if total_length % 2 == 1:
        return curr_element
    
   
    else:
        return (prev_element + curr_element) / 2.0


print(f"Median of [1, 3] and [2]: {find_median([1, 3], [2])}")          
print(f"Median of [1, 2] and [3, 4]: {find_median([1, 2], [3, 4])}")  