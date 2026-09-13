


def inorder_iterative(root):

    stack = []
    result = []
    current = root 


    while current or stack:

        # go as far lesft as possible 
        while current:
            stack.append(current)
            current = current.left

        # process node
        current = stack.pop()
        result.append(current.value)

        # go right
        current = current.right


    return result 