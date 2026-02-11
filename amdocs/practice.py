

def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = merge(arr[:mid])
    right = merge(arr[mid:])

    i = j = 0
    merge_arr = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge_arr.append(left[i])
            i += 1
        else:
            merge_arr.append(right[j])
            j += 1

    merge_arr.extend(left[i:])
    merge_arr.extend(right[j:])
    return merge_arr

# print(merge([6,2,9,1,10,44,3]))

class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def traverse(head):
    temp = head
    while temp:
        print(temp, end='')
        if temp.next:
            print('->', end='')
    print()

def reverse(head):
    temp = head
    prev = None
    while temp:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    return next

head = LinkedNode(1)
a = LinkedNode(2)
b = LinkedNode(3)
c = LinkedNode(4)
head.next = a
a.next = b
b.next = c

traverse(head)
# rev = reverse(head)
# print(rev)






