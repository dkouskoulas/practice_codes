# Greedy - Maximum Profit (Buy Low, Sell High)
# Time Complexity: O(n) - single pass through prices
# Space Complexity: O(1) - only uses constant extra space


def max_profit(prices):

    min_price = float('inf')
    max_profit = 0 

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


if __name__ == "__main__":
    prices = [-2, 10, -5, 4, 2, 25, -2, 4 ]
    result = max_profit(prices)

    print(result)