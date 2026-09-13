

def move_zeros(nums):

    left = 0 

    for right in range(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 


    return nums[:left]


