print('==========single linkedlist===================')

class SingleNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

node = SingleNode(1)
a = SingleNode(2)
b = SingleNode(3)
c = SingleNode(4)

node.next = a
a.next = b
b.next = c

print(node)

print('=======traverse the list===========')
def traverse(node):
    curr = node
    while curr:
        print(curr)
        curr = curr.next


print(traverse(node))

print('=======display the linkedlist===========')

def display(node):
    curr = node
    while curr:
        print(curr.val, end='')
        if curr.next:
            print('->', end='')
        curr = curr.next
    print()

display(node)

print('=====search===========')

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False


print(search(node, 5))

print('======double linkedlist===========')

class DoubleLinkedList:
    def __init__(self, val, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre

    def __str__(self):
        return str(self.val)

head = tail = DoubleLinkedList(1)

print('=========traverse double linkedlist=========')

def traverse(head):
    curr = head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print('<->'.join(element))

traverse(head)

print('=======insert at beginning ===========')

def insert_at_beginning(head, tail, val):
    new_node = DoubleLinkedList(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
traverse(head)


print('=======insert at tail===========')

def insert_at_end(head, tail, val):
    new_node = DoubleLinkedList(val, pre=tail)
    tail.next = new_node
    return head, new_node
head, tail = insert_at_end(head, tail,5)
traverse(head)



print('=========merge two sorted ll==================')

'''
approach

list1, list2

dummy_ll = SingleNode()
curr = dummy_ll

while list1 and list2:
    if list1.val < list2.val:
        curr.next = list1
        curr = list1
        list1 = list1.next
    else:
        curr.next = list2
        curr = list2
        list2 = list2.next
curr.next = list1 if list1 else list2
return dummy_ll.next
    

'''


def merge_two_sort_ll(list1, list2):
    dummy_ll = SingleNode()
    curr = dummy_ll
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            curr = list1
            list1 = list1.next
        else:
            curr.next = list2
            curr = list2
            list2 = list2.next
    curr.next = list1 if list1 else list2
    return dummy_ll.next

print('===== maxSubArray ========')


class Solution:
    def maxSubArray(self, nums):
        cur_sum = 0
        max_sum = float('-inf')
        n = len(nums)
        for i in range(n):
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum =0
        return max_sum



