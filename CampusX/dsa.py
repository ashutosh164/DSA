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
print(l)
# l.replace_max(16)
print(l)
# print(l.search(3))

'''
write a python programme to find the maximum value in a linked list and replace
it with a given value , assume that the linked list populated with wholw numvers and there is onlt one max value in the list

'''


# class Node1:
#     def __init__(self, value):
#         self.data = value
#         self.next = None
#
#
# class LinkedL:
#     def __init__(self):
#         self.head = None
#         self.n = 0
#
#     def __str__(self):
#
#
#     def __len__(self):
#         return self.n
#
#     def insert(self, value):
#         new_node = Node1(value)
#         new_node.next = self.head
#         self.head = new_node
#         self.n += 1
#
#     def replace_max(self, value):
#         pass

# l = LinkedL()
# l.insert(1)
# print((l))
# print(len(l))






