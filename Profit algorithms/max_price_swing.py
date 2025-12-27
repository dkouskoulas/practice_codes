

def max_price_swing(prices):

    min_global = float('inf')
    max_swing = 0 

    for price in prices:

        min_global = min(price, min_global)
        max_swing = max(max_swing, price - min_global)

    return max_swing