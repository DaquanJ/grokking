# ----------------------- TWO POINTERS (prune & search) - ARRAYS / LINKED LISTS / STRINGS - O(n) -----------------

    # DESCRIPTION
    # The two pointers pattern uses two pointers to iterate over an array or list until the conditions of the problem are satisfied
    # With two pointers we can keep track of two indexes in a single iteration (at each iteration we can look at two items in a data set and compare them)
    # The pointers can be used to iterate the data structure in one or both directions, depending on the problem statement.
    # I.e with each iteration we look at an item at the beginning of the data set and at end creating a subset of elements
    
    # Whenever there’s a requirement to find a set amount of data elements in an array that satisfy a certain condition, the two pointers pattern should be the first strategy to come to mind.


# TEMPLATE
def two_pointers(array):
    
    # initializing two pointers
    left = 0 # (left outer most elem)
    right = len(array) - 1 # (right outermost elem)
    
    # iterates through data structure until middle elements are reached or loop is broken
    while left <= right:
        left = left + 1 # increment outermost left by 1
        right = right - 1 # decrement outermost right by 1
    
# EXAMPLE QUESTIONS
# Reversing an array - travers the array from the beginning and the end and swap the values until we reach the middle
# Pair with given sum in a sorted array - traverse the array from the end to the beginning 
#                                         comparing the last item to first until pair found that satisfies target sum

# NAIVE APPROACH
# The naive approach to solving this problem would be using nested loops, with a time complexity of O(n^2)


# TRICKS


# ---------------------- CHALLENGES/SOLUTIONS (ARRAY/LINKED LIST/STRING) --------------

# ------ sum of three values

'''
Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, 
that is, nums[i] + nums[j] + nums[k] == target. 
Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

Note: A valid triplet consists of elements with distinct indexes. 
This means, for the triplet nums[i], nums[j], and nums[k], i ≠ j, i ≠ k and j ≠ k.
'''
def find_sum_of_three(nums, target):
   # O(n^2)

      #sort array of nums in asc order
      nums.sort()

      #iterate through length of array
      for i in range(len(nums)):
         # initialize two pointers
         low = i + 1
         high = len(nums) - 1

         while low < high: 
             # calculate sum of three values
            numSum = nums[i] + nums[low] + nums[high]
            
            # increase pointers according to calculations
            # if greater than target we can concur the highest value should be decreased
            # if lower than target we can concur the lowest value should be increased
            if numSum == target:
               return True
            
            elif numSum < target:
               low += 1
               
            elif numSum > target:
               high -= 1
      # if loop finishes without satisfying true statement return false
      return False
  
  
# -------- Valid Palindrome

'''
Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.

Note: A palindrome is a word, phrase, or sequence of characters that reads the same backward as forward.
'''

def is_palindrome(s):
   # O(n)
  
  # Initialize two pointers
  left = 0
  right = len(s) - 1
  
  while left <= right:
    # check if left outermost and right outermost are equal, if not we return false and end the loop
    if s[left] != s[right]:
      return False
    else:
      left = left + 1
      right = right - 1
  # if while loop ends and false is not returned we can concur all pointers we equal and we return true for is a palindrome
  return True

# ------ Remove nth Node from End of List

def remove_nth_last_node(head, n): # O(n)
    # initialize two pointers at head (start of linked list)
    left = head
    right = head

   # iterate n and move right pointer n times through linked list
    for i in range(n):
        right = right.next

   # if right pointer reaches end of list when iterating n 
   # remove head (first node in linked list) 
    if right == None:
        return head.next

# traverse linked list and move two pointers once
# until right pointer is null
    while right.next:
        right = right.next
        left = left.next
    # once condition is met (right pointer is at end of list)
    # we link the left node to the node after its next node (this removes the immediate next node from list)
    left.next = left.next.next
    return head
 
# ------ sort colors in an array O(n)
'''
Given an array, colors, which contains a combination of the following three elements:

0 (representing red) 1 (representing white) 2 (representing blue)

Sort the array in place so that the elements of the same color are adjacent, 
with the colors in the order of red, white, and blue. The function should return the same array.
'''

# solution with less checks
def sort_colors(colors):

    # initialize pointers
    white = 0
    red = 0
    blue = len(colors) - 1

    # check values at each index until white pointer exceeds blue pointer
    while white <= blue:
        if colors[white] == 0:
            colors[white], colors[red] = colors[red], colors[white] # swap values at red and white pointers (0,1)
            white += 1
            red += 1
        elif colors[white] == 1:
            white += 1
        else:
            colors[white], colors[blue] = colors[blue], colors[white] #if not 0 or 1 as specified in above checks swap white and blue (1,2)
            blue -= 1



    return colors
 
 
# improved solution with more checks

def sort_colors(colors):
    red, white, blue = 0, 0, len(colors) - 1
    
    while white <= blue:
        if colors[white] == 0:
            if colors[red] != 0:
                colors[red], colors[white] = colors[white], colors[red]
            
            white += 1
            red += 1

        elif colors[white] == 1:
            white += 1

        else:
            if colors[blue] != 2:
                colors[white], colors[blue] = colors[blue], colors[white]

            blue -= 1

    return colors

# ----------- Reverse Words in a String

# Given a sentence, reverse the order of its words without affecting the order of letters within a given word.

'''
 The input string may contain leading or trailing spaces or multiple spaces between words. 
 The returned string, however, should only have a single space separating each word. 
 Do not include any extra spaces.
 
'''
import collections

def reverse_words(sentence):
   string_builder = collections.deque()

   #initialize pointers
   start = -1
   end = 0

   while end < len(sentence):
      if sentence[end] != " ":
         start = end

         while end < len(sentence) and sentence[end] != " ":
            end += 1

         string_builder.appendleft(sentence[start: end])

         end -= 1
      end += 1

   return " ".join(string_builder)

# ------- Valid Palindrome II O(n)

# Write a function that takes a string as input and checks whether it can be a valid palindrome by removing at most one character from it.

def is_palindrome(s):

 # initialize pointers at start char and end char of s
  left = 0
  right = len(s) - 1

  # initialize counter to track chars not the same at each end of string
  misMatch = 0
  
  while left <= right:
    # if mismatch exceeds 1 s can not be palindrome
    if misMatch > 1:
      return False

    # if char at each end match move both along s
    if s[left] == s[right]:
      left += 1
      right -= 1

    # if char at each end are not equal skip right char 
    # and increment mismatch count
    elif s[left] != s[right]:
      right -= 1
      misMatch += 1
    

  return True