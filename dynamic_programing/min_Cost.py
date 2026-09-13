# Question:
# Given an array cost where cost[i] is the cost to step on the ith stair,
# find the minimum cost to reach the top of the stairs.
# You can start at step 0 or step 1, and at each move, you can climb one or two steps.


def minimum_cost(costs):
    
    n = len(costs)

    if n == 0:
        return 0 
    if n == 1:
        return costs[0] 
    
    dp = [0]*n
    dp[0] = costs[0]
    dp[1] = costs[1]

    for i in range(2, len(costs)):
        dp[i] = costs[i] + min(dp[i-1], dp[i-2])
        

    return min(dp[-1], dp[-2])