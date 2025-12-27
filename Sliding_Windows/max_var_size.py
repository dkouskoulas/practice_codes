# Sliding Window (Variable Size) - Longest Subarray with Sum K
# Time Complexity: O(n) - each element visited at most twice
# Space Complexity: O(1) - only uses constant extra space


#assume all positive values 

def longest_subarray_sum_k(arr, k):

    left = 0
    current_sum = 0
    max_length = 0 
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        if current_sum == k:
            max_length = max(max_length, right - left + 1)

    return max_length