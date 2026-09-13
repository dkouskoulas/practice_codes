
"""
Minimum Jumps to Reach End

Given an array of non-negative integers where each element represents 
the maximum jump length from that position, find the minimum number of 
jumps needed to reach the last index from the first index.

Example:
    Input: nums = [2, 3, 1, 1, 4]
    Output: 2
    Explanation: Jump from index 0 to 1, then to the last index

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

def min_jumps(nums):

    if n <= 1:
        return 0

    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0 

    for i in range(len(nums)):
        for j in range(i):
            if j + nums[j] >= i:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]