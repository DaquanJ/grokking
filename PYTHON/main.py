# Python is a dynamically typed language (variables are dynamically typed)

# ---------------- V A R I A B L E S ---------------------------
n = 0
print('n = ', n) # output: 0

n = 'abc'
print(' n = ', n) # output: abc

#MULTI ASSIGNMENT (assign multiple variables on one line - multiple types are ok in a single line)

n, m = 0.125, "abc", False

#INCREMENT
n = n + 1 # good
n += 1 # good
# n++  bad

#NONE IS NULL (absence of value)

n = 4
n = None

# -------------------- I F  S T A T E M E N T S ------------------------------

# IF STATEMENTS don't need parentheses for conditional or curly braces from statement (indentation is used)
# statement will be indented within condition


n = 1

if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2
 
# Parentheses are needed for MULTI-LINE CONDITIONALS    
# LOGIC AND / OR OPERATORS are words not symbols -> && = and || = or

n, m = 1, 2

if ((n > 2 and 
     n != m) or n == m):
    n += 1
    
    
# -------------------------- L O O P S --------------------------------
    
    
# WHILE LOOPS (no parentheses, indent statement below while loop condition)

n = 0

while n < 5:
    print(n)
    n += 1
    
# FOR LOOPS - looping from i = 0 to i = 4 (i is incremented implicitly, no need to declare incrementation)
# RANGE tells our loop to continue from 0 to number we include in range(), in this example 5 (0 - 4)
for i in range(5):
    print(i)
    
# looping from i = 2 to i = 5 (the number you are looping to is not included - in this case 6 is not included)
for i in range(2, 6):
    print(i)

# Looping from i = 5 to i = 2
# to decrement within a given range include range as first two number (5, 1) 
# and the amount to decrement by as third number (5, 1, -1)
for i in range(5, 1, -1):
    print(i)
    
# ------------- O P E R A T I O N S ---------------------
    
# Division is decimal by default (does not round to 0 by default)

print(5 / 2) # gives 2.5

