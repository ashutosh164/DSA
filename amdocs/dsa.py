'''
Q. Given an array of integers, sort the array in
 ascending order using the Merge Sort algorithm.
'''
arr = [38, 27, 43, 3, 9, 82, 10]
def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j+=1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
print(merge_sort(arr))
'''
Q. Given the head of a singly linked list,
reverse the list, and return the reversed list.
'''
class LinkNode:
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
        temp = temp.next
    print()
head = LinkNode(1)
a = LinkNode(2)
b = LinkNode(3)
c = LinkNode(4)
d = LinkNode(5)
head.next = a
a.next = b
b.next = c
c.next = d
traverse(head)

def reverse(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
# rev = reverse(head)
# traverse(rev)
'''
Q. Given a singly linked list, implement a function
 to find the middle node.
'''
def middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
print(middle(head))

'''
Q. Given an integer, how do you find the next 
smallest palindrome larger than the given number?


A. We mirror the left half to form a palindrome; 
if it’s not greater, we increment the middle and 
mirror again to get the next smallest palindrome.
'''

# def next_palindrome(arr):
def next_palindrome(n):
    s = list(str(n))
    length = len(s)

    # Special case: all 9s (e.g., 9, 99, 999)
    if all(ch == '9' for ch in s):
        return int('1' + '0' * (length - 1) + '1')

    # Mirror left to right
    s_rev = s[:]
    for i in range(length // 2):
        s_rev[-(i + 1)] = s_rev[i]

    if int("".join(s_rev)) > n:
        return int("".join(s_rev))

    # Increment the middle
    carry = 1
    mid = (length - 1) // 2

    while mid >= 0 and carry:
        num = int(s[mid]) + carry
        carry = num // 10
        s[mid] = str(num % 10)
        mid -= 1

    # Mirror again after increment
    for i in range(length // 2):
        s[-(i + 1)] = s[i]

    return int("".join(s))









