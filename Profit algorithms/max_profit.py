# Greedy - Best Time to Buy and Sell Stock
# Time Complexity: O(n) - single pass through prices
# Space Complexity: O(1) - only uses constant extra space





def max_profit(prices):

    max_profit = 0
    min_global = float('inf')

    for price in prices:
        min_global = min(price, min_global)
        max_profit = max(max_profit, price - min_global)
    
    return max_profit
