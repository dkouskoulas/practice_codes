

def are_identical(root1, root2):

    if not root1 and not root2:
        return True
    
    if not root1 or not root2:
        return False
    
    if root1.value != root2.value:
        return False
    
    return are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right)