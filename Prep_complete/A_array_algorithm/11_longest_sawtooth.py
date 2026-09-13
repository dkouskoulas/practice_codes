

def longest_sawtooth(nums):
    if not nums:
        return -1 
    
    max_len = 1
    count = 1 


    for i in range(1, len(nums)):
        if nums[i] % 2 != nums[i-1] % 2:
            count += 1
            max_len = max(max_len, count)
        else:
            count = 1

    return max_len