# creating node class
class Node:
    def __init__(self, item = None, next= None):
        self.item = item
        self.next = next



# creating class of start point which is point to first node
class SLL:
    def __init__(self, head = None):
        self.head = head 

    # creating function which check list is empty or not
    def is_empty(self):
        return self.head == None   # if list is empty it returns True


    # <---------------------------Insert Function--------------------------->
    
    def insert_at_start(self, data):
        n = Node(data, self.head)   # new nodes object
        self.head = n   #  linke new node n to the head

    def insert_at_last( self, data):
        n = Node(data)     # here default value of next is None so we not need to specify it.

        if not self.is_empty():   # checking is list is empty or not
            
            temp = self.head      # temp is help us find previous nodes address initially it points to head.
            while temp.next is not None:
                temp = temp.next   # moving to the next node

            temp.next = n
        else:
            self.head = n

    # inserting new data after specified node:  here first we need to seach this specified data
    def insert_after(self, temp, data):

        if temp is not None:   # here search function is already create below:
            n = Node(data, temp.next)
            temp.next = n
            

    # <-------------------------Searching ----------------------------------->
    
    def searching(self, key):
        temp = self.head
        while temp is not None:

            if (temp.item == key):
                return temp      # if element is found then loop is break because of return value
            temp = temp.next     # moving to next node

        return Node 
    # <-----------------------Delete-------------------------------->

    def delete_head(self):

        if self.head is not None:
            self.head = self.head.next 

    def delete_last(self):

        if self.head is None:           # checking list is empty
            print("Underflow..!")
            
        elif self.head.next is None:       # checking list has only 1 node
            self.head = None

        else:                             # list is not None

            temp = self.head
            while temp.next.next is not None:   # checking the next nodes next is not None
                temp = temp.next

            temp.next = None            # after loop we got 2nd last node so place it as None


    def delete_given_data(self, data):

        if self.head is None:
            print("Underflow..!")

        elif self.head.next is None:

            if self.head.item == data:
                self.head = None
            
        else:
            temp = self.head   
            if temp.item == data:        # checking deleting item is First node then
                temp.head = temp.next    # puting next node into head
                
            else:
                
                while temp.next is not None:
                    
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    # <-------------------------Display------------------------------>

    def Display(self):
        temp = self.head
        while temp is not None:
            print(temp.item , end=" ")
            temp = temp.next


# <-------------SLL iteration-------------------->

class DLLiterator: 
    def __init__(self, head): 
        self.current = head 
    def __iter__(self): 
        return self 
    def __next__(self): 
        if self.current is None: 
            raise StopIteration 
        else: 
            data = self.current.data 
            self.current = self.current.next 
            return data