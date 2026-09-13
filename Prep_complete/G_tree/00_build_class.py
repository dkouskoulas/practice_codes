
"""
Node class that bilds childrean from values
"""

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