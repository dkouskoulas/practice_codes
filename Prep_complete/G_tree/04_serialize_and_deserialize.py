

def serialize(root):
    vals = []

    def dfs(node):

        if not node:
            vals.append("N")
            return
        vals.append(str(node.value))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(vals)



def serialize(root):

    vals = []

    def dfs(node):

        if not node:
            vals.append("N")
            return
        vals.append(str(node.value))
        dfs(node.left)
        dfs(nod.right)
    
    dfs(root)
    return ",".join(vals)