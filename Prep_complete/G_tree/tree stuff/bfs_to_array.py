
from collections import deque

def bfs_levels(root):

    if not root:
        return [] 
    
    q = deque([root])
    result = []


    while q:
        level = []
        size = len(q)

        for _ in range(size):
            node = q.popleft()
            level.append(node.value)


            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)

    return result