

def max_path_sum(root):

    if not root:
        return float('-inf')
    

    if not root.left and not root.right:
        return root.value
    
    left = max_path_sum(root.left)
    right = max_path_sum(root.right)


    return root.valeu + max(left, right)