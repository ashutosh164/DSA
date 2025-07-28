from numpy.ma.core import count


class SingleNode:
    def __init__(self, head):
        self.head = head
        self.next = None

    def __str__(self):
        return str(self.head)


head = SingleNode(1)
a = SingleNode(2)
b = SingleNode(3)
c = SingleNode(4)

head.next = a
a.next = b
b.next = c

def traverse(head):
    temp = head
    while temp:
        print(temp, end='')
        if temp.next:
            print('->', end='')
        temp = temp.next
    print()

print('===before delete head=======')
traverse(head)

def remove_head(head):
    if head is None:
        return head
    temp = head
    head = head.next
    del temp
    return head

print('====after delete head=====')

a = remove_head(head)
traverse(a)
print('==========delete the tail==========')


def remove_tail(head):
    if head is None or head.next is None:
        return None
    temp = head
    while temp.next.next:
        temp = temp.next
    del temp.next
    temp.next = None
    return head

traverse(head)
t = remove_tail(head)
traverse(t)

print('==========delete the kth  node==========')


def remove_kth_node(head, k):
    if head is None or k < 1:
        return head
    if k == 1:
        temp = head
        head = head.next
        del temp
        return head
    count = 0
    temp = head
    prev = None
    while temp:
        count += 1
        if count == k:
            prev.next = temp.next
            del temp
            return head
        prev = temp
        temp = temp.next
    return head

traverse(head)
remove_kth_node(head, 2)
traverse(head)
print('==========insert at tail==========')

def insert_at_tail(head, val):
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = SingleNode(4)
    return head

traverse(head)
insert_at_tail(head, 4)
traverse(head)
print('===========inserting at kth element=========')

# def inertat_nth_element(head, val):
#     if head is None:
#         if val == 1:
#             head = SingleNode(val)
#             return head
#         else:
#             return None
#     if val == 1:
#         head = SingleNode(val)
#         return head
#
#     count , temp = 0, head
#     while temp:
#         count += 1
#         if count == val - 1:
#             new = SingleNode(val)
#             new.next = temp.next
#             temp.next = new
#             break
#     return head


def insert_nth_element(head, el, n):
    if head is None:
        if n == 1:
            return SingleNode(el)
        else:
            return None
    if n == 1:
        new_node = SingleNode(el)
        new_node.next = head
        return new_node

    count, temp = 1, head
    while temp and count < n - 1:
        count += 1
        temp = temp.next

    if temp is None:
        return head

    new_node = SingleNode(el)
    new_node.next = temp.next
    temp.next = new_node
    return head


traverse(head)
insert_nth_element(head, 100, 3)
traverse(head)






















