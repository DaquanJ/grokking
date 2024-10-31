# ----------------------- SLIDING WINDOW - ARRAY / STRINGS - O(n) -----------------
    # The sliding window pattern is used to process sequential data by maintaining a moving subset of elements, called a window.
    # A window is a sublist formed over a part of an iterable data structure.
    # The sliding window pattern allows us to process the data in segments instead of the entire list.
    # It may be viewed as a variation of the two pointers pattern, with the pointers being used to set the window bounds.
    # 


# TEMPLATE(S)
# template to find min or max number of items within any sized window (not a fixed window length) ---->
def sliding_window_find_min_max(input, k):
    
    res = 0 # track result
    
    l = 0 # start window with left pointer at index 0 (l will represent start position in window)
    
    # r pointer is set with loop to look at every item in string
    for r in range(len(input)): # r will represent end position in window
        
        while (r - l + 1) > k: # if the current window size have exceeded the limit, slide the window (window is not valid)
            l += 1 # increment left pointer (removes left most item from window and sets it as next left)
        

    return res

# template to find min or max of elems within a
# with a fixed size window ---->
def sliding_window_subset(input, windowSize): 
    
    res = input[:windowSize] # initialize res as window based on set window size using slice method

    for i in range(len(input) - windowSize): # iterate through k length of elems in bounds of input length
        
        #slide window to update res with min or max of elems within set window
        res -= input[i] # remove left most item from window
        res += input[i+windowSize] # add next item in input to window
        
        
    return res  
                                                

# EXAMPLE QUESTIONS

# NAIVE APPROACH

# TRICKS
# Focus on ensuring you have a full understanding of the problem statement i.e if a question asks you to find the palindrome
# understand what a palindrome is thoroughly before coding
# To find MIN or MAX always increment window one item at a time and remove left most from window if size of window is more than k (not starting with set size window using k etc.) 


# ---------------------- CHALLENGES/SOLUTIONS (ARRAY / STRINGS) -----------------------

# ------------ Repeated DNA Sequences
"""
Given a string, s, that represents a DNA subsequence, and a number, 
return all the contiguous subsequences (substrings) of length that occur more than once in the string. 
The order of the returned subsequences does not matter. 
If no repeated substring is found, the function should return an empty set.
"""

def find_repeated_sequences(s, k):
    seen, res = set(), set() # initialize sets to track seen chars and res of substr

    l = 0 #initialize start of window
    r = k #initialize end of window

    while r <= len(s): # iterate over string where r reps end of window
        cur = s[l:r] # set current window with each iteration (end of window moves one forward)
        if cur in seen: #if curr window in set add curr window to res (it repeats)
            res.add(cur)

        seen.add(cur) # add curr window to seen (window not valid)
        #slide window forward
        l += 1 #increment start of window
        r += 1 #increment end of window

    return res

# ------------ find max in sliding window (hard)
 # Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.

from collections import deque

def find_max_sliding_window(nums, w):
    output = [] # initialize output array
    q = deque() # initialize queue
    l = r = 0 #initialize pointers at 0 index

    while r < len(nums): # we increment right pointer until we reach end of input array
        # if last item pushed to queue is less than current num, remove and append index of current num
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # left index is greater then left most index in q remove left most index
        if l > q[0]:
            q.popleft()

        # out of bounds check (if next elem after cur right is > window)
        if (r + 1) >= w: #while window is not valid
            output.append(nums[q[0]]) # append actual num value which is max
            l += 1 # increment left if within window
        r += 1 # increment right

    return output

# ------------ find min window substring (hard)
# Given two strings, s and t, find the minimum window substring in s, which has the following properties:

# It is the shortest substring of s that includes all of the characters present in t.
# It must contain at least the same frequency of each character as in t.
# The order of the characters does not matter here.

def find_min_window_substr(s, t):
    if t == "": return ""
    
    countt, window = {},{}
    
    for c in t:
        countt[c] = 1 + countt.get(c, 0)
        
    have, need = 0, len(countt)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        
        if c in countt and window[c] == countt[c]:
            have += 1
            
        while have == need:
            # update our result 
            if (r - l + 1) < resLen:
                res = [l,r]
                resLen = (r - 1 + 1)
            # pop from left of window
            window[s[l]] -= 1
            
            if s[l] in countt and window[s[l]] < countt[s[l]]:
                have -= 1
            l += 1
            
    l, r = res
    return s[l:r+1] if resLen != float("infinity") else ""

