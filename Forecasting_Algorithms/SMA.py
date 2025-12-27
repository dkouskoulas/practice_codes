

def rolling_sma_forecast(arr, k):
    if len(arr)<k:
        raise ValueError('length mismatch')
    
    smoothed_series = []

    for i in range(k,len(arr)):
        window = arr[i-k:i]
        smoothed_series.append(sum(window)/k)

    return smoothed_series, arr[-k:] 


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 14, 17, 18, 21, 24, 27, 29]
    result, future = rolling_sma_forecast(arr, 3)

    print(result)
    print(future)