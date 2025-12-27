# Kadane's Algorithm - Maximum Subarray Sum (Circular Array)
# Time Complexity: O(n) - two passes through array
# Space Complexity: O(n) - creates inverted array in min_subarray

def max_subarray(nums):

    max_global = max_local = nums[0]

    for num in nums[1:]:
        max_local = max(num, max_local + num)
        max_global = max(max_global, max_local)

    return max_global

def min_subarray(nums):
    
    nums = [-x for x in nums]

    max_global = float('-inf')
    max_local = nums[0]

    for num in nums[1:]:
        max_local = max(num, max_local + num)
        max_global = max(max_global, max_local)

    return -max_global

def circular_var(nums):

    #calculate min and max from linear
    max_kadane = max_subarray(nums)
    if max_kadane < 0:
        return max_kadane
    min_kad = min_subarray(nums)
    
    total_sum = sum(nums)
    max_circular = total_sum - min_kad

    return max(max_kadane, max_circular)