# Dynamic Programming - 0/1 Knapsack
# Time Complexity: O(n * capacity) where n = number of items
# Space Complexity: O(n * capacity) - 2D DP table

# given a knapsack with capcity
# weights of each item, values for each item
# find total value you can carry

#Classic DP problem 


def knapsack_01(w, v, capacity):

    n = len(w)
    dp = [[0]*(capacity + 1) for _ in range(n+1)]

    for i in range(1,n+1):
        for cap in range(1, capacity+1):
            if w[i-1] <= cap:
                dp[i][cap] = max(
                    dp[i-1][cap],
                    dp[i-1][cap - w[i-1]] + v[i-1]
                )
            else:
                dp[i][cap] = dp[i-1][cap]

    return dp[n][capacity]