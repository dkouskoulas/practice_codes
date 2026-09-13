

def max_sum_size_k(arr,k):

    n = len(arr)
    max_sum = float ('-inf')

    window_sum = sum(arr[:k])

    max_sum = max(window_sum, max_sum)

    for i in range(k,n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(window_sum,max_sum)

    return max_sum

