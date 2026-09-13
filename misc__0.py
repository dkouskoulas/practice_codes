





def inorder(root):

    res = [] 

    def dfs(node):
        if not node:
            return 
        
        dfs(node.left)
        res.append(node.value)
        dfs(node.right)

    dfs(root)

    return res


