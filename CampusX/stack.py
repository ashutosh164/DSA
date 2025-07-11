''''stack data structure'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        if self.isempty():
            return 'stack empty'
        else:
            return self.top.value
    def pop(self):
        if self.isempty():
            return 'stack empty u cant pop'
        else:
            data = self.top.value
            self.top = self.top.next
            return data


    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

s = Stack()
print(s.isempty())
s.push(2)
s.push(3)
s.push(4)
s.push(5)
# print(s.traverse())
print('----------')
print(s.peek())
s.pop()
print(s.peek())
print('========reverse a string=========')

def reverse_string(text):
    s = Stack()
    for i in text:
        s.push(i)
    res = ''
    while(not s.isempty()):
        res += s.pop()
    print(res)


reverse_string('ashutosh')

print('=========text editor==============')


def text_editor(text, pattern):
    u = Stack()
    r = Stack()
    for i in text:
        u.push(i)

    for j in pattern:
        if j == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)
    res = ''
    while not u.isempty():
        res = u.pop() + res
    return res

print(text_editor('ashutosh', 'uurruuu'))
print('======celebrity problem==============')

l = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,1,0],
    [0,0,0,0]
]

# def find_the_celeb(l):
#     s = Stack()
#     for i in range(len(l)):
#         s.push(i)
#     while len(s) >= 2:
#         i = s.pop()
#         j = s.pop()
#         if l[i][j] == 0:
#             # j is not celeb
#             s.push(i)
#         else:
#             # i is not a celeb
#             s.push(j)
#     celeb = s.pop()
#     for i in range(len(l)):
#         if i != celeb:
#             if l[i][celeb] == 0 or l[celeb][i] == 1:
#                 print('no one is celebrity')
#                 return
#     print('the celebrity is ', celeb)


matrix = [
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]

def find_the_celeb(l):
    candidate = 0
    for i in range(1, len(l)):
        if l[candidate][i] == 1:
            candidate = i #candidate can't be celeb
    for i in range(len(l)):
        if i != candidate:
            if l[candidate][i] == 1 or l[i][candidate] == 0:
                print('no one is celebrity')
                return
    print('the celebrity is ', candidate)


find_the_celeb(matrix)


print('=============stack============')


class Stack:
    def __init__(self, size):
        self.size = size
        self.__stack = [None] * self.size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            return 'overflow'
        else:
            self.top += 1
            self.__stack[self.top] = value

    def pop(self):
        if self.top == -1:
            return 'empty'
        else:
            data = self.__stack[self.top]
            self.top -= 1
            print(data)

    def traverse(self):
        for i in range(self.top + 1):
            print(self.__stack[i], end=' ')

s = Stack(3)
# print(s.stack)
s.push(2)
s.push(3)
s.push(4)
# s.pop()
s.pop()
# s.pop()
# print(s.stack)
s.traverse()

print('===========balance paranthesis problem==========')


def is_balance(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for i in s:
        if i in bracket_map.values():
            stack.append(i)
        elif i in bracket_map:
            if not stack or stack.pop() != bracket_map[i]:
                return False
        else:
            return False
    return not stack

print(is_balance('({[))}{)}'))
print('============== array implement in stack===========')


class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def push(self, val):
        if self.top == self.size - 1:
            return 'overflow'
        else:
            self.top += 1
            self.stack[self.top] = val


s = Stack(3)
print(s.stack)
s.push(4)
print(s.stack)

print('===========flatend the list========')

arr = [5, 2, [9, 4, [1, 6, [7], 8], 3], 0]

def flatten_list(arr):
    results = []
    stack = [arr]
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(reversed(curr))
        else:
            results.append(curr)
    return results

print(flatten_list(arr))

'''using generator for Very memory efficient'''

def flatten_generator(arr):
    stack = [arr]
    while stack:
        curr = stack.pop()
        if isinstance(curr, list):
            stack.extend(reversed(curr))
        else:
            yield curr


for item in flatten_generator(arr):
    print(item, end=' ')


print('=======fltten a linkedlist========')


class SingleNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.child = None


head = SingleNode(1)
head.next = SingleNode(2)
head.next.next = SingleNode(3)
head.next.next.child = SingleNode(7)
head.next.next.child.next = SingleNode(8)
head.next.next.child.next.child = SingleNode(12)
head.next.next.child.next.next = SingleNode(9)


def flatten(head):
    if not head:
        return head
    stack = []
    curr = head

    while curr:
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.child = None
        if not curr.next and stack:
            curr.next = stack.pop()
        curr = curr.next
    return head


def traverse(head):
    while head:
        print(head.val, end='->')
        head = head.next

flattened = flatten(head)
print(traverse(flattened))












