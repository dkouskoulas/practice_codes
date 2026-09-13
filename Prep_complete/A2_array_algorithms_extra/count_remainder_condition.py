
"""
Subarray Sum Divisible by K

Given an integer array nums and an integer k, return the number of
contiguous subarrays whose sum is divisible by k.

A subarray is a contiguous sequence of elements.

Example:
Input: nums = [4, 5, 0, -2, -3, 1], k = 5
Output: 7

Explanation:
There are 7 subarrays whose sum is divisible by 5.
"""

def count_remainder_k(nums, k):

    prefix_sum = 0
    pref_freq = {0: 1}
    count = 0


    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k
        if remainder in pref_freq:
            count += pref_freq[remainder]
        pref_freq[remainder] = pref_freq.get(remainder, 0) + 1 

    return count