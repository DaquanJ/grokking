# ----------------------------- HEAP / PRIORITY QUEUE ----------------------

# OVERVIEW:
'''
Heaps are advanced data structures that are useful in applications such as sorting and implementing priority queues. 
They are regular binary trees with two special properties

Heaps must be Complete Binary Trees
A Complete Binary tree is a tree where each node has at most two children and the nodes at all levels are full, except for the leaf nodes which can be empty.

Some Complete Binary Tree Properties:

All leaves are either at depth d or depth d-1.
The leaves at depth d are to the left of the leaves at depth d-1
There is at most one node with just one child
If the singular child exists, it is the left child of its parent
If the singular child exists, it is the rightmost leaf at depth d.

The Heap Order Property
The nodes must be ordered according to the Heap Order Property. 
The heap order property is different for the two heap structures MIN HEAP / MAX HEAP
'''

# DATA STRUCTURE REPRESENTATION

# Min Heap
'''
Min Heap Property:
In Min-Heaps, all the parent node keys are less than or equal to their child node keys. 
So the root node, in this case, will always contain the smallest element present in the Heap. 
If Node A has a child node B, then:

    key(A)<=key(B)
'''

# Max Heap
'''
Max Heap Property:
All the parent node keys must be greater than or equal to their child node keys in max-heaps. 
So the root node will always contain the largest element in the Heap. 
If Node A has a child node B, then:

    key(A)>=key(B)
'''


# WHY HEAPS?
# The primary purpose of heaps is to return the smallest or largest element
# This is because the time complexity of getting the minimum/maximum value from a min/max heap is O(1)
# Heaps are also used to design Priority Queues. 

# PROS AND CONS

    # HEAP ADVANTAGES    

    # HEAP DISADVANTAGES
    
# BIG O ANALYSIS 

    # INSERTION - O(log(n)) - EXPLANATION
    # DELETION - O(log(n)) - EXPLANATION
    # ACCESS - O(log(n)) - EXPLANATION
    # SEARCH - O(log(n)) - EXPLANATION
    
# MAX HEAP IMPLEMENTATION

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) -1)
    
    def getMax(self):
        if self.heap:
            return self.heap[0]
        
        return None
    
    def removeMax(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            
            return max
        else:
            return None
    
    def __percolateUp(self, index):
        parent = (index-1)//2
        
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__percolateUp(self, parent)
    
    def __maxHeapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
            
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
            
        if largest != index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.__maxHeapify(largest)
            
    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self.__maxHeapify(i)

heap = MaxHeap()

# MIN HEAP IMPLEMENTATION

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def getMin(self):
        if self.heap:
            return self.heap[0]
        
        return None

    def removeMin(self):
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__minHeapify(0)
            return min
        
        elif len(self.heap) == 1:
            min = self.heap[0]
            del self.heap[0]
            
            return min
        else:
            return None

    def __percolateUp(self, index):
        parent = (index-1)//2
        
        if index <= 0:
            return
        
        elif self.heap[parent] > self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__percolateUp(parent)

    def __minHeapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            tmp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = tmp
            self.__minHeapify(smallest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self.__minHeapify(i)


heap = MinHeap()