# Question:
# Given an array nums where each element represents the maximum jump length from that position,
# determine if you can reach the last index starting from the first index.
# Return True if you can reach the end, False otherwise.

def can_jump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:
            return True
    return True
