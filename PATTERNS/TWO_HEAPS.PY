# ----------------------- TWO HEAPS - ARRAY - O(Logn) -----------------
    # As the name suggests, this pattern maintains two heaps, which could be either two min heaps, two max heaps, or a min heap and a max heap.
    # This pattern will be used mostly in cases where we want to compare two separate data sets and return the smallest from one and the largest from the other or the smallest from both or largest from both
    # For a heap containing n elements, inserting or removing an element takes O(logn) time, while accessing the element (we always access the min or max of data set) takes O(1) time.
    # The root element will always contain the max for max heap or the min for min heap.
    
    # The two heaps pattern is a preferred technique for various problems to implement computationally efficient solutions.


# TEMPLATE 
from heapq import heappush, heappop

def two_heaps(dataset):
    min_heap, max_heap = [],[] # init min heap and max heap
    
    for x in range(0, len(dataset)): # iterate through data set to build heaps 
        if max_heap and dataset[x] <= -max_heap[0]: # if max heap has length and val in data set is less then or equal to the root of max heap (the largest val in list) push to max_heap (adding - returns positive value as all values in max heap are set negatively)
            heappush(max_heap, -dataset[x]) # setting num as negative values to simulate max-heap behavior
        else:
            # push to min heap if current val is greater then the root of max
            heappush(min_heap, dataset[x]) 
        
        rebalance_heaps(max_heap, min_heap) # at each iteration run to ensure heaps are of approx. same length (one should never be of length 2 or more than the other)
    
    return min_heap[0] or max_heap[0] # returns min value or max value

    
def two_heaps_two_datasets(data1, data2, k):
    
    min_heap = [] # initialize min heap
    max_heap = [] # initialize max heap
    
    for x in range(0, len(data1)): # iterate through first data set
        heappush(min_heap, data1[x]) # build min_heap from data
        
    for z in range(0, len(data2)): # iterate through second data set
        heappush(max_heap, -data2[z]) # build max_heap from data (each data is store as negative from max heap behavior)
    
    rebalance_heaps(max_heap, min_heap) # at each iteration run to ensure heaps are of approx. same length (one should never be of length 2 or more than the other)
            

    return -max_heap[0] or min_heap[0] # returns max value or min value
        
        
