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





