def moving_average(data, window_size, forecast_k=3):
    """
    Calculates moving average and forecasts up to k points ahead using the last moving average value.
    """
    smoothed_series = []
    n = len(data)
    if window_size > n or window_size <= 0:
        return smoothed_series

    window_sum = sum(data[:window_size])
    smoothed_series.append(window_sum / window_size)

    for i in range(window_size, n):
        window_sum += data[i] - data[i - window_size]
        smoothed_series.append(window_sum / window_size)

    # Forecast k points ahead using the last moving average
    if smoothed_series:
        last_avg = smoothed_series[-1]
        for _ in range(forecast_k):
            smoothed_series.append(last_avg)

    return smoothed_series