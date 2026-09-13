
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return []

    return inorder(root.left) + [root.value] + inorder(root.right)