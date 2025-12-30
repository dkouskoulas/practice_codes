# Simple Moving Average with Future Forecast
# Time Complexity: O(n * k) where n = array length, k = window size
# Space Complexity: O(n) - stores forecast arrays

def SMA(arr,k):
    n = len(arr)

    if n < k:
        raise ValueError('Array smaller than window')
  
    smoothed = []

    for i in range(k,len(arr)):
        new_value = sum(arr[i-k:i])/k
        smoothed.append(new_value)

    future_forecast = []
    last_window = arr[-k:]
    new_value = sum(last_window)/k

    for _ in range(k):
        future_forecast.append(new_value)
        last_window = last_window[1:] + [new_value]
        new_value = sum(last_window)/k

    return future_forecast

if __name__ == "__main__":
    arr = [1, 2 ,4 ,6 ,7,  9, 10, 12, 16, 18, 21, 22, 23, 26, 30, 31]
    k = 3
    result_1 = SMA(arr, k)
    print('The full forecast is:', result_1)
