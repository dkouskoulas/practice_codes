

def previx_sum(nums):

    if not nums:
        return -1 
    
    prefix = []
    running_sum = 0

    for num in nums:
        running_sum += num
        prefix.append(num)

    return prefix