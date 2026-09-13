
def single_non_repeating(nums):

    result = 0 
    for num in nums:
        result ^= num
    return result