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
    
    def PreorderTraversal(self, root):
        # root > left > right
        preorder = []
        if root:
            preorder.append(root.data)
            preorder.extend(self.PreorderTraversal(root.left))
            preorder.extend(self.PreorderTraversal(root.right))
        return preorder

root_node = node(27)
elements = [14, 35,10,19, 31, 42]
for i in elements:
    root_node.insert(i)
# root_node.insert(12)
# root_node.insert(15)
# root_node.insert(20)
# root_node.insert(30)
# root_node.insert(31)

print(root_node.PreorderTraversal(root_node))