

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

def LCA(root, p, q):
    if not root or root==p or root == q:
        return root
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if right and left:
        return root
    return left if left else right


def mirror(root):
    if not root:
        return root
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)
    return root

def is_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.value != root2.value:
        return False
    return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)

def validate_bst(root):

    def dfs(node, low, high):

        if not node:
            return True

        if not (low < node.value < high):
            return False

        return dfs(node.left, low, node.value) and dfs(node.right, node.value, high)

    return dfs(root,float('-inf'), float('inf'))


def serialize(root):
    vals = []

    def dfs(node):
        if not node:
            vals.append("N")
            return

        vals.append(str(node.value))
        dfs(node.left)
        dfs(right.right)

    dfs(root)
    return ",".join(Vals)


def deserialzie(root):
    vals = iter(data.split(","))

    def dfs():
        val = next(val)
        if val == "N":
            return None

        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()


def get_paths(root):

    res = []

    def dfs(node, path):
        if not node:
            return node

        path.append(str(node.val))

        if not node.left and not node.right:
            res.append("->".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()
    dfs(root, [])
    return res
    