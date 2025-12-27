# Simple Moving Average with Future Forecast
# Time Complexity: O(n * k) where n = array length, k = window size
# Space Complexity: O(n) - stores forecast arrays

def SMA(arr,k):
    n = len(arr)

    if n < k:
        raise ValueError('Array smaller than window')
    
    forecast = []

    for i in range(k,len(arr)):
        window = arr[i-k:i]
        avg = sum(window)/k
        forecast.append(avg)

    future_forecast = []
    last_window = arr[-k:]  
    next_value = sum(last_window)/k

    for _ in range(k):
        future_forecast.append(next_value)
        last_window = last_window[1:] + [next_value]  # ✓ Slide the window
        next_value = sum(last_window)/k

    return forecast, future_forecast

if __name__ == "__main__":
    arr = [1, 2 ,4 ,6 ,7,  9, 10, 12, 16, 18, 21, 22, 23, 26, 30, 31]
    k = 3
    result_1, result_2 = SMA(arr, k)
    print('The full forecast is:', result_1)
    print('The future forecast is:', result_2)