
def max_sum_k_elements(arr, k):
    n = len(arr)

    if n < k:
        raise ValueError(" k larger than array length")
    
    window_sum = sum(arr[:k])
    max_sum = window_sum 

    for i in range(k,n):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum