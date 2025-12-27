




def max_profit(prices):

    max_profit = 0
    min_global = float('inf')

    for price in prices:
        min_global = min(price, min_global)
        max_profit = max(max_profit, price - min_global)
    
    return max_profit
