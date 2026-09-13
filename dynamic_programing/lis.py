"""
Longest Increasing Subsequence

Given an array of integers, find the length of the longest strictly 
increasing subsequence. A subsequence is derived from the array by 
deleting some or no elements without changing the order of the remaining elements.

Example:
    Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4
    Explanation: The longest increasing subsequence is [2, 3, 7, 101]

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

def length_of_LIS(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] +1)
                
    return max(dp)
    
