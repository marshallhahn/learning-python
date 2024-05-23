# Variables are dynamically typed
n = 0
print("n = " + str(n))

n = "abc"
print("n = " + n)

# Multiple assignments
n, m, z = 0, "abc", False
print(n)
print(m)
print(z)

# Increment
n = n + 1
n += 1
# n++      # bad

# None is null (absense of value)
n = 4
n = None
print(n)

# If statements don't need parenthesis
# or curly braces
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2


# Parenthesis needed for multi-line conditions
# and = &&
# or = ||
n, m = 1, 2
if (n > 2 and n != m) or n == m:
    n += 1

# While loops are similar
n = 0
while n < 5:
    print(n)
    n += 1

# Looping from 1 = 0 to i = 4
for i in range(5):
    print(i)

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)

# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)

# Division is decimal by default
print(5 / 2)

# Double slash rounds down
print(5 // 2)

# CAREFUL: most languages round toward 0 by default
# so negative numbers will round down
print(-3 // 2)

# A workaround for rounding towards zero is to
# use a decimal division and then convert to int.
print(int(-3 / 2))


# Modding is similar to most languages
print(10 % 3)

# Except for negative values
print(-10 % 3)

# To be consistent with other languages modulo
from collections import deque
from math import fmod

print(fmod(-10, 3))

# More math helpers
from math import floor, ceil, sqrt, pow

print(floor(3 / 2))
print(ceil(3 / 2))
print(sqrt(2))
print(pow(2, 3))


# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
from math import pow

print(pow(2, 200))

# But still less than infinity
print(pow(2, 200) < float("inf"))

##################
# Arrays
##################

# Arrays are called lists in python
arr = [1, 2, 3]
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)  # O(n)
print(arr)

arr[0] = 0  # O(1)
arr[3] = 0  # O(1)
print(arr)

# Initialize arr of size with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Careful: -1 is not out of bounds,
# it's the last value
arr = [1, 2, 3]
print(arr[-1])

# Indexing -1 is the second to last value, etc.
print(arr[-2])

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])

# Similar to for-loop ranges, last index is
# non-inclusive
print(arr[0:4])

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# Be careful though – make sure the number of variables
# on the left matches the number from the array or the
# interpreter will throw a "too many values to unpack" error
#
# a, b = [1, 2, 3]

# Loop through Arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)

# With index and value
for idx, value in enumerate(nums):
    print(idx, value)

# Loop through multiple arrays simultaneously
# with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)

# Sorting
# Asc order by default
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

# Reverse the order (desc)
arr.sort(reverse=True)
print(arr)

# Sorting a list of strings
# Alphabetical order by default
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

# Custom sort (by length of each string)
arr.sort(key=lambda x: len(x))
# Lambda = function without a name
# Take every value from the array, call it 'x' and then
# return the length of that value, which is the 'key' used to sort the string
# the string is going to be mapped to its length
# and then sort those strings based on their length
# default is asc order
print(arr)

# List comprehension
arr = [i for i in range(5)]
# This does 'for i in range(5)' and adds it where the
# first 'i' is located for each returned value
print(arr)

arr = [i + i for i in range(5)]
# This does similar to the above, but the index plus 'i' is
# added to the result (for each index, we want 2 times
# that index returned to the result)
print(arr)

# 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)

# This won't work
arr = [[0] * 4] * 4
# Because each of the rows are going to be the same
# It looks like it works, but when one row is modified,
# all of the rows will also be modified.
# This does not create 4 unique rows
arr[0][2] = 5
print(arr)


##################
# Strings
##################

# Strings are similar to arrays
s = "abc"
print(s[0:2])

# But they are immutable
# This does not work
# s[0] = 'A'

# So this creates a new string
s += "def"
print(s)

# NOTE: Any time a string is modified,
# it's considered an O(n) operation

# Valid numeric strings can be converted
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# In rare cases you may need the ASCII value of a char
print(ord("a"))
print(ord("b"))

# Combine a list of strings (with a delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))
print(" :: ".join(strings))

##################
# Queues
#
# They are double ended in python by default
##################
from collections import deque

queue = deque()

