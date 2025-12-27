

# given array nums and val, remove all occurences of val in place,
# return the  new length (k) with the first k elements being the ones you keep



def remove_elements(nums, val):

    slow = 0 

    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1 

    return slow, nums[:slow]

