
#Tree builder 

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def addLeft(self, value):
        self.left = Node(value)
        return self.left
    
    def addRight(self, value):
        self.right = Node(value)
        return self.right
    
def get_all_paths(root):
    result = []

    def dfs(node, path):
        if not node:
            return
            
        path.append(str(node.value))

        if not node.left and not node.right:
            result.append(" -> ".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)

        path.pop()
    dfs(root, [])

    return result
    
            

root = Node(10)

left = root.addLeft(5)
right = root.addRight(15)

left.addLeft(2)
left.addRight(7)

right.addRight(20)
