

def partition_array(nums):
    
    left, right = 0, len(arr) = 1 

    while left < right:
        while left < right and nums[left] < 0:
            left += 1 
        while left < right and nums[right] >= 0:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    return nums