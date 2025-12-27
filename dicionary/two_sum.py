# Hash Map - Two Sum
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(n) - hash map stores up to n elements

from collections import defaultdict

def two_sum(nums, target):

    my_dict = defaultdict(int)


    for idx, num in enumerate(nums):
        if target - num in my_dict:
            return [my_dict[target-num], idx]
        my_dict[num] = idx
    
    return None