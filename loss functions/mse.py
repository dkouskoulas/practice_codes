# Mean Squared Error Calculation
# Time Complexity: O(n) - single pass through arrays
# Space Complexity: O(n) - list comprehension creates intermediate list


def mse_calc(x,y):

    if len(x) != len(y):
        raise ValueError('array size mismatch')
    
    n = len(x)

    vals = [(1/n)*(y-x)**2 for x,y in zip(x,y)]

    return sum(vals)