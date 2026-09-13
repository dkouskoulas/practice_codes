

"""
LOWEST COMMON Ancestor (LCA)

think... look at the path up to root... look at common nodes and than take the lowest/deepest 

Given the root of a binary tree and two nodes p and q,
return their lowest common ancestor (LCA).

The LCA of two nodes is the lowest (deepest) node in the tree
that has both p and q as descendants (a node can be a descendant of itself).

Example:

        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

LCA(5, 1) = 3
LCA(6, 4) = 5
LCA(7, 8) = 3

Goal:
Find the node where the paths to p and q split.
"""
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 


def lca(root, p, q):

    if not root or root == p or root == q:
        return root
    
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    

    return left if left else right