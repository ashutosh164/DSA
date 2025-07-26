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






