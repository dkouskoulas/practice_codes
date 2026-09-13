transactions = [10, 20, 30, 40, 100, 50, 20]

window_size = 3

def flag_fraud(transactions, window_size):
    """
    Flags indices where the transaction is greater than twice the average of the previous window.
    Returns a list of indices.
    """
    n = len(transactions)
    if window_size > n or window_size <= 0:
        return []
    
    indices = []
    window_sum = sum(transactions[:window_size])
    for i in range(window_size, n):
        if transactions[i] > (2 * window_sum) / window_size:
            indices.append(i)
        window_sum += transactions[i] - transactions[i - window_size]
    return indices

# Print flagged indices
print(flag_fraud(transactions, window_size))