# rebalancing heaps ensures heaps have the same or close to the same number of elems
# heaps are considered balanced if 1. Both heaps have the same amount of elems 2. the Max heap has AT MOST 1 more elem than the min heap
def rebalance_heaps(max_heap, min_heap):
    if len(max_heap) > len(min_heap) + 1:
        heappush(min_heap, -heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heappush(max_heap, -heappop(min_heap))

# EXAMPLE QUESTIONS

# NAIVE APPROACH

# TRICKS
# two heaps will not be used if the input data is sorted, if so this pattern won’t apply.
# This is because two heaps will be sorted, from smallest (max heap) to largest (min heap)

# ---------------------- CHALLENGES/SOLUTIONS (ARRAY) -----------------------

# --------------- MAXIMIZE CAPITAL / IPO (HARD)
'''
A busy investor with an initial capital, c, needs an automated investment program. 
They can select k distinct projects from a list of n projects with corresponding capitals requirements and expected profits. 
For a given project i, its capital requirement is capitals[i], and the profit it yields is profits[i].

The goal is to maximize their cumulative capital by selecting a maximum of k distinct projects to invest in, subject to the constraint that the investor’s current capital must be greater than or equal to the capital requirement of all selected projects.
When a selected project from the identified ones is finished, the pure profit from the project, along with the starting capital of that project is returned to the investor. 
This amount will be added to the total capital held by the investor. 
Now, the investor can invest in more projects with the new total capital. It is important to note that each project can only be invested once.

As a basic risk-mitigation measure, the investor wants to limit the number of projects they invest in. For example, if k is 22, 
the program should identify the two projects that maximize the investor’s profits while ensuring that the investor’s capital is sufficient to invest in the projects.

Overall, the program should help the investor to make informed investment decisions by picking a list of a maximum of k distinct projects to maximize the final profit while mitigating the risk.
'''

from heapq import heappush, heappop, heapify

def maximum_capital(c, k, capitals, profits):

    current_capital = c # initialize var to ref current capital
    capitals_min_heap = [] # create min heap to track minimum
    profits_max_heap = [] # create max heap to track maximum 

    for x in range(0, len(capitals)): # iterate through length of capital & push to min heap (including index of capital in list)
        heappush(capitals_min_heap, (capitals[x], x)) # push each item to min heap (heappush will store smallest item at top, builds min heap)

    for _ in range(k): # iterate k (amount of projects selectable) times

        while capitals_min_heap and capitals_min_heap[0][0] <= current_capital: # at each iteration, if min heap has values and the first item is less than the current capital
            c, capital_index = heappop(capitals_min_heap) # intialize var to store reference of removed item in min heap (min heap items are (value, index) -> c, c_index)
            heappush(profits_max_heap, (-profits[capital_index])) # push to max heap only the profits who index match removed item from min heap (adding negative will build heap that acts as max heap)
        
        if not profits_max_heap:
            break

        j = -heappop(profits_max_heap) # initialize var to ref the first item in max heap, this will be max
        current_capital = current_capital + j # add max to current capital k times 

    return current_capital # return current capital

# --------------- FIND MEDIAN FROM A DATA STREAM (HARD) (time O(1) space O(n))
'''
Create a data structure that can store a list of integers that can change in size over time and find the median from this dynamically growing list in constant time, O(1).

Implement a class, MedianOfStream, which should support the following operations:

Constructor(): This initializes the object of this class, which in turn creates the max and the min heap.
Insert Num(num): This adds an integer, num, to the data structure.
Find Median(): This finds the median of all elements seen so far. If there are an even number of elements, return the average of the two middle values.
'''

class MedianOfStream:
  def __init__(self): 
      
    # large list because the min heap keeps the smallest number in the list at the root, 
    # we will ensure the smallest number in this list is larger than the largest number in the max heap list 
    # (ensuring the numbers are sorted so that if the length of both lists is even grabbing the root num from min and max we know this is the median as the median of an even list if the 2 middle numbers of the list sorted divided by 2)
    self.min_heap = [] 
    
    # small list because the max heap keeps the largest number in the list at the root, 
    # we will ensure the largest number in this list is less than the smallest number in the min heap list 
    # (ensuring the numbers are sorted so that if the length of both lists is odd grabbing the root num from max we know this is the median as the median of an odd list is the middle num of the list sorted)
    self.max_heap = [] 

  # This function should take a number and store it - when inserting each num we ensure the largest number in the max heap is smaller then the smallest number in the min heap thus max heap is considered the small list and min heap is considered the large list
  def insert_num(self, num):
    # push to max heap if num is less than middle elem
    if self.max_heap and num <= -self.max_heap[0]:
      heappush(self.max_heap, -num) # setting num as negative values to simulate max-heap behavior
    else:
      # push to min heap if num is greater then middle elem
      heappush(self.min_heap, num) 

    self.rebalance_heaps()

  def rebalance_heaps(self):
    # rebalance heaps if length of max is larger then length of min + 1 or length of min is greater then length of max
    if len(self.max_heap) > len(self.min_heap) + 1: # ensures we only balance if length is of 2 or greater difference
      heappush(self.min_heap, -heappop(self.max_heap))
    elif len(self.min_heap) > len(self.max_heap):
      heappush(self.max_heap, -heappop(self.min_heap))

  # This function should return the median of the stored numbers
  def find_median(self):
      
    median = None # init var to reference median val later
    heap_is_even = False # init var to store if length of lists is even

    two_heaps_len = len(self.min_heap) + len(self.max_heap) # init var storing len of both heaps

    # calcute if the number of elems between both heaps is even or odd
    if two_heaps_len % 2 == 0:
      heap_is_even = True

    # if even find median by getting mean(average) of the root of the two heaps
    if heap_is_even:
      median = (self.min_heap[0] + -self.max_heap[0]) / 2 # mean is list of nums added divided by length of that list num1 + num2 / 2
    # if odd find median by returning the root of the max heap 
    else:
      median = -self.max_heap[0] # max heap will contain middle elem if number of items in both lists is odd

    return median
  
# --------------- SLIDING WINDOW MEDIAN (HARD) (time O(k * m) space O(n))

 # My Solution
def median_sliding_window(nums, k):
  medians = [] # init var to reference median val later
  
  l = 0 # init left pos of window
  r = k # init right pos of window as k
  
  while r <= len(nums):
    
    min_heap = [] 
    max_heap = []
    curr_window = nums[l:r]
    
    for i in range(len(curr_window)):
      # push to max heap if num is less than middle elem
      if max_heap and curr_window[i] <= -max_heap[0]:
        heappush(max_heap, -curr_window[i]) # setting num as negative values to simulate max-heap behavior
      else:
        # push to min heap if num is greater then middle elem
        heappush(min_heap, curr_window[i]) 
      
      # # rebalance heaps if length of max is larger then length of min + 1 or length of min is greater then length of max
      if len(max_heap) > len(min_heap) + 1: # ensures we only balance if length is of 2 or greater difference
        heappush(min_heap, -heappop(max_heap))
      elif len(min_heap) > len(max_heap):
        heappush(max_heap, -heappop(min_heap))
        
    # if even find median by getting mean(average) of the root of the two heaps
    if k % 2 == 0:
      medians.append((min_heap[0] + -max_heap[0]) / 2) # mean is list of nums added divided by length of that list num1 + num2 / 2
    # if odd find median by returning the root of the max heap 
    else:
      medians.append(-max_heap[0])

    # slide window forward    
    l += 1
    r += 1

  return medians


# Common Solution
import collections

def medianSlidingWindow(nums, k):
  
  max_heap = []
  min_heap = []
  heap_dict = collections.defaultdict(int)
  
  res = []
  
  for i in range(k):
    heappush(max_heap, -nums[i])
    heappush(min_heap, -heappop(max_heap))
    
    if len(min_heap) > len(max_heap):
      heappush(max_heap, heappop(min_heap))
    
  if k % 2 == 1:
    median = -max_heap[0]
    res.append(median)
  else:
    median = (-max_heap + min_heap[0]) / 2
    res.append(median)
    
  for i in range(k, len(nums)):
    prev_num = nums[i - k]
    heap_dict[prev_num] += 1
    
    balance = -1 if prev_num <= median else 1
    
    if nums[i] <= median:
      balance += 1
      heappush(max_heap, -nums[i])
    else:
      balance -= 1
      heappush(min_heap, nums[i])
      
    if balance < 0:
      heappush(max_heap, -heappop(min_heap))
    elif balance > 0:
      heappush(min_heap, -heappop(max_heap))
      
    while max_heap and heap_dict[-max_heap[0]] > 0:
      heap_dict[-max_heap[0]] -= 1
      heappop(max_heap)
    
    while min_heap and heap_dict[min_heap[0]] > 0:
      heap_dict[min_heap[0]] -= 1
      heappop(min_heap)
    
    if k % 2 == 1:
      median = -max_heap[0]
      res.append(median)
    else:
      median = (-max_heap + min_heap[0]) / 2
      res.append(median)
      
      
# --------------- MEETING ROOMS III (HARD) (O (n log n))
'''
You have an integer rooms, representing room numbers from 0 to rooms - 1. Additionally, you are given an 2 2D integer array called meetings, 
where each element meetings[i] = [starti,endi] [starti,endi] indicates that a meeting will be held in the half-closed interval [starti,endi) [starti,end i). 
Each starti is unique.

Your task is to determine the room number that hosted the highest number of meetings. 
If there are multiple rooms, return the room with the lowest number.
'''

# this solution uses two min heaps (available and used_rooms)

def most_booked(meetings, rooms):
	count = [0] * rooms # init count: add value 0 to array for x number of rooms
	available = [i for i in range(rooms)] # init available rooms: iterates rooms and adds i as room number
	used_rooms = [] # init used rooms arr: will be used as min heap to track used meeting rooms

	meetings.sort() # sort meetings 
 
	for start_time, end_time in meetings: # iterate over meetings extracting 0 and 1 index value (start,end)
		while used_rooms and used_rooms[0][0] <= start_time: # evaluate if rooms are in use and first used room end time is less than or equal to current meeting start time
    # move next open used room to available rooms
			ending, room = heappop(used_rooms) 
			heappush(available, room) 

		if not available:
			end, room = heappop(used_rooms)
			end_time = end + (end_time - start_time)
			heappush(available, room)

		room = heappop(available)
		heappush(used_rooms, (end_time, room))
		count[room] += 1

	return count.index(max(count))