# ----------------------- IN-PLACE REVERSAL OF LINKED LIST - LINKED LIST - O(n) -----------------
    # The in-place manipulation of a linked list pattern allows us to modify a linked list without using any additional memory
    # In-place refers to an algorithm that processes or modifies a data structure using only the existing memory space
    # This pattern is best suited for problems where we need to modify the structure of the linked list, without manipulating data i.e., the order in which nodes are linked together
    # We iterate over the linked list while keeping track of three nodes: the current node, the next node, and the previous node


# TEMPLATE 
# template to reverse a linked list iteratively 
def in_place_reversal_iterative(head):
    
    # initialize 3 pointers (prev node, next, and current nodes)
    prev, next, curr = None, None, head
        
    while curr is not None: # traverse through until we hit the end of linked list
        next = curr.next # first store next as the next node in list
        curr.next = prev # reverse the current nodes pointer to point to the previous node (performs single reversal at each iteration)
            
        prev = curr # move the prev node to be the curr node in iteration
        curr = next # move the current node to the new next node (we just set next in first line of loop)
        
    return prev # prev is now sitting at head so we return prev
            
        
        
# template to reverse a linked list iteratively 
def in_place_reversal_recursive(head):
    
    
   # set base case (condition in which function does no work and returns base elem/item passed in)
    if head == None or head.next == None: # if head is none we have no work to do OR head has an item but head.next is none we have one item in our list which counts as a reversed list just return head
        return head

    reversedHead = in_place_reversal_recursive(head.next) # this will happen at each node - reverse the rest of list not including me until we are at end of nodes
    head.next.next = head # once we are at the end of nodes set next nodes next to head (current node)
    head.next = None # set next value to None
    
    return reversedHead

# -> 1 -> 1 -> 3 ->
        

# EXAMPLE QUESTIONS

# NAIVE APPROACH
# The naive approach to reverse a linked list is to traverse it and produce a new linked list with every link reversed

# TRICKS

# ---------------------- CHALLENGES/SOLUTIONS (LINKED LIST) -----------------------

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


# ------------ Reverse Linked List (Easy)
def reverse(head):

    prev, next = None, None # initialize prev and next pointer to None
    curr = head # set current pointer to the head node
   
    while curr is not None:  # while the current pointer is not None
        next = curr.next # temporarily store the next node
        curr.next = prev # reverse the current node
        prev = curr # before we move to the next node, point previous to the current node
        curr = next  # move to the next node 
    head = prev
    
    # return the new head pointer
    return head



# ------------ Reverse Nodes in K-Group (HARD)

def reverse_k_groups(head, k):
    
    dummy = Node(0)
    dummy.next = head
    
    ptr = dummy
    
    
    while ptr:
        tracker = ptr
        
        for _ in range(k):
            if tracker == None:
                break
            
            tracker = tracker.next
            
        if tracker == None:
            break
        
        previous, current, next = None, ptr.next, None
        
        # reverse k group
        for _ in range(k):
            next = current.next # temporarily store the next node
            current.next = previous # reverse the current node
            previous = current # before we move to the next node, point previous to the # current node
            current = next  # move to the next node 
            
        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group
        
    return dummy.next

# ------------ Reverse Linked List II (MEDIUM)
'''
Given a singly linked list with nodes and two positions, left and right, 
the objective is to reverse the nodes of the list from left to right. 
Return the modified list.
'''
def reverseBetween(head, left, right):
  dummy = Node(0, head)
  
  # reach node at position left (start of nodes to be reversed)
  left_prev, curr = dummy, head 
  for _ in range(left - 1):
    left_prev, curr = curr, curr.next
  
  # curr = left, left_prev=node before left     
  prev = None
   
  for _ in range(right - left + 1):
    next = curr.next # temporarily store the next node
    curr.next = prev # reverse the current node
    prev, curr = curr, next # point previous to the current node & move to the next node
  
  # Update pointers outside of reversed nodes
  left_prev.next.next = curr # curr is node after right node
  left_prev.next = prev # prev is right
   
  return dummy.next # return new head if re assigned 

# ------------ Reorder List (MEDIUM)

'''
Given the head of a singly linked list, reorder the list as if it were folded on itself. For example, if the list is represented as follows:
You dont need to modify the values in the lists nodes; only the links between nodes need to be changed.
'''


def reorder_list(head):

    dummy = Node(0, head)
    ptr = head #storing head node for reference later

    # (1) get middle node (using fast and slow pointers)
    slow, fast = head, head

    while fast and fast.next:
        # slow_prev = slow # track prev middle node
        slow = slow.next # will land on middle node
        fast = fast.next.next

    prev, curr = None, slow

    # (2) reverse second half of list
    while curr is not None:
        next = curr.next # temporarily store the next node
        curr.next = prev # reverse the current node
        prev = curr # before we move to the next node, point previous to the current node
        curr = next  # move to the next node 

    # (3) merge list
    while prev.next: # stop once we reach the slow node (middle node)
        next_prev = prev.next # temporary store next up of second half of list
        next_ptr = ptr.next # temporary store next up of first half of list (starting from head node)

    # swap pointers at each iteration
        ptr.next = prev # set curr node from first half of list to curr prev node (end of second half of list)
        prev.next = next_ptr # set curr prev node pointer to the node next up in first half of list
        prev = next_prev # move prev node along the the second half of list (reversed list)
        ptr = next_ptr # move ptr node along the first half of list (non reversed)

     
    return dummy.next

# ------------ Swap Nodes (MEDIUM)

'''
Given the linked list and an integer, k, 
return the head of the linked list after swapping the values of the kth node from the beginning 
and the kth node from the end of the linked list.
'''

def swap_nodes(head, k):

    curr = head # initialize a current node at head of linked list
    count = 1 # initialize count to track place in linked list and compare with k
        
    while count < k: #traverse list until count == k
        curr = curr.next # move forward curr node
        count += 1 # increment count

    front, end = curr, head # store kth node of front list as current node, initialize var end at head of list
    
    while curr.next: # continue traversing list until curr, starting at kth front node, next node is Null
        curr = curr.next # move curr node forward
        end = end.next # move end node forward (when we reach end of list this will be the kth node at end of list)

 # swap nodes
    front_kth_node = front.data # store temp var for front kth node val
    front.data = end.data # swap front kth node val with end kth node val
    end.data = front_kth_node # swa end kth node val with front kth node val
    
    return head

# single while loop
def swap_nodes_2(head, k):
    
    count = 0
    
    front, end, curr = None, None, head

    while curr:
        count += 1
        
        if end is not None:
            end = end.next

        if count == k:
            front = curr
            end = head
        curr = curr.next
        
    front.data, end.data = end.data, front.data # swap front kth node val with end kth node val w. one line

    # swap nodes by storing front kth node before swap multi line
    front_kth_node = front.data # store temp var for front kth node val
    front.data = end.data # swap front kth node val with end kth node val
    end.data = front_kth_node # swa end kth node val with front kth node val
    
# ------------ Reverse Nodes In Even Length Groups (MEDIUM)

''''
Given the head of a linked list, the nodes in it are assigned to each group in a sequential manner. 
The length of these groups follows the sequence of natural numbers. 
Natural numbers are positive whole numbers denoted by 

In other words:

The 1st node is assigned to the first group.

The 2nd and 3rd nodes are assigned to the second group.

The 4th, 5th, and 6th nodes are assigned to the third group, and so on.

Your task is to reverse the nodes in each group with an even number of nodes and return the head of the modified linked list.

'''

def reverseEvenLengthGroups(head):
    
    l = 2 # initialize var to track group length (set at 2 since head will always be odd group length of 1)
    ptr = head #intialize start node at head
        
    while ptr.next:
        
        t = ptr # intialize tracker pointer as pointer (traverses through node without updating curr place in list)
        n = 0 # initialize var to track remaining number of nodes in list after each groupe reversal
        
        for _ in range(l): # traverse through list in range of group length
            if t.next is None: # if at end of list break and move to next block
                break
            
            n += 1 # increment remaining nodes
            t = t.next # move through list
        
        if n % 2: # if remaining nodes is odd update curr node through the list, passing the curr group length
            ptr = t
        else:    # if remaining nodes is even reverse the remaining nodes
            prev, curr, next = None, ptr.next, None

            for _ in range(n):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            last_node_of_reversed_group = ptr.next
            last_node_of_reversed_group.next = curr
            ptr.next = prev

            ptr = last_node_of_reversed_group
            
        l += 1
        
    return head

# ---------------- Swap Nodes in Pairs (MEDIUM)

'''
Given a singly linked list, swap every two adjacent nodes of the linked list. 
After the swap, return the head of the linked list.
'''

def swap_pairs(head):
    dummy = Node(0, head) # initialize var as dummy node
    pair = 2 # initialize var pair, represents num of reversals 
    ptr = dummy # initialize var at start of linked list

    while ptr and ptr.next:
        t = ptr # initialize var to track num of nodes left in linked list 

        for _ in range(pair): # iterate in range of pair to ensure there are atleast 2 nodes left before reversing
            if t == None: # if t == null we are at end of list
                break

            t = t.next # move forward through list

        if t == None:
            break
        
        prev, curr, next = None, ptr.next, None

        for _ in range(pair):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = curr
        ptr.next = prev

        ptr = last_node_of_reversed_group
    

    return dummy.next


def swapPairs(head):
    dummy = Node(0, head)
    prev, curr = dummy, head
    
    while curr and curr.next:
        
        # save ptrs
        nxtPair = curr.next.next
        second = curr.next
        
        
        # reversal
        second.next = curr # reverse ptr of second node in pair to first node in pair
        curr.next = nxtPair # move first node in pair pointer to next pairs first node
        prev.next = second # 
        
        # update ptrs
        prev = curr
        curr = nxtPair
        
    return dummy.next