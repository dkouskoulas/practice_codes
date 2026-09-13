

def max_subarray(nums):

    cur_max = global_max = float('-inf')

    for num in nums:
        cur_max = max(num, cur_max+num)
        global_max = max(cur_max, global_max)
        
    return global_max