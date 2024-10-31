# ----------------------------- QUEUE ----------------------

# OVERVIEW:
'''
    A queue is a linear data structure that stores the elements in a sequential manner
    Queues implement the FIFO method which is short for First in First Out.
    Elements from a queue are always deleted from the front and added at the rear.
        A typical queue utilizes the following list of functions
        
        represents queue in pythong
        enqueue(element)	inserts element at the end of the queue
        dequeue()	removes an element from the start of the queue
        
        queue helper methods
        front()	returns the first element of the queue
        rear()	returns the last element inserted into the queue
        isEmpty()	checks if the queue is empty
        size()	returns the size of the queue   
'''


# DATA STRUCTURE REPRESENTATION

# QUEUE TYPES
    # Linear Queue
    # Circular Queue
    # Priority Queue
    # Double-ended Queue


# WHY QUEUE ?
'''
    We generally use Queues when:

    We want to prioritize something over another
    A resource is shared between multiple devices
'''


# PROS AND CONS

    # DATA STRUCTURE ADVANTAGES    

    # DATA STRUCTURE DISADVANTAGES
    
# BIG O ANALYSIS 

    # INSERTION - O(1) - EXPLANATION
    # DELETION - O(1) - EXPLANATION
    # ACCESS - O(1) - EXPLANATION
    # SEARCH - O(1) - EXPLANATION
    
# QUEUE IMPLEMENTATION

# In this example we implement a queue using a doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get_head(self):
        if (self.head != None):
            return self.head.data
        else:
            return False
    
    def tail_node(self):
        if (self.head != None):
            return self.tail.data
        else:
            return False

class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()
    
    def is_empty(self):
        return self.items.length == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items.get_head()

    def rear(self):
        if self.is_empty():
            return None
        return self.items.tail_node()

    def size(self):
        return self.items.length
    
    def enqueue(self, value):
        return self.items.insert_tail(value)

    def dequeue(self):
        return self.items.remove_head()

        
queue_obj = MyQueue()