

def best_time(prices):

    min_price = float('inf')
    max_profit = 0

    min_idx = 0
    sell_idx = 0
    buy_idx = 0

    for i, price in enumerate(prices):
        if price < min_price:
            min_idx = i
            min_price = price
        elif price - min_price > max_profit:
            max_profit = prices[i] - min_price
            buy_idx = min_idx
            sell_idx = i 

    return buy_idx, sell_idx, max_profit