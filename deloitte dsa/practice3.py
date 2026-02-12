from random import lognormvariate
from selectors import SelectSelector

from numpy.f2py.auxfuncs import l_not

from EXL.interview import freq_count

txt = 'hey,are,you,ok'
out = 'yeh, era, uoy, ko'

new = [i[::-1] for i in txt.split(',')]

print(','.join(new))

txt = 'ashutosh pradhan'
out = 'a2s2h1'

def feq_count(txt):
    data = {}
    for i in txt.replace(' ', ''):
        if i in data:
            data[i] = data.get(i , 0) + 1
        else:
            data[i] = 1
    result = ''
    for j in data.keys():
        result += j + str(data[j])
    return result

print(feq_count(txt))


def first_min_freq(txt):
    data = {}
    for i in txt.replace(' ', ''):
        data[i] = data.get(i, 0) + 1
    print('data===>>',data)
    for ch in txt.replace(' ', ''):
        if data[ch] == 1:
            return ch
    return None

print(first_min_freq('ashutosh pradhan'))

a = [20,4,50,89,12,90]
'''sort the list and find 2nd heighest'''
n = len(a)
'''bubblesort'''
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

'''two sum'''

def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return diff, num
        seen[num] = i
    return None
print(two_sum([2,3,5,7],9))

'''longest substring without repeating character'''

def log_sub(txt):
    left = 0
    longest = 0
    data = set()
    start_index = 0
    for right in range(len(txt)):
        while txt[right] in data:
            data.remove(txt[left])
            left += 1
        data.add(txt[right])
        if (right-left+1)>longest:
            longest = right-left+1
            start_index = left
        longest = max(longest, right-left+1)
    return longest, txt[start_index: start_index+longest]

print(log_sub('abcabcbb'))

'''move 0 into last'''

def move_zero(arr):
    index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    # arr = arr[::-1]
    return arr
a = [0,4,7,0,4,2,0,1,7,0,4]
# print(move_zero(a))
# print(a)

def move_zero_to_fst(arr):
    index = len(arr) - 1
    for i in range(len(arr)-1 , -1, -1):
        if arr[i] != 0:
            arr[index], arr[i] = arr[i], arr[index]
            index -= 1

    return arr

print(move_zero_to_fst(a))
''' remove duplicate '''



'''majority element'''

def majority(arr):
    count = 0
    ele = None

    for i in arr:
        if count == 0:
            ele = i
        count += 1 if i == ele else -1
    if arr.count(ele) > len(arr)//2:
        return ele
    return None
print('majority===>>',majority([1,2,3,2,4]))

'''most freq number'''

def most_freq(arr):
    freq = {}
    max_count = 0
    max_ele = None
    for i in arr:
        freq[i] = freq.get(i, 0)  + 1
        if freq[i] > max_count:
            max_count = freq[i]
            max_ele = i
    return max_ele, max_count

print(most_freq([1,2,3,2,4]))


def fun(arr, target):
    left , right = 0 , len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(fun([0,2,3,1,0,2,6,0,2,0],6))



def isvalid(txt):
    stack = []
    maping = {')':'(','}':'{',']':'['}
    for i in txt:
        if i in maping:
            top = stack.pop() if stack else '#'
            if maping[i] != top:
                return False
        else:
            stack.append(i)
    return not stack

def isPalaendrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
txt = 'hey,are,you,ok'
out = 'yeh, era, uoy, ko'

res = [i[::-1] for i in txt.split(',')]
print(', '.join(res))


arr = [2, 4, 60, 20, 4, 90]

def sencondHeighest(arr):
    first , sec = float('-inf'), float('-inf')

    for i in arr:
        if i > first:
            sec = first
            first = i
        elif i > sec and i != first:
            sec = i
    return sec
print(sencondHeighest(arr))

def isAnagram(a, b):
    if len(a) != len(b):
        return False
    data = {}
    for ch in a:
        data[ch] = data.get(ch, 0 )+1

    for ch in b:
        if ch not in data:
            return False
        data[ch] -= 1
        if data[ch] == 0:
            del data[ch]
    return len(data) == 0
print(isAnagram('listen', 'silent'))
print(isAnagram('rat', 'cat'))

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import defaultdict
def gp_angm(words):
    data = defaultdict(list)
    print(data)
    for i in words:
        key = tuple(sorted(i))
        print(key)
        data[key].append(i)
    return list(data.values())

print(gp_angm(words))

class LinkNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


    def __str__(self):
        return str(self.val)


node = LinkNode(1)
a = LinkNode(2)
b = LinkNode(3)
c = LinkNode(4)

node.next = a
a.next = b
b.next = c

def traverse(head):
    curr = head
    while curr:
        print(curr.val, end='')
        if curr.next:
            print('->', end='')
        curr = curr.next
    print()

traverse(node)

def reverse(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head
data = reverse(node)
traverse(data)

arr = [2, 4, 60, 20, 4, 90]

fst, sec = float('-inf'), float('-inf')
for i in arr:
    if i > fst:
        sec = fst
        fst = i
    elif i > sec and i != fst:
        sec = i
print(sec)

arr = [2, 4, 60, 20, 4, 90]
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr[-2])

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
def gp_anagm(word):
    data = defaultdict(list)
    for i in words:
        key = tuple(sorted(i))
        data[key].append(i)
    return list(data.values())
print(gp_anagm(words))





