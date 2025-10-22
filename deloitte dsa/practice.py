def fun(text):
    stack = []
    for i in text:
        stack.append(i)
    rever = ''
    while stack:
        rever += stack.pop()
    return rever

print(fun('deloitte'))


a = 'deloitte india'
s = ''
for i in a:
    s = i+s
print(s)

def isAnagram(a, b):
    if len(a) != len(b):
        return False

    count = {}
    for ch in a:
        count[ch] = count.get(ch, 0) + 1

    for ch in b:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    return len(count) == 0

print(isAnagram('listen', 'silent'))
print(isAnagram('rat', 'cat'))


def isPalandrom(arr):
    l = 0
    r = len(arr) - 1

    while l <= r:
        # if arr[l] == arr[r]:
        #
        #     l += 1
        #     r -= 1
        while l < r and not arr[l].isalnum():
            l += 1
        while l < r and not arr[r].isalnum():
            l -= 1
        if arr[l].lower() != arr[r].lower():
            return False
        l += 1
        r -= 1
    return True

# print('palandrom===>>',isPalandrom("A man, a plan, a canal: Panama"))


def func(arr):
    l = 0
    r = len(arr) - 1

    while l < r:
        while l < r and not arr[l].isalnum():
            l += 1
        while l < r and not arr[r].isalnum():
            r -= 1

        if arr[l].lower() != arr[r].lower():
            return False
        l += 1
        r -= 1
    return True

print('func =====>>>>>>',func('racecar'))

print('=======find duplicate======')

def find_duplicate(arr):
    seen = set()
    duplicate = []
    for num in arr:
        if num in seen:
            duplicate.append(num)
        else:
            seen.add(num)
    return duplicate

print(find_duplicate([4,3,4,5,6,7,7,9,9]))

def two_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [arr[left], arr[right]]
        elif s < target:
            left += 1
        else:
            right -= 1
print(two_sum([2,7,11,15],9))

a = [4,3,4,5,6,7,7,9,9]
b = set(a)
print(b)


print('=====Group Anagrams=========')
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

from collections import defaultdict

def group_anagram(words):
    hasmap = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        hasmap[key].append(word)
    return list(hasmap.values())

print(group_anagram(words))


print('=====second max======')

def second_max(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    return second


print(second_max([3, 1, 4, 1, 5, 9]))

print('=======Longest Palindrome Substring========')

# def longest_palindrome(s):
#     def
























