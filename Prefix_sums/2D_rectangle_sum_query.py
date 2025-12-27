

def build_2d_prefix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])

    prefix = [[0] * (cols + 1) for _ in range(rows+1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1 ):
            prefix[i][j] = (matrix[i-1][j-1] +
                                  prefix[i-1][j] + 
                                  prefix[i][j-1] -
                                  prefix[i-1][j-1])
            
    return prefix


def rectangle_sum(prefix, r1, c1, r2, c2):

    r1, c1, r2, c2 = r1 + 1, c1+1, r2 + 1, c2 + 1 

    return (prefix[r2][c2] - 
            prefix[r1-1][c2] -
            prefix[r2][c1-1] + 
            prefix[r1-1][c1-1]
    )