

def mirror(root):

    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    
    mirror(root.left)
    mirror(root.right)

    return root 