

class Node:
    def __init__(self, item= None, left= None, right= None):
        self.item = item
        self.left = left
        self.right= right
    
class BinarySearchTree:
    def __init__(self, root= None):
        self.root = root

        
#<------------------  Insertion --------------------------------->#

    def insertion(self, data):
        self.root = self.rinsert(self.root, data)   # inserting new node into 

    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)   
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root

#<---------------- Searching --------------------------------->#
    
    def search(self, data):
        return self.rec_search(self.root, data)

    def rec_search(self, root, data):
        if root is None or root.item == data:
            return root
        elif data < root.item:
            return self.rec_search(root.left, data)
        else:
            return self.rec_search(root.right, data)


#<---------------- Inorder Traverse --------------------------------->#

    def inorder(self):
        result = []
        self.rec_inorder(self.root, result)
        return result

    def rec_inorder(self, root, list):
        if root:
            self.rec_inorder(root.left, list)
            list.append( root.item)
            self.rec_inorder(root.right, list)

#<---------------- preorder Traverse --------------------------------->#

    def preorder(self):
        result = []
        self.rec_preorder(self.root, result)
        return result

    def rec_preorder(self, root, list):
        if root:
            list.append( root.item)
            self.rec_preorder(root.left, list)
            self.rec_preorder(root.right, list)
            
#<---------------- Postorder Traverse --------------------------------->#

    def postorder(self):
        result = []
        self.rec_postorder(self.root, result)
        return result

    def rec_postorder(self, root, list):
        if root:
            self.rec_postorder(root.left, list)
            self.rec_postorder(root.right, list)
            list.append( root.item)

#<---------------- Minimum value --------------------------------->#
    def min_value(self):
        temp = self.root
        current = temp
        while current.left is not None:
            current = current.left
        return current.item

#<---------------- Maximum Value --------------------------------->#
    def max_value(self):
        temp = self.root
        current = temp
        while current.right is not None:
            current = current.right
        return current.item


#<---------------- Deletion in nodes --------------------------------->#

    def delete(self, data):
        self.root = self.rec_delete(self.root, data)
    def rec_delete(self, root, data):
        if root is None:
            return None
        elif data < root.item:
            root.left = self.rec_delete(root.left, data)
        elif data > root.item:
            root.right = self.rec_delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left          
            root.item= self.min_value(root.right)
            self.rec_delete(root.right, root.item)
        return root
    

#<---------------- Total No. of elements  ----------------------------->#
    def size(self):
        return len(self.inorder())
            
    
    

t = BinarySearchTree()
t.insertion(8)
t.insertion(3)
t.insertion(10)
t.insertion(1)
t.insertion(6)
t.insertion(14)
t.insertion(4)
t.insertion(7)
t.insertion(13)  

t.inorder()

t.preorder()

t.postorder()

t.min_value()
t.max_value()

t.delete(10)

t.inorder()



        