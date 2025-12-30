# Simple Moving Average (SMA)
# Time Complexity: O(n * k) where n = array length, k = window size
# Space Complexity: O(n) - stores smoothed series


def rolling_sma_forecast(arr, k):
    if len(arr)<k:
        raise ValueError('length mismatch')
    
    smoothed = []

    for i in range(k,len(arr)):
        window_sum = sum(arr[i-k:i])/k
        smoothed.append(window_sum)

    return smoothed


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 14, 17, 18, 21, 24, 27, 29]
    result, future = rolling_sma_forecast(arr, 3)

    print(result)
    print(future)