# ------------ Longest Repeating Character Replacement (hard)

# Given a string s and an integer k, find the length of the longest substring in s, 
# where all characters are identical, after replacing, at most, k characters with any other lowercase English character.

def longest_repeating_character_replacement(s, k):
    count = {} # store occurances of each char
    res = 0 # track longest substring
    maxf = 0 # track most frequent char
    
    l = 0 # start window with left pointer at index 0
    
    # r pointer is set with loop to look at every item in string
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0) # for char at curr position increment count in hashmap i.e {a: 2, b: 1}
        maxf = max(maxf, count[s[r]]) # update most frequent char
        
        while (r - l + 1) - maxf > k:  # if the number of replacements in the current window have exceeded the limit, slide the window (window is not valid)
            count[s[l]] -= 1 # decrement count of char in count hashmap
            l += 1 # increment left pointer (removes left most item from window and sets it as next left)
        
        res = max(res, r - l + 1) # set res to highest number between size of curr window or itself
    return res


# ------------ Longest Substring without Repeating Characters (medium)

# Given a string, input_str, return the length of the longest substring without repeating characters.

def find_longest_substring(input_str):
   char_idx = {} # initialize hashmap to track char_idx
   res = 0 # initialize var to track longest sub without rpting chars

   l = 0 # initialize start of window

   for r in range(len(input_str)): # traverse string char by char

   # if curr char not in char idx dict add it and set curr idx as value
      if input_str[r] not in char_idx:
         char_idx[input_str[r]] = r

      elif char_idx[input_str[r]] >= l:  # checks if repeating char is found and within window (window is not valid)
         curr_window = r - l # calculate curr window size

         res = max(res, curr_window) # update res if curr window is larger than prev
         l = char_idx[input_str[r]] + 1 #increment start of window passed og char

      char_idx[input_str[r]] = r #update hashmap with dup char idx
      
   r += 1
   res = max(res, r - l) # update longest sub without rpting chars if curr window is longer than prev
         
   return res

def findLongestSubstr(input_str):
    charSet = set() # initialize empty set (set instead of hashmap because set does not allow dups)
    res = 0 # initialize var to track longest subset as result
    l = 0 # initialize var to set start of window
    
    for r in range(len(input_str)): # traverse string char by char (r represents end of window)
        while input_str[r] in charSet: # check curr char in set (window is not valid)
            charSet.remove(input_str[l]) # if curr char is in set we have duplicate, remove set char
            l += 1 # we have duplicate so we increment our start of window
            
        charSet.add(input_str[r]) # add curr char to set if not alrdy present
        res = max(res, r - l + 1) # update res to curr window if longer than prev
        
    return res # return longest sub string

# ------------ Minimum Size Subarray Sum (medium)
"""
Given an array of positive integers, nums, and a positive integer, target, 
find the minimum length of a contiguous subarray whose sum is greater than or equal to the target. 
If no such subarray is found, return 0.
"""
def min_sub_array_len(target, nums):

    min_sub_array = float("infinity") # initialize var to track min sub array
    l, total = 0 # # initialize start of window, initialize var to track total sum

    for r in range(len(nums)): # iterate through each num (r represent end of window)
        
        total += nums[r] # add next elem to total at each num/iteration

        while total >= target: # hold if current sum is greater than target (window not valid)
            
            curr_window = r - l + 1 # calculate curr window size
            min_sub_array = min(min_sub_array, curr_window) # if curr window is smaller than prev window update min_sub
        
            total -= nums[l] # subtract leftmost num from window
            l += 1 # slide window to right
            
    # return min_sub if updated otherwise return 0
    return min_sub_array if min_sub_array != float("infinity") else 0 

# ------------ Best time to buy and sell stock (easy)

"""
Given an array where the element at the index i represents the price of a stock on day i, 
find the maximum profit that you can gain by buying the stock once and then selling it.
"""

def max_profit(prices):

    #initialize pointers
    buy, sell = 0,1 #buy reps start of window, sell reps end of window

    maxP = 0 # initialize var to track max profit

    while sell < len(prices):

        if prices[buy] < prices[sell]:
            curr_profit = prices[sell] - prices[buy] # calc curr profit by subtracting start of window to end elem in window
            maxP = max(maxP, curr_profit) # update profit with greater of curr_profit and prev
        else:
            buy = sell
        
        sell += 1

    return maxP