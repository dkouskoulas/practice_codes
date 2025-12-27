# Kahn's Algorithm - Topological Sorting
# Time Complexity: O(V + E) where V = vertices, E = edges
# Space Complexity: O(V + E) - adjacency list and indegree array

#topological sorting for a directed acyclical graph

from collections import deque


def kahn_toposort(n: int, edges: list[tuple[int, int]]) -> list[int]:

    adj = {i: [] for i in range(n)}

    indegree = [0]*n

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1


    #initially takes only the first layer but is not a static deifnition
    queue = deque(i for i in range(n) if indegree[i] == 0)
    
    topo = []

    while queue:
        u = queue.popleft()
        topo.append(u)

        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)


    if len(topo) != n:
        raise ValueError("Cycle detected")

    return topo
