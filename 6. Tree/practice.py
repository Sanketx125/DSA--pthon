

class Node:
    def __init__(self, item= None, left= None, right= None):
        self.item = item
        self.left = left
        self.right= right
    
class BinarySearchTree:
    def __init__(self):
        self.root= None

    def insert(self, data):
        self.rec_insert(self.root, data)

    def rec_insert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.item:
            root.left = self.rec_insert(root.left, data)
        elif data > root.item:
            root.left = self.rec_insert(root.right, data)

        return Node
    
    def searching(self, data):
        return self.rec_search(self.root, data)
    
    def rec_search(self, root, data):
        if root is None or root.item == data:
            return root
        elif data < root.item:
            return self.rec_search(root.left, data)
        elif data > root.item:
            return self.rec_search(root.right, data)
        
    
    def inorder(self):
        result = []
        self.rec_inorder(self.root, result):
        return result
    def rec_inorder(self, root, list):
        if root is not None:
            self.rec_inorder(root.left, list)
            list.append(root.item)
            self.rec_inorder(root.right, list)

    def preorder(self):
        result = []
        self.rec_preorder(self.root, result)
        return result
    def rec_preorder(self, root, list):
        if root is not None:
            list.append(root.item)
            self.rec_preorder(root.left, list)
            self.rec_preorder(root.right, list)

    def postorder(self):
        result = []
        self.rec_postorder(self.root, result)
        return result
    def rec_postorder(self, root, list):
        if root is not None:
            self.rec_postorder(root.left, list)
            self.rec_postorder(root.right, list)
            list.append(root.item)
            



        