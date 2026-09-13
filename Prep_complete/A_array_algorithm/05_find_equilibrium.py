
"""
Equilibrium Index Problem

Given an array of integers, find an index such that the sum of elements
to the left of the index equals the sum of elements to the right.

Return the first such index, or -1 if none exists.

Notes:
- The element at the index is not included in either sum.
- Array may contain positive, negative, and zero values.
- Single-element array returns 0.
"""


def find_equilibrium(arr):
    if not arr:
        raise ValueError('Missing array!')
    
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        right_sum = total_sum - num - left_sum
        if left_sum == right_sum:
            return i 
        left_sum += num
        

    return -1 