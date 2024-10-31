# ----------------------------- LINKED LIST ----------------------

# OVERVIEW:
'''
    A linked list is a list made up of nodes that consists of two parts.
        Data - contains data or value i.e 4 or 'joe'
        Next - contains the address of the next node of the list (this link is represented as the .next property in our real linked list)
        
        The data component allows a node in the linked list to store an element of data 
        that can be of type string, character, number, or any other type of object. 
        
        The next component in every node is a pointer that points from one node to another.

        The start of the linked list is referred to as the head. 
        head is a pointer that points to the beginning of the linked list, 
        so if we want to traverse the linked list to obtain or access an element of the linked list, we'll start from head and move along.
        
        The last component of a singly linked list is a notion of null. 
        This null idea terminates the linked list. In Python, we call this None. 
        The last node in a singly linked list points to a null object, 
        and that tells you that it's the end of the linked list.
'''


# DATA STRUCTURE REPRESENTATION
'''
    Suppose we want to store a list of numbers: 23,54,78,90
        We must create 4 different nodes
            Data: 23 Link: 2000  Data: 54 Link: 3000  Data: 78 Link: 4000  Data: 90 Link: NULL
            The Link in each node represents the address of the next node in list
'''

# LINKED LIST TYPES
   # Single Linked List: Navigation is forward only (pointers are uni-directional)
   # Doubly linked list: Forward and backward navigation is possible 
   # Circular Linked list: Last element is linked to the first element


# WHY LINKED LIST?


# PROS AND CONS

    # LINKED LIST ADVANTAGES    

    # LINKED LIST DISADVANTAGES
    
# BIG O ANALYSIS 

    # INSERTION - O(1) - EXPLANATION
    # DELETION - O(1) - EXPLANATION
    # ACCESS - O(n) - EXPLANATION
    # SEARCH - O(n) - EXPLANATION
    
# LINKED LIST IMPLEMENTATION

# When we create our own singly linked list we write a node class which initializes the data and link  
class ListNode:
    def __init__(self, data):
        self.data = data # current value in list
        self.next = None # next value in list initialized as None or NULL 


# When we create our own singly linked list we write a class
# head property points to first node in SSL#
class LinkedList:
    def __init__(self):
        self.head = ListNode(-1) # defines head pointer which will point to the first node in linked list here we use dummy node can also be initialized with None
        self.tail = self.head # defines tail or end of node will help with intertion
        
    def get(self, index): # should return value of the Ith node, node of given index
        current = self.head.next
        i = 0
        
        while current:
            if i == index:
                return current.data
            i += 1
            current = current.next
            
        return -1 # index out of bounds
    
    def insertHead(self, data): # will insert a node with data at the head of the list
        new_node = ListNode(data)
        new_node.next = self.head.next
        self.head.next = new_node
        
        if not new_node.next:
            self.tail = new_node

            
    def insertTail(self, data): # will insert a node with data at the tail of the list
        self.tail.next = ListNode(data)
        self.tail = self.tail.next
        
    def remove(self, index): # will remove the Ith node 
        i = 0
        current = self.head
        while i < index and current:
            # move current to node before target node
            i += 1
            current = current.next
            
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
                
            current.next = current.next.next 
            return True
        return False
    
    def getData(self): # returns array of all the values in the linked list
        current = self.head.next
        res = []
        
        while current:
            res.append(current.data)
            current = current.next
            
        return res