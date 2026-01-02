# Sliding Window - Maximum Sum of Fixed Window Size
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(1) - only uses constant extra space

def max_sum(arr, k):

    n= len(arr)
    if k<= 0 or len(arr)<k:
        raise ValueError("k must be positive and less than len(arr)")
    
    cur_sum = sum(arr[:k])
    max_sum = cur_sum

    for i in range(k, len(arr)):
        cur_sum += arr[i]
        cur_sum -= arr[i-k]
        max_sum = max(cur_sum, max_sum)
    
    return max_sum
