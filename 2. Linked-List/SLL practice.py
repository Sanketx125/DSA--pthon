

class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self, head= None):
        self.head = head

    def is_empty(self):
        return self.head == None
    
    def insert_at_start(self, data):
        n = Node(data, self.head)
        self.head = n
    
    def insert_at_last(self, data):
        n= Node(data)

        if not self.is_empty():
            
            temp = self.head
            while temp.next is not None:
                temp= temp.next
            temp.next = n
        else:
            temp.head = n

    def search(self, key):
        temp= self.head
        while temp is not None:

            if( temp.item == key):
                return temp
            temp = temp.next

        return Node



    