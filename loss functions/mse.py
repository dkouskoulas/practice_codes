

def mse_calc(x,y):

    if len(x) != len(y):
        raise ValueError('array size mismatch')
    
    n = len(x)

    vals = [(1/n)*(y-x)**2 for x,y in zip(x,y)]

    return sum(vals)