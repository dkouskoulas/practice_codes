# Given an array of coin denominations and a target amount,
# find minimum number of coins needed to make up amount
# or determine if impossible


def coin_change(coins, amount):

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x-coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1