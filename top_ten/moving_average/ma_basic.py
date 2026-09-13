def moving_average(data, window_size):

    smoothed_series = []
    n = len(data)
        
    if window_size > n or window_size <= 0:
        return smoothed_series

    window_sum = sum(data[:window_size])
    smoothed_series.append(window_sum/window_size)

    for i in range(window_size, n):
        window_sum += data[i] - data[i-window_size]
        smoothed_series.append(window_sum/window_size)


    return smoothed_series