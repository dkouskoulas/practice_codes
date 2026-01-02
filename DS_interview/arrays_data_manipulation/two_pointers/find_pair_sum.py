

def find_pair_sum(nums, target):

    left, right = 0, len(nums) - 1 
    
    while left < right:
        cur_val = nums[left] + nums[right]
        if cur_val == target:
            return [nums[left], nums[right]]
        elif cur_val < target:
            left += 1
        else: 
            right -= 1
    return None