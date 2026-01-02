
def prefix_sum_array(nums):
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix

def range_sum(prefix, i, j):
    return prefix[j+1] - prefix[i]