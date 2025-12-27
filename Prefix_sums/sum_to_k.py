

def subarray_sum(arr,k):

    prefix_sum = 0 
    prefix_map = {0: -1}

    for i, num in enumerate(arr):
        prefix_sum += num 

        if (prefix_sum - k) in prefix_map:
            start = prefix_map[prefix_sum - k] + 1
            return [start, i]
        
        prefix_map[prefix_sum] = i

    return None