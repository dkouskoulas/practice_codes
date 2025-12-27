

def min_sum(arr,k ):

    if k<= 0 or len(arr)<k:
        raise ValueError('k must be postive and less than length of array!')
    
    n = len(arr)

    window_sum = sum(arr[:k])
    min_sum = window_sum

    for i in range(k,n):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        min_sum = min(window_sum, min_sum)

    return min_sum 


if __name__ == "__main__":
    arr = [1, 2, -3, -5, 5, 4, 2, -10, 20, 12, -8, 6, -10, 4, 2, 8, -4, -2, -5, -3]

    result = min_sum(arr, 4)
    print(result)