# Double slash rounds down
print(5 // 2) #rounds down to -2

# A workaround for rounding towards zero is to 
# use decimal division and then convert to int
print(int(3 // 2))

#Modding is similar to most languages
print(10 % 3) # -> remainder 1

#Except for negative values
print(-10 % 3) # -> remainder 2 (different from Java C++ JS)

#To be consistent with other languages
import math

print(math.fmod(-10, 3)) # -> remainder -1

#math helpers
print(math.floor(3 / 2)) #rounds down
print(math.ceil(3 / 2)) #rounds up
print(math.sqrt(3 / 2)) #getting square root
print(math.pow(3 / 2)) #get the power of a number i.e 2 to the power of 3

#Max / Min int
float("inf")
float("-inf")

#Python numbers are infinite so they never flow over
print(math.pow(2, 200)) # -> 1.6069380442589903e+60

#The number above is still less than infinity
print(math.pow(2, 200) < float("inf"))

# ----------------------------------- A R R A Y S (LISTS) --------------------------

# ARRAYS (called lists in python) arrays are dynamic (arrays are declared by putting a list in square brackets)
arr = [1, 2, 3]
print(arr)

# Can be used as a stack
arr.append(4) # pushes to array [1,2,3,4]
arr.append(5) # pushes to array [1,2,3,4,5]
print(arr)

arr.pop() # removes last value [1,2,3,4]
print(arr)

# Being that this is an array and not an actual stack we can insert into middle of array
arr.insert(1, 7) #inserts 7 at the 1 index

arr[0] = 0 #we can read and reassign values at a given index arr[index]

#Initialize arr of size n with default value of 1
n = 5
arr = [1] * n

print(arr)
print(len(arr))

#Careful: -1 is not out of bounds when indexing an array
# It is actually the representation of the last value in an array

arr = [1, 2, 3]
print(arr([-1]))

# Indexing -2 is the second to last value etc.
print(arr([-2]))

#Sublists (aka SLICING)
arr = [1, 2, 3, 4]
print(arr[1:3]) #we take value from index 1 - 3 not including 3 which returns the array with those values [2,3]

#Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4]) # [1, 2, 3, 4]

# Unpacking (we can take individual elems of array and assign to variables - can be helpful if going through a list of pairs)
# ensure the number of variables match number of elems in array
a, b, c = [1, 2, 3]

#Looping through arrays
nums = [1,2,3]

#Using index (len is the same as .length)
for i in range(len(nums)):
    print(nums[i]) # prints individual value
    
# Without index
for n in nums:
    print(n) #prints individual value without providing index

# With index and value
for i, n in enumerate(nums):
    print(i, n) #provides index (i) and number/value (n) via unpacking
    
    
# Loop through multiple arrays simultaneously with unpacking

nums1 = [1,3,5]
nums2 = [2,4,6]
 # zip takes both arrays combines them into an array of pairs and we can unpack those pair of values
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
    

#sorting (.sort sorts in asc order by default)
arr = [5,4,7,3,8]
arr.sort()
print(arr) # output: [3,4,7,5,8]

# reversing
arr.sort(reverse=True)
print(arr) # output: [8,5,7,4,3]

#can sort a list of strings (by default are sorted in alph order)

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

#Custom sort (by length of string) (pass in lambda which is function without a name)
# take each value call it x and return the length of x and that will be the key used to sort
arr.sort(key=lambda x: len(x))
print(arr)

#LIST COMPREHENSTION (advanced way to initialize a list)
# we want to go through every value in range 5 and call the value i and add the value to array we follow below
arr = [i for i in range(5)] # iterate for i in range 5 i is going here, we take i value and it to array [0,1,2,3,4]
print(arr)

#may be want 2x that index to go into array
arr = [i+i for i in range(5)] # for every index we want 2x that index added to result

# 2 - D list
# first sets array of 4 with all 0s then we want that array to be added to outer array 4 times we have inner loop with range 4
arr = [[0] * 4 for i in range(4)] # this will build a 4 x 4 grid of all 0s
print(arr)

# -------------- ACCESSING VALUES ------------

# ARRAYS
# INDEXING - ARR[0] | ARR[1] | ARR[i] | EMPLOYEES = ['ALICE','MARGE'] -> EMPLOYEES[1] -> 'MARGE'

# --------------------------------------------- S T R I N G S --------------------------------------------------

# Strings are similar to arrays (we can declare with double or single quotes)

str = 'abc'
print(str[0:2]) #Slices the same as an array output: ab


# Strings are immutable (can not modify a string - can not reassign character at a given index)
str[0] = "A" #not possible

# We can create a new string to update the string 
str += 'def'
print(str) # output: abcdef

# Valid numeric strings can be converted
print(int("123") + int("123")) # using int on string will convert to num and add as expected output: 246

# Numbers can be converted to strings
print(str(123) + str(123)) # using str on number will convert to string and concat string as expected output: "123123"

# In rare cases you may need the ASCII value of a char
print(ord('a')) # output: 97 (ascii of lowercase a)
print(ord('b')) # output: 98 (ascii of lowercase b)

#Combine a list of strings (with an empty string delimitor)

strings = ["ab", "cd", "ef"]
print("".join(strings)) # using .join on "" will join each string at the next value output: "abcdef"

#Slice a string

string = "abcdef"

#we slice a string by indexing providing a start index a stop index and step (how to retreive chars)
# string[start:stop:step]


#Get every character in reverse order
print(string[::-1])

# Get every other character from 0 to the end
print(string[::2])

# Get every other character from 1 to the end
print(string[1::2])


# -------------------------------------- Q U E U E S -------------------------------------------

# Queues by default are double ended 
# (we can add or remove items from either end of a queue with the following operations)

# Double ended queue

from collections import deque

queue = deque()

# append adds items to the right of a QUEUE (defaults to first item in queue if no items exist)
queue.append(1)
queue.append(2)
print(queue) # output: deque([1,2])

# popleft removes items from the left of a queue 
# using popleft on the above queue will remove the first element 1
queue.popleft()
print(queue) # output: deque([2])

#appendleft inserts an item at the left of a queue
# using appendleft on our queue will add a 1 as the first element
queue.appendleft(1)
print(queue) #output: deque([1,2])

# pop removes an item from the right of our queue
# using pop on our queue will remove the 2 from the queue
queue.pop()
print(queue) #output: deque([1])

# --------------------------------- H A S H  S E T S ---------------------------

# HashSet are useful because we can insert and grab values in constant time
# Unlike a list there can not be any duplicates in a hashSet

mySet = set()

mySet.add(1)
mySet.add(2)

print(mySet) # output: {1, 2}
print(len(mySet)) # we can algo get the length of a hashSet output: 2
print(1 in mySet) # we can search a hashSet without a function using the in operator (here we are searching for 1 in hashset) #output: true
print(2 in mySet) # (here we are searching for 2 in hashset) #output: true
print(3 in mySet) # (here we are searching for 3 in hashset) #output: false

# we can remove items from a hashSet
mySet.remove(2)
print(2 in mySet) #output: false

# To initialize a hashSet with a bunch of values

# list to set
print(set([1, 2, 3])) # output: {1, 2, 3}

# set comprehension (manually initialize with a loop inside a hash set)
mySet = { i for i in range(5) }
print(mySet) # output: { 0, 1, 2, 3, 4}

# ------------------------------- H A S H  M A P S ------------------------------------------------

#HashMap which is known as a dictionary in python (single most common DS used)


myMap = {}

#insert into hashMap (similar to JS)
myMap['alice'] = 88
myMap['bob'] = 77
print(myMap) # output: { 'alice': 88, 'bob': 77 }
print(len(myMap)) # using len on hashMap gives us the length of keys in map output: 2

# We can modify the values link to a key
myMap['alice'] = 80 #here we change the alice from 88 to 80
print(myMap['alice']) # output: 80 *note this format only returns the value linked to key 

print('alice' in myMap) # we can search for a key in a hashMap without a function using the in operator (here we are searching for alice key in hashMap) #output: true

myMap.pop('alice') # using pop we can remove a key wich also removes the value from a map
print('alice' in myMap) # (here we are searching for alice key in hashMap) #output: false

# Initiating hashMaps

# We can initiate using key/value pairs where key is on left of colon and value on right with each key/value pair seperated by comma

myMap = { "alice": 90, "bob": 70 }
print(myMap) # output: { "alice": 90, "bob": 70 }

#Dict comprehension (manually initialize with a loop inside a hash map)
# useful when building graph problems and an adjacency list

myMap = { i: 2 * i for i in range(3) } # here we set the key i linked to the value 2 * i (i.e {1: 2, 2: 4 }) in the range of 3
print(myMap) # output: { 0: 0, 1: 2, 2: 4 }

# Looping through maps
myMap = { "alice": 90, "bob": 70 }

# here we loop through every key in map and we can print each key (key) and every value the current key maps to (myMap[key])
for key in myMap:
    print(key, myMap[key]) # output: alice 90
                           #         bob 70
    
# alternatively we can directly iterate through the list of values if we dont need key
for val in myMap.values():
    print(val)  # output: 90
                #         70 

# we can also use unpacking to iterate directly through items in hashMap (key/value pair is an item) and have access to key and value
# similar to first loop but can be more concise
for key, val in myMap.items():
    print(key, val)  # output: alice 90
                    #         bob 70
                    
# -------------- ACCESSING VALUES ------------

# HASHMAPS
# KEY - OBJ[KEY] | EMPLOYEES = { 'ALICE': 'DEVELOPER' } -> EMPLOYEES['ALICE'] -> 'DEVELOPER'
                    
                    
# ----------------------------------------- T U P L E S ------------------------------------------

# Tuples are like arrays but immutable (tuples are declared by putting a list in parentheses)
# we can index tuples (grab a value at a given index within a tuple) we can not modify
tup = (1, 2, 3)
print(tup) # output: 
print(tup[0]) # output: 
print(tup[-1]) # output: 

# can't modify
tup[0] = 0 # not possible

# Can be used as key for hash map/set

# here we map a pair of values (1,2) to 3 with 1 and 2 being the key and 3 being the value
myMap = { (1,2): 3 }
print(myMap) # output: 

mySet = set()
mySet.add((1,2))
print((1, 2) in mySet) # (here we are searching for tuple pair in hashSet) #output: true

# Lists cant be keys for hashsets or hashmaps
myMap[[3,4]] = 5 # not possible

# ------------------------------------------- H E A P S ---------------------------------------------------------

# Heaps
import heapq

# under the hood they are implemented with arrays
minHeap = [] # to implement heaps we declare minHeap with empty bracket

# here we are inserting values to a heap (pushes values into heap similar to array)
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min value is always at index 0
print(minHeap[0]) # output: 2

# to loop through heap while the length of the heap is non 0 we can pop values from heap
while len(minHeap):
    print(heapq.heappop(minHeap)) # output: 2 
                                  #         3
                                  #         4
                                  
# No max heaps by default the work around is use min heap and multiply by -1 then push and pop
# to implement a maxHeap we declare maxHeap with empty bracket
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0]) # to get max number we multiply value at index 0 by -1 (negates original negative value) output: 4

while len(maxHeap):
    print(-1 * heapq.heappush(maxHeap)) # output: 4
                                        #         3
                                        #         2
                                        
# Build heap from a set of initial values
arr = [2,1,8,4,5] # our initial values we want to use in heap

heapq.heapify(arr) # by calling heapify we can add a set of values to a heap

while arr:
    print(heapq.heappop(arr)) # here we print each value added (shown one by one as they are popped from heap) heaps will pop from smallest to largest by default
                              # output: 1
                              #         2
                              #         4
                              #         5
                              #         8
                              
# -------------------------- L I N K E D  L I S T -------------------------

# -------------- ACCESSING VALUES ------------


# LINKED LISTS
# NODES - 

# -------------------------- T R E E S -------------------------


# -------------------------- G R A P H S -------------------------
                              
# -------------------------- F U N C T I O N S -------------------------

# Functions are declared in python using def keyword followed by function name and params
#The body of function is going to be indented within function

def myFunc(n, m): # like conditionals and loops we use a colon to finish function declaration
    return n * m

print(myFunc(3,2)) # output: 12

# Nested functions have access to outer variables

# outer function has some parameters and a variable declared at its level
def outer(a, b):
    c = 'c'
    
    # inner function has access to outer variables
    def inner():
        return a + b + c
    return inner()

print(outer('a', 'b')) # output: abc

#Can modify objects but not reassign unless using nonlocal keyword

def double(arr, val):
    def helper():
        # Modifying array works but will only modify val in the helper scope
        # val *= 2
        for i, n in enumerate(arr):
            arr[i] *= 2
            
        # this will modify val outside the helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)
    
nums = [1,2]
val = 3

double(nums, val) # when calling function we return array where each index is reassigned with doubled numbers and val is doubled also output: [2,4] 6 


# ------------------------------------------ C L A S S E S ------------------------------------------

# Classes (are concise but can be more limiting than other languages)

# classes are declared with class keyword followed by the class name using capital first letter
class MyClass:
    #Constructor (declared using def keyword followed by __init__ then passing params)
    def __init__(self, nums): # self in python is the same as this keyword in other languages and is passed into every method of a class (self allows us to call methods and variables declared within class)
        
        # Create member variables
        self.nums = nums #creating member value called nums and setting it as the num value passed in as a param to constructor
        self.size = len(nums) # this creates member variable for size of nums by taking length of parameter (nums)
        
        # self key word required as param when creating methods
        def getLength(self):
            return self.size # here we return member variable size by calling self to it
        
        def getDoubleLength(self):
            return 2 * self.getLength() # we can call to member functions / methods within a class using the self keyword (self.methodName())
        
        
        


