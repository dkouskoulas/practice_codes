

def longest_contiguous_increasing(nums):
    if not nums:
        return 0 

    cur_max = 1 
    count = 1

    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
            cur_max = max(count, cur_max)
        else:
            count = 1 
    return cur_max