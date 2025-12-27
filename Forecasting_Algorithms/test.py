def sma_forecast(arr, k):
    """
    Compute k-step future forecast using Simple Moving Average.
    
    Args:
        arr: historical time series (list/array)
        k: window size for SMA
    
    Returns:
        future_forecast: list of k future predictions
    """
    if len(arr) < k or k <= 0:
        raise ValueError(f"Need len(arr) >= k > 0, got len={len(arr)}, k={k}")
    
    forecast = []
    
    for i in range(k, len(arr)):
        window = arr[i-k:i]
        forecast.append(sum(window)/k)
    
    # Start from the most recent k values
    last_window = arr[-k:]
    new_value = sum(last_window) / k
    
    future_forecast = []
    for _ in range(k):
        future_forecast.append(new_value)
        last_window = last_window[1:] + [new_value]
        new_value = sum(last_window) / k

    return future_forecast


# Example usage (uncomment to test):
# if __name__ == "__main__":
#     data = [10, 20, 30, 40, 50, 60, 70]
#     forecast = sma_forecast(data, k=3)
#     print(f"Future forecast: {forecast}")
