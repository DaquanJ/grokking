# ----------------------- BINARY SEARCH/BI-SECTION SEARCH - ARRAY - O (log (n)) -----------------
   # Binary search is an efficient search algorithm for searching a target value in sorted arrays or 
   # sorted lists that support direct addressing (also known as random access) like indexing. 
   # It follows a divide-and-conquer approach, significantly reducing the search space with each iteration. 
   # The algorithm uses three indexes—
   # start, end, and middle—and proceeds as follows: 
   
   # Set the start and end indexes to the first and last elements of the array, respectively.
   # Calculate the position of the middle index by taking the average of the start and end indexes. I.E
   # If start = 0 and end = 7, then middle = (0 + 7/2) = 3 so middle = 3
   # The binary search approach allows us to efficiently Compare a target value with the element at the middle index.
   
'''
BINARY SEARCH APPROACH

Target is equal to or less than middle elem
    If the target value is equal to the middle index we have found the target and the search terminates, 
    if the target value is less than the middle index element we update the END index to middle - 1 recalcuate the middle index and compare the target value with the middle value again
    This is effective in that, given the array is sorted, if the target is less then the middle elem we KNOW the values to the right (from middle to end index) are all greater than the target so we can remove them from the search


Target is equal to or greater than middle elem
    If the target value is equal to the middle index we have found the target and the search terminates, 
    If the target value is greater than the middle index element we update the START index to middle + 1 recalcuate the middle and compare the target value with the middle value again
    This is effective in that, given the array is sorted, if the target is greater then the middle elem we KNOW the values to the left (from start to middle index) are all less than the target so we can remove them from the search

summary - 
    The above steps walks through the binary search approach, which seeks to remove half of any data set based on if the middle elem is greater than or less than the target 
    following each comparison we will update either the start (target is greater then middle elem) or end (target is less than middle elem) indexes to become the middle, recalcuate the middle based on the new index and compare the middle elem with the target until they are equal or the list is exhausted
'''

# TEMPLATE  
    # full template
def binary_search(arr, target):
    
    arr.sort() # if arr is not sorted, sort array - by default python sorts in asc order
     
    # initialize pointers to the start and end of the array
    start, end = 0, len(arr) - 1
    
    # iterate until the pointer intersect/the list is exhausted or the target is met
    while start <= end:
        
        # at each new iteration calc the middle elem
        mid = start + (end - start) // 2 # we add start first and subtract end from start since we know it will always evaluate to greater than start to prevent overflow in some languages (python can rep large ints so no need to worry about overflow)
        middle = (start + end) // 2 # python way since we are not concerned with overflow
        
        # check if target equal to middle elem, terminate search and return the elem
        if arr[mid] == target:
            return mid # here we return the middle index we can also return the middle elem arr[middle]
        elif arr[mid] < target:
            # move start to middle + 1 if middle is less than target as all elems to the left will also be less than target so we search the right half
            start = mid + 1
        else:
            # move end to middle - 1 if middle elem is greater than target as all elems to the right will also be greater than target so we search the left half
            end = mid - 1
            
    # set some return to indicate list was exhausted and target was not found        
    return -1

# EXAMPLE QUESTIONS

# NAIVE APPROACH

# TRICKS
'''
 The Binary Search can be modified to adapt to handle arrays that have been mutated or to solve for multiple requirements
    The modified binary search pattern builds upon the basic binary search algorithm discussed above. 
    It involves adapting the traditional binary search approach by applying certain conditions or transformations, 
    allowing us to solve problems in which input data are modified in a certain way.

    I.E
      We must perform a binary search to satisfy multiple requirements like finding a target range rather than a single target 
      or finding the leftmost or rightmost occurence of a target value 

Python has bisect_left and bisect_right as apart of the std library 
i.e from bisect import bisect_left, bisect_right
'''

# ---------------------- CHALLENGES/SOLUTIONS (ARRAY) -----------------------

# --------------- BINARY SEARCH (EASY) (O (log(n)))

def binary_search(nums, target):
  start, end = 0, len(nums) - 1
  
  while start <= end:
    
    mid = start + (end - start) // 2
    
    if target == nums[mid]:
      return mid # target is found terminate search
    elif target < nums[mid]:
      end = mid - 1 # search the left side of nums
    else:
      start = mid + 1
    # Replace this placeholder return statement with your code
  
  return -1

# --------------- SEARCH IN ROTATED SORTED ARRAY (DIFFICULTY) (BIG 0)




