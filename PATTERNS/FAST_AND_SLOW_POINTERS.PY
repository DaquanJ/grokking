# ----------------------- FAST AND SLOW POINTERS (Floyd’s cycle detection algorithm.) - LINKED LIST / ARRAY / STRING - O(log n) -----------------
    # Similar to the two pointers pattern, the fast and slow pointers pattern uses two pointers to traverse an iterable data structure at different speeds with one moving faster than the other.
    # Generally, the slow pointer moves forward by a factor of one, and the fast pointer moves by a factor of two in each step. 
    # However, the speed can be adjusted according to the problem statement.
    # Unlike the two pointers approach, which is concerned with data values, the fast and slow pointers approach is used to determine data structure traits

# TEMPLATE 

def fast_and_slow_pointers(val):
    
    # initialize fast and slow pointers
    slow = val # initial val
    fast = val + 2 # initialize val 2 steps ahead of slow pointer
    
    while slow != fast: # if slow and fast point at same val a cycle is detected, break loop
        slow += 1 # increment slow pointer by 1
        fast += 2 # increment fast pointer by 2

# EXAMPLE QUESTIONS
    # Find the middle node of a linked list
    # Determine if an integer is a happy number

# NAIVE APPROACH

# TRICKS

# ---------------------- CHALLENGES/SOLUTIONS (LINKED LIST / ARRAY / STRING) -----------------------


# -------- Happy Number

# Write an algorithm to determine if a number n is a happy number.

# We use the following process to check if a given number is a happy number:

# Starting with the given number n, replace the number with the sum of the squares of its digits.
# Repeat the process until:
# The number equals 1, which will depict that the given number n is a happy number. 
# It enters a cycle, which will depict that the given number n is not a happy number.
# Return TRUE if n is a happy number, and FALSE if not.

def is_happy_number(n): # 0(log n)

    def sum_of_squared_digits(number): # Helper function that calculates the sum of squared digits.
        total_sum = 0 # initial total sum
        while number > 0:
            digit = number % 10 # return remainder (second number in given number)
            number = number // 10 # divide given number by 10 (return first number in given number)
            total_sum += digit ** 2 # square num
        return total_sum

    slow = n
    fast = sum_of_squared_digits(n)

    # if input is 1 number is happy return true
    if n == 1:
        return True

    # if pointers are equal we have a cycle, break loop
    while slow != fast:
        # if fast is not equal to 1 we increment pointers until we get 1 or fast pointer equals slow 
        if fast != 1:
            slow = sum_of_squared_digits(slow) # increment slow by 1
            fast = sum_of_squared_digits(sum_of_squared_digits(fast)) # increment fast by 2 (square sum twice)

        # if fast pointer equals 1 we have a happy number
        elif fast == 1:
            return True
    
    # if loop breaks we have a cycle, return false (not a happy number)
    return False

# -------- linked list cycle O(n)
# Check whether or not a linked list contains a cycle. If a cycle exists, return TRUE. Otherwise, return FALSE. 
# The cycle means that at least one node can be reached again by traversing the next pointer.

# NAIVE APPROACH - store visited nodes in hash set
def detect_cycle(head):

   # use set to keep track of all visited nodes, 
   # used to detect cycle if current node is in set 
   visitedNodes = set()

   # initialize slow and fast pointers at head node (start of linked list)
   slow = head
   fast = head

   while fast.next: # If pointer is None, loop breaks (this means we are at end of linked list, no cycle detected)
      # if current node is in set of visited nodes we have a cycle
      if fast in visitedNodes:
         return True

      visitedNodes.add(fast) # add current node to set
      slow = slow.next # increment slow pointer by 1
      fast = fast.next.next # increment fast pointer by 2

   return False

# OPTOMIZED APPROACH

def detect_cycle(head):
    
    if head is None:
        return False

    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# -------- Middle of the linked list O(n)
# Given the head of a singly linked list, return the middle node of the linked list. 
# If the number of nodes in the linked list is even, there will be two middle nodes, so return the second one.

def get_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow