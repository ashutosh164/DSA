import cProfile
import ctypes


def func():
    results = []
    for i in range(1, 10000):
        for j in range(1, 10000):
            if i % j == 0:
                results.append((i, j))
    return results


# cProfile.run('func()')

# Optimize code


def opt_func():
    result = [(i, j) for i in range(1, 6) for j in range(1, int(i ** 0.5) + 1) if i % j == 0]
    return result


# cProfile.run('opt_func()')

import asyncio


async def greet():
    await asyncio.sleep(1)
    print("Hello, Async!")


# asyncio.run(greet())


import asyncio


async def task_one():
    for i in range(5):
        print(f"Task One: {i}")
        await asyncio.sleep(1)  # Simulates I/O operation (non-blocking)


async def task_two():
    for i in range(5):
        print(f"Task Two: {i}")
        await asyncio.sleep(1)  # Simulates I/O operation (non-blocking)


async def main():
    await asyncio.gather(task_one(), task_two())  # Runs both tasks concurrently


# asyncio.run(main())


from multiprocessing import Process
import time


def task_one():
    for i in range(5):
        print(f"Task One: {i}")
        time.sleep(1)


def task_two():
    for i in range(5):
        print(f"Task Two: {i}")
        time.sleep(1)


# if __name__ == "__main__":
#     process1 = Process(target=task_one)
#     process2 = Process(target=task_two)
#
#     process1.start()
#     process2.start()
#
#     process1.join()
#     process2.join()


def second_largest(arr):
    if len(arr) < 2:
        return None
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second, largest = largest, num
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None


def second_largest2(arr):
    if len(arr) < 2:
        return None
    return sorted(set(arr), reverse=True)[1] if len(set(arr)) > 1 else None


a = [4, 5, 1, 2, 3]
import cProfile


# cProfile.run('second_largest(a)')
# cProfile.run('second_largest2(a)')

# print(second_largest(a))
# print(sorted(a, reverse=True)[1])


class SeconsLargest:
    def __init__(self, arr):
        self.arr = arr

    def num(self, arr):
        if len(arr) < 2:
            return None
        return sorted(self.arr, reverse=True)[1] if len(self.arr) > 1 else None


b = SeconsLargest(a)
# print(b.num(a))

'''
youtube tutorial
DSA by campusx
'''

'''
python array is dynamic array proved
'''

import sys

L = []

for i in range(100):
    # print(i, sys.getsizeof(L))
    L.append(i)

'''create a list '''

'''
1. create list
2. len
3. append
4. print
5. indexing
6. pop
7. clear
8. find
9. insert
10. delete
11. remove
'''


class MeraList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

    def __getitem__(self, item):
        if 0 <= item < self.n:
            return self.A[item]
        else:
            return "Index out of range"

    def append(self, item):
        if self.n == self.size:
            # resize
            self.__resize(self.size * 2)
        # appens
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return "empty list"
        print(self.A[self.n - 1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        self.B = self.__make_array(new_capacity)
        self.size = new_capacity
        #     copy the content of A to B
        for i in range(self.n):
            self.B[i] = self.A[i]
        self.A = self.B

    def __make_array(self, capacity):
        # this code crea a c type array(static array) with size capacity
        return (capacity * ctypes.py_object)()


L = MeraList()


# print(len(L))
# L.append('hello')
# L.append(2)
# print(L)
# L.clear()
# print(L)


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c


class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def __str__(self):
        curr = self.head
        results = ''
        while curr != None:
            results = results + str(curr.data) + '-->'
            curr = curr.next
        return results[:-3]

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'Item not found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return 'empty list'
        self.head = self.head.next
        self.n -= 1

    def pop(self):
        curr = self.head

        if self.head is None:
            return 'empty linkedlist'

        if curr.next is None:
            return self.delete_head()

        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self.n -= 1

    def remove(self, value):
        if self.head == None:
            return 'empty ll'
        if self.head.data == value:
            return self.delete_head()
        curr = self.head
        while curr.next.next is not None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next is None:
            return 'Not found'
        else:
            curr.next = curr.next.next

    def search(self, item):
        curr = self.head
        pos = 0
        while curr is not None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return 'not found'

    def __getitem__(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == item:
                return curr.data
            curr = curr.next
            pos += 1

    def replace_max(self, value):
        temp = self.head
        max = temp
        while temp is not None:
            if temp.data > max.data:
                max = temp
            temp = temp.next
        max.data = value


l = LinkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
# print(l)
# l.insert_after(2, 6)
# print(l)
# l.clear()
# print(l)
# l.pop()
# print(l)
# l.replace_max(16)
# print(l)
# print(l.search(3))

'''
write a python programme to find the maximum value in a linked list and replace
it with a given value , assume that the linked list populated with wholw numvers and there is onlt one max value in the list

'''


class Node1:
    def __init__(self, value):
        self.data = value
        self.next = None
#
#
# class LinkedL:
#     def __init__(self):
#         self.head = None
#         self.n = 0
#
#     def __str__(self):


    # def __len__(self):
    #     return self.n

    # def insert(self, value):
    #     new_node = Node1(value)
    #     new_node.next = self.head
    #     self.head = new_node
    #     self.n += 1
#
#     def replace_max(self, value):
#         pass

# l = LinkedL()
# l.insert(1)
# print((l))
# print(len(l))


class LinkNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


head = LinkNode(1)
a = LinkNode(2)
b = LinkNode(30)
c = LinkNode(4)
head.next = a
a.next = b
b.next = c


def display(head):
    curr = head
    while curr:
        print(curr.val, end='')
        if curr.next:
            print('->', end='')
        curr = curr.next
    print()


display(head)


def max_num(head):
    if not head:
        print(float('-inf'))
    curr = head.next
    max = head.val
    while curr:
        if curr.val > max:
            max = curr.val
        curr = curr.next
    print(max)


max_num(head)

print('============replace_max=============')


def replace_max(head, val):
    if not head:
        print(float('-inf'))
    curr = head
    max_val = curr
    while curr:
        if curr.val > max_val.val:
            max_val = curr
        curr = curr.next
    max_val.val = val


replace_max(head, 80)

display(head)

print('==========sum of odd position==========')


def sum_odd_node(head):
    curr = head
    counter = 0
    result = 0
    while curr:
        if counter % 2 != 0:
            result = result + curr.val
        counter += 1
        curr = curr.next
    print(result)


sum_odd_node(head)

print('==========reverse ll containing int============')


def reverse(head):
    prev_node = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    head = prev_node
    return head


def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


b = reverse_linked_list(head)
print(b)


print('====max number==========')
def max_n(head):
    curr = head.next
    max = head.val
    while curr:
        if curr.val > max:
            max = curr.val
        curr = curr.next
    print(max)


max_n(b)
print('==========string ll ===========')
'''
given a linked list of ch. write a python fun toreturn a new string that is created by appending ala tha cha given in the ll as per the rls given bellow
rule:
1 . replace '*' or '/' by single space
2. inn case of two consecutive occurrences of '*' of '/', replace those two occurrence by a single space and convert the next chara to upper case
'''


class StringNode:
    def __init__(self, head, next=None):
        self.head = head
        self.next = next


#
# class StringLinkedList:
#     def __init__(self):
#         self.head = None
#         self.n = 0
#
#     def insert_head(self, value):
#         new_node = StringNode(value)
#         if self.head == None:
#             self.head = new_node
#             self.n += 1
#             return
#         curr = self.head
#         while curr.next != None:
#             curr = curr.next
#         curr.next = new_node
#         self.n += 1
#
#     def traverse(self):
#         curr = self.head
#         data = ''
#         while curr:
#             data = data + curr.head
#             curr = curr.next
#         return data
#




class StringLinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def append(self, value):
        new_node = StringNode(value)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n += 1

    def traverse(self):
        curr = self.head
        data = ''
        while curr:
            data = data + curr.head
            curr = curr.next
        return data

    def change(self):
        curr = self.head
        while curr is not None:
            if curr.head == '*' or curr.head == '/':
                curr.head = ' '
                if curr.next.head == '*' or curr.next.head == '/':
                    curr.next.next.head = curr.next.next.head.upper()
                    curr.next = curr.next.next
            curr = curr.next


word_list = StringLinkedList()
word_list.append('T')
word_list.append('h')
word_list.append('e')
word_list.append('/')
word_list.append('*')
word_list.append('i')
word_list.append('r')
word_list.append('o')
word_list.append('n')
word_list.append('/')
word_list.append('/')
word_list.append('m')
word_list.append('a')
word_list.append('n')

word_list.change()
print(word_list.traverse())

'''
 Move all zeroes to end of array using python 
'''
print('=============move all zero to end===============')
def move_zero(nums):
    non_zero = [x for x in nums if x != 0]
    zeroes = [0] * (len(nums) - len(non_zero))
    return non_zero + zeroes

arr = [1,0,3,0,4]
print(move_zero(arr))

'''using 2 pointer '''

def push_zero_to_end(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] != 0:
            left += 1
        elif arr[right] == 0:
            right -= 1
        else:
            for i in range(left, right):
                if arr[i] == 0:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            right -= 1

    return arr

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print(push_zero_to_end(arr))
# print(arr)

'''
Sort an array consisting only of 0s, 1s, and 2s without using sort functions give the solution using python
'''
print('===========sort an array=============')

def sort_arr(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

arr = [1,2,0,1,0,2,1]
print(sort_arr(arr))

print('=========even num sorting algo===========')

def even_sort(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
            left += 1
    return arr

arr = [2,3,5,6,7,8]
print(even_sort(arr))

print('========Move all vowels (a, e, i, o, u) to the left and all other characters to the righ===========')

def move_vowels_left(arr):
    vowels = {'a','e','i','o','u'}
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left].lower() in vowels:
            left += 1
        elif arr[right].lower() not in vowels:
            right -= 1

        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

arr = ['b', 'a', 'x', 'e', 'u', 'm', 'i']
print(move_vowels_left(arr))

class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

head = LinkedList(1)
a = LinkedList(2)
b = LinkedList(3)
c = LinkedList(4)
head.next = a
a.next = b
b.next = c

def display(head):
    curr = head
    while curr:
        print(curr, end='')
        if curr.next:
            print('->', end='')
        curr = curr.next
    print()


display(head)


def max_fun(head):
    if not head:
        print(float('-inf'))
    curr = head.next
    max = head.val
    while curr:
        if curr.val > max:
            max = curr.val
        curr = curr.next
    print(max)


# max_fun(head)
print('==========reverse ll===========')

def reverse(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head


reverse_ll = reverse(head)
display(reverse_ll)


print('=============Problem: Remove duplicates in-place from a sorted array.===')

def remove_duplicate(arr):
    if not arr:
        return 0

    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1

nums = [0,0,1,1,1,2,2,3,3,4]
a = remove_duplicate(nums)
print(a)
print(nums[:a])

arr = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]
print('=========quick short============')

nums = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]

# def quick_sort(arr, low, high):
#     if low < high:
#         pivot_index = partition(arr, low, high)
#         quick_sort(arr, low, pivot_index - 1)
#         quick_sort(arr, pivot_index + 1, high)
#
# def partition(arr, low, high):
#     pivot = arr[high]  # choose the last element as pivot
#     i = low - 1         # pointer for the smaller element
#
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]  # swap
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]  # place pivot in correct position
#     return i + 1

# Sort the list
# quick_sort(nums, 0, len(nums) - 1)
# print(nums)


def partition(arr, low , high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


print('before sort=====>>>',nums)
quick_sort(nums)
print('after sort====>>>',nums)

print('==========binary search==========')

def sorted(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1

a = sorted(nums)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(nums[:a])
print(binary_search(nums[:a], 9))


print('========return the number where the some is 12===================')

def return_number(arr, target):
    low = 0
    high = len(arr) - 1
    while low < target:
        val = arr[low] + arr[high]
        if val == target:
            return arr[low], arr[high]
        elif val < target:
            low += 1
        else:
            high -= 1
    print()
print(return_number([2,1,5,7,9],12))

arr = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]

# def partitions(arr, low, high):
#     low = 0
#     i =

print('========two sum==========')
def two_sum(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        new_val = arr[low] + arr[high]
        if new_val == target:
            # print(arr[low], arr[high])
            return arr[low], arr[high]
        elif new_val < target:
            low += 1
        else:
            high -= 1

    print()

print(two_sum([5,1,2,7,9], 12))











