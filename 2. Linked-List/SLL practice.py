

class Node:
    def __init__(self, item= None, next= None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, head= None):
        self.head = head

    def is_empty(self):
        return self.head == None
    
    def insert_at_first(self, data):
        n = Node(data, self.head)
        self.head = n

    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.head= n
            
        else:
            temp = self.head
            while temp.next is not None:
                temp= temp.next
            temp.next = n

    def search(self, key):
        temp = self.head
        while temp is not None:
            if (temp.item == key):
                return temp
            temp = temp.next

        return Node 

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
              
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.item, end="  ")
            temp = temp.next
    
    def __iter__(self):
        return sll_iterator(self.head)


class sll_iterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
        
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
        

l = SLL()

print(l.is_empty())

l.insert_at_first(10)
l.print()
print("\n")
l.insert_at_last(50)
l.print()
print("\n")
l.insert_after(l.search(10), 20)
l.print()
print("\n")
l.insert_after(l.search(20), 30)
l.print()
print("\n")
l.insert_after(l.search(30), 40)
l.print()
print("\n")
l.search(30)



for i in SLL():
    print(i, end=" ")