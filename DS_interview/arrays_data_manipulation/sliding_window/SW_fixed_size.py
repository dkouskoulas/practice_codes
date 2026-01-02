

def max_sum(nums, k):

    n = len(nums)
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k,n):
        window_sum += nums[i]
        window_sum -= nums[i-k]
        max_sum = max(window_sum, max_sum)

    return max_sum