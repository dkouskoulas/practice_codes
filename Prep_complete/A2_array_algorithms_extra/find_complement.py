

def sum_to_k(nums, k):

    if not nums:
        return -1 
    
    seen = {}

    for num in nums:
        complement = k - num
        if complement in seen:
            return True
        seen[num] = seen.get(num,0) + 1
    
    return False