

#note you start at 1 because 0-index is always correct
def remove_duplicates(nums):

    slow = 1 

    for fast in range(1,len(nums)):
        if nums[fast] != nums[slow-1]:
            nums[slow] = nums[fast]
            slow += 1
             
    return slow, nums[:slow]