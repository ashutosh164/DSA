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





