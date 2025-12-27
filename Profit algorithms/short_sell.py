
#for short selling, you need to track the maximum 
# you sell high and buy low 

def short_sell(arr):

    if not arr:
        return 0
    

    max_global = arr[0]
    max_profit = 0 

    for price in arr:
        profit = max_global - price

        max_profit = max(max_profit, profit)

        max_global = max(max_global, price)

    return max_profit


    