def two_non_repeating(nums):
    xor = 0
    for num in nums:
        xor ^= num
    # Find rightmost set bit
    diff = xor & -xor
    x = y = 0
    for num in nums:
        if num & diff:
            x ^= num
        else:
            y ^= num
    return x, y