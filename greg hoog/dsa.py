# single linkedlist

class SingleNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


head = SingleNode(1)
a = SingleNode(2)
b = SingleNode(3)
c = SingleNode(4)
head.next = a
a.next = b
b.next = c

print(head)


def traverse(head):
    curr = head
    while curr:
        print(curr.val, end='')
        if curr.next:
            print('->', end='')
        curr = curr.next
    print()

traverse(head)

# serach for a value


def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False


print(search(head, 6))

# doubly linked lists


class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


Head = tail = DoublyNode(1)


def display(head):
    curr = head
    while curr:
        print(curr.val, end='')
        if curr.next:
            print('<->', end='')
        curr = curr.next
    print()


# insert at beginning

def innsert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

Head, tail = innsert_at_beginning(Head, tail, 2)


display(Head)
