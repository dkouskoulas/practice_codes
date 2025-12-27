from heapq import heappush, heappop

def closest(points, k):

    def get_dist(x,y):
        return x**2 + y**2
    
    min_heap = []
    n = len(points)

    for i in range(n):
        x = points[i][0]
        y = points[i][1]
        heappush(min_heap, (get_dist(x,y), points[i]))

    res = []

    for i in range(k):
        res.append(heappop(min_heap)[1])

    return res