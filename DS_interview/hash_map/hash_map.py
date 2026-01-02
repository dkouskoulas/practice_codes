from collections import defaultdict

def find_pair_prefix_sum(nums, target):

    seen = defaultdict(int)

    for num in nums:
        if target - num in seen:
            return 'yes'
        seen[num] += 1 

    return 'not found'