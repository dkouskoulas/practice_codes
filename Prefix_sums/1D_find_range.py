

def prefix_calc(nums):
    
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    return prefix

def range_calc(prefix, i, j):
    return (prefix[j + 1] - prefix[i])