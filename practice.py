from enum import nonmember

print('==========quick short=============')
def partition(arr, low, high):
    pivote = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickshort(arr, low=0, high=None):
    if high is None:
        high = len(arr) -1
    if low <= high:
        pivote_index = partition(arr, low, high)
        quickshort(arr, low, pivote_index - 1)
        quickshort(arr, pivote_index+1, high)

nums = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]
quickshort(nums)
print(nums)
print('==========2 sum============')

arr = [1,2,5,7,9]
target = 12

def func(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        val = arr[low] + arr[high]
        if val == target:
            return arr[low], arr[high]
        elif val < target:
            low += 1
        else:
            high -= 1
    print()
print(func(arr, target))

print('======for unsorted arry==========')

def fun2(arr, target):
    set = {}
    for item, val in enumerate(arr):
        num = target - val
        if num in set:
            return [num, val]
        set[val] = item
print(fun2(arr, target))
b = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0,4,2,6,7,8,]

def remove_dup(arr):
    if not arr:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1

# a = remove_dup(arr)
#
# print(b[:a])
print('=======majority element=======')
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

print(b)
print(majority_element([2,2,1,1,1,2,2,4,5,6,7,8,8,8,8,8,8]))
print('======single linkedlist===========')

class Linkedlist:
    def __init__(self, head, next=None):
        self.head = head
        self.next = next
    def __str__(self):
        return str(self.head)

head = Linkedlist(1)
a = Linkedlist(2)
b = Linkedlist(3)
c = Linkedlist(4)

head.next = a
a.next = b
b.next = c

print(head)


def traverse(head):
    curr = head
    while curr:
        print(curr.head, end='')
        if curr.next:
            print('->', end='')
        curr = curr.next
    print()
print('=====traverse signgle linked node=========')
traverse(head)
print('=====reverse ll=============')

def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev
rr = reverse(head)
print(traverse(rr))
print('======double linked list=========')

class DoubleLinkedList:
    def __init__(self, head, next=None, prev=None):
        self.head = head
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.head)

head  = tail = DoubleLinkedList(1)

def display(head):
    curr = head
    while curr:
        print(curr.head, end='')
        if curr.next:
            print('<->', end='')
        curr = curr.next

    print()
display(head)

print('=====double ll insert at beginning=========')

def insert_at_begin(head, tail, val):
    new_node = DoubleLinkedList(val, next=head)
    head.next = new_node
    return new_node, tail
head, tail = insert_at_begin(head, tail, 2)
# display(head)

def reverse_str(text):
    s = list(text)
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

print(reverse_str('ashutosh pradhan'))

print('=======set 0 to end of the list=========')

def set_zero_to_end(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
arr = [0,3,4,0,2,0,5,0]
print(set_zero_to_end(arr))
print(arr)
print('============fibonancy number==========')
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0,1
    for _ in range(2, n+1):
        a,b = b , a+b
    return b

print(fib(10))
print('===decorator=====')

def log_dec(func):
    def wrapper(*args, **kwargs):
        print('function called:', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_dec
def say_hlo():
    print('hello...')

say_hlo()

print('============two sum===========')

def two_su(arr, target):
    stack = {}
    for i, val in enumerate(arr):
        diff = target - val
        if diff in stack:
            return [diff, val]
        stack[val] = i
    return []

print(two_su([2,3,5,7], 9))







