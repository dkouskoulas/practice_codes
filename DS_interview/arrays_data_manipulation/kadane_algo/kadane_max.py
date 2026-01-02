


def kadane_algo(nums):

    local_max = global_max = float('-inf')
    
    for num in nums:
        local_max = max(num, local_max + num)
        global_max = max(global_max, local_max)

    return global_max