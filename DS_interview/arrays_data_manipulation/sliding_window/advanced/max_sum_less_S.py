
def max_sum_subararay_leq_s(nums, S):
    
    left = curr_sum = max_sum = 0

    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > S:
            curr_sum -= nums[left]
            left +=1 
        max_sum = max(curr_sum, max_sum)
        
    return max_sum