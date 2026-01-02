


def max_sum_subarray_leq_s(nums, kk):

    max_sum = float('inf')

    for size in range(1, kk+1):
        window_sum = sum(nums[:size])
        max_sum = max(max_sum, window_sum)
        for i in range(size, len(nums)):
            window_sum += nums[i] - nums[i-size]
            max_sum = max(max_sum, window_sum)

    return max_sum