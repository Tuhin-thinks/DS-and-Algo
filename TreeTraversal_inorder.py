"""
Binary Inorder Traversal Algorithm
"""
class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def PrintTree(self):
        if self.left:  # left
            self.left.PrintTree()
        
        print(self.data)  # root
        
        if self.right:  # right
            self.right.PrintTree()

root = node(10)  # create root node with data 10
root.insert(12)
root.insert(-1)
root.insert(10)
root.insert(50)
root.PrintTree()