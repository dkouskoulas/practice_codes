

def dfs_levels(root):

    result = [] 

    def dfs(node, depth):
        if not node:
            return 
        
        if depth == len(result):
            result.append([])

        result[depth].append(node.value)


        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)


    dfs(root, 0)
    return(result)