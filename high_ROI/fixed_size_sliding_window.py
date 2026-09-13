

def max_sum_subarry_k(nums,k):

    if k > len(nums):
        raise ValueError('lenght mismatch')

    max_sum = float('-inf')
    window_sum = sum(nums[:k])
    max_sum = max(max_sum, window_sum)

    for i in range(k,len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum
        