

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def is_valid_bst(root):

    def dfs(node, low, high):
        if not node:
            return True
        
        if not (low < node.value < high):
            return False
        

        return dfs(node.left, low, node.value) and dfs(node.right, node.value, high)
    
    return dfs(root, float('-inf'), float('inf'))