
def max_sum(arr, k):

    n= len(arr)
    if k<= 0 or len(arr)<k:
        raise ValueError("k must be positive and less than len(arr)")
    
    window_sum = sum(arr[:k])
    global_max = window_sum

    for i in range(k,len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        global_max = max(window_sum, global_max)

    return global_max