# Adding to the right is simple as
# appending (similar to a stack)
queue.append(1)
queue.append(2)
print(queue)

# But while this is similar to a stack, the benefit of a queue
# is that it can pop from the left, and can be done
# in constant time O(1) – unlike a stack.
queue.popleft()
print(queue)

# Append on left side
queue.appendleft(1)
print(queue)

# Pop from right
queue.pop()
print(queue)


##################
# HashSet
#
# Search in constant time - O(1)
# Insert values in constant time - O(1)
#
# Unlike a list, there cannot be any duplicates in a hash set
##################

my_set = set()

my_set.add(1)
my_set.add(2)
print(my_set)

# Get length of hashset
print(len(my_set))

# Search in hash set
print(1 in my_set)
print(2 in my_set)
print(3 in my_set)

# Remove values in hashset
my_set.remove(2)
print(2 in my_set)

# Initialize a set with a list
print(set([1, 2, 3]))

# Set comprehension
# Similar to lists, we can manually initialize
# a set using a loop inside the set
my_set = {i for i in range(5)}
print(my_set)


##################
# HashMap (aka dictionary)
#
# Similar to hash sets, hash maps cannot have
# duplicate keys inside the hash map
##################

my_map = {}
my_map["alice"] = 88
my_map["bob"] = 77
print(my_map)

# Length will display the number of keys
print(len(my_map))

# Modify the value for a key
my_map["alice"] = 80
print(my_map["alice"])

# Search if a key exists
# This is constant time O(1)
print("alice" in my_map)

# Remove by key
my_map.pop("alice")
print("alice" in my_map)

# Initialize manually
my_map = {"alice": 90, "bob": 100}

# Dictionary Comprehension
# Example output: {0: 0, 1: 2, 2: 4}
# Note: This is very powerful and most often
# helpful/used when doing graph problems
my_map = {i: 2 * i for i in range(3)}
print(my_map)

# Looping through maps
my_map = {"charles": 90, "ada": 100}
for key in my_map:
    print(key, my_map[key])

# Another way to do it is to directly iterate through
# the map values if the key(s) are not needed
for val in my_map.values():
    print(val)

# Unpacking
# This is a more concise way to write
# the first loop from above
for key, val in my_map.items():
    print(key, val)


##################
# Tuples
#
# Similar to arrays but tuples are initialized with parenthesis
# instead of square brackets. They are also immutable.
#
# They can be indexed but not modified
##################

tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# This will not work / can't modify
# ❌ tup[0] = 0

# Can be used for keys for hash map/set
# Note: Most often, tuples are used for this purpose
my_map = {(1, 2): 3}
print(my_map[(1, 2)])

my_set = set()
my_set.add((1, 2))
print((1, 2) in my_set)

# Lists can't be keys
# This will not work
# ❌ my_map[[3,4]] = 5


##################
# Heap
#
# Helpful to find min and max of a set of values
##################

import heapq

# under the hood heaps are arrays
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 4)
print(min_heap)

# In python, heaps are min heaps
# Min is always at index 0
print(min_heap[0])


while len(min_heap):
    print(heapq.heappop(min_heap))


# No max heaps by default. Workaround is to use
# min heap and multiply by -1 when push & pop
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -4)

# Max will always be at index 0
# Multiple by -1 to negate the original negative value
print(-1 * max_heap[0])

while len(max_heap):
    print(-1 * heapq.heappop(max_heap))


# Build a heap from initial values
# Linear time
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))


##################
# Functions
##################


def my_func(n, m):
    return n * m


print(my_func(3, 4))


# Nested functions have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c

    return inner()


print(outer("a", "b"))


# For nested functions: Can modify objects but can not reassign values
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # but it will only modify "val" in the helper scope
        # val *= 2
        #
        # this will modify "val" outside the helper scope
        nonlocal val
        val *= 2

    helper()
    print(arr, val)


nums = [1, 2]
val = 3
double(nums, val)


##################
# Classes
##################


class MyClass:
    # Constructor
    def __init__(self, nums):
        # create member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getLength(self):
        return self.size

    # calling a member function from another member function
    def getDoubleLength(self):
        return 2 * self.getLength()
