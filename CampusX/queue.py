class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.rear is None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return 'empty'
        else:
            self.front = self.front.next

    def traverse(self):
        temp = self.front
        while temp is not None:
            print(temp.val, end=' ')
            temp = temp.next

    def is_empty(self):
        return self.front is None

    def size(self):
        temp = self.front
        counter = 0
        while temp:
            counter += 1
            temp = temp.next
        return counter

    def front_item(self):
        if self.front is None:
            return 'empty'
        else:
            return self.front.val

    def rear_item(self):
        if self.rear is None:
            return 'empty'
        else:
            return self.rear.val



q = Queue()
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# q.traverse()
print(q.rear_item())



