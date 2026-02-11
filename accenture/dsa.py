'''
Q. Given two sequences, find the length of the
 longest subsequence present in both of them.
A subsequence is a sequence that can be derived from
 another sequence by deleting some or no elements without
  changing the order of the remaining elements.

'''

x = "ABCBDAB"
y = "BDCAB"

# m, n = len(x), len(y)
# dp = [[0] * (n + 1) for _ in range(m + 1)]
# print(dp)
def lcs_laength(x,y):
    m,n = len(x), len(y)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i -1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
# print(lcs_laength('abcdefgh','xyzdefg'))

'''
Q. Given an integer array, how would you find the
 contiguous subarray with the maximum sum? Please
  explain your approach and write code to solve
   this problem efficiently.

'''

def max_subarray_sum(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum+nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_subarray_sum(nums))

def max_subarray(nums):
    current_sum = max_sum = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    return max_sum, nums[start:end+1]
# print(max_subarray(nums))

def find_min(nums):
    min_ele = nums[0]
    for num in nums:
        if num < min_ele:
            min_ele = num
    return min_ele
# print(find_min(nums))

'''
Q. Implement a function to find the middle element of a
 linked list in a single pass.
'''

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def find_middle(head):
    slow = fast= head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
e = ListNode(6)
f = ListNode(7)
head.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

def traverse(head):
    temp = head
    while temp:
        print(temp, end='')
        if temp.next:
            print('->', end='')
        temp = temp.next
    print()

traverse(head)
# print(find_middle(head))


def mid_point(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
# print(mid_point(head))

def max_ele(nums):
    max_ele = nums[0]
    for i in nums:
        if i > max_ele:
            max_ele  = i
    return max_ele

# print(max_ele([9,3,10,3,2]))

def mid_ele(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast =fast.next.next
    return slow

'''
Q. Write a function that reverses a string.
 The input string is given as an array of characters s.

'''

def reverse_str(s):
    txt = list(s)
    left, right = 0, len(s) - 1
    while left<right:
        txt[left], txt[right] = txt[right], txt[left]
        left += 1
        right -= 1
    return ''.join(txt)

print(reverse_str('ashutosh'))

'''
Q. Write a function to create a dictionary using two
 lists, where one list represents keys and the other 
 represents values.
'''

def create_dict(keys, values):
    if len(keys) != len(values):
        raise ValueError('key and values must have the same length!')
    res = {}
    for i in range(len(keys)):
        res[i] = values[i]
    return res

txt = 'hey,are,you,ok'
out = 'yeh, era, uoy, ko'


rev_txt = [i[::-1] for i in txt.split(',')]
print(', '.join(rev_txt))

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

from collections import defaultdict

def group_anagram(words):
    hasmap = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        hasmap[key].append(word)
    return list(hasmap.values())

print(group_anagram(words))

nums = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]
'''bubble short'''

def sort_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


arr = sort_arr(nums)

max_ele = arr[0]
for i in arr:
    if i > max_ele:
        max_ele = i
print(max_ele)

fruits = ['banana','papaya', 'apple', 'cherry']
for i in range(1, len(fruits)):
    key = fruits[i]
    j = i -1

    while j >= 0 and fruits[j] > key:
        fruits[j+1] = fruits[j]
        j -= 1
    fruits[j+1] = key
print(fruits)
'''
maximum repeating ele
'''

nums = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0,2,5,2]

def fun(arr):
    count = 0
    ele = None
    for i in arr:
        if count == 0:
            ele = i
        count += 1 if i == ele else -1
    return ele
print(fun([1,2,1,2,1, 3, 2,9,3,5,4,2,1]))




