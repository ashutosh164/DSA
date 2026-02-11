def two_sum(arr, target):
    hasmap = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hasmap:
            return [diff, arr[i]]
        hasmap[num] = i

print(two_sum([2,3,5,7], 9))

def fun(text):
    stack = []
    for i in text:
        stack.append(i)
    rev = ''
    while stack:
        rev += stack.pop()
    return rev

print(fun('deloitte india'))

text = 'deloitte india'
s = ''
for i in text:
    s = i + s
print(s)

'''
    is anagram means letters length are same with same character
    palandrom means character are same from left to right and right to left
'''

def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in s1:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True
print('anagram=====>',is_anagram("listen", "silent"))

def is_palendrome(s):
    s = s.replace(' ', '').lower()
    return s == s[::-1]

def is_pal(s):
    s = s.replace(' ', '').lower()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def majority_element(nums):
    count = 0
    ele = None
    for i in nums:
        if count == 0:
            ele = i
        count += 1 if i == ele else -1
    return ele
print(majority_element([2,2,1,1,1,2,2]))

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    for ch in s2:
        if ch not in s1:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True


nums = [100, 4, 200, 1, 3, 2]
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

print('longest_consecutive=>>>',longest_consecutive(nums))

def count_ele(arr):
    count = {}
    for i in arr:
        count[i] = count.get(i, 0) + 1
    return count

print('count ele===',count_ele([1,2,2,3,1,4,5,4,3,5,6]))

txt = 'Ashutosh pradhan'
data = {}
for ch in txt.replace(' ',''):
    data[ch] = data.get(ch, 0) + 1

a = [ch for ch, count in data.items() if count <= 1]
print(a)

'''. How do you remove special characters from a string?'''

text = "Py@tho#n3!"

result = ''.join(ch for ch in text if ch.isalnum())
print(result)
'''reverse a string'''
txt = 'ashutosh pradhan'
def reverse_str(txt):
    result = ''
    for ch in txt:
        result = ch+result
    return result
print(reverse_str(txt))
'''palandrop'''

def is_palindrom(txt):
    txt = txt.replace(' ','').lower()
    left = 0
    right = len(txt) - 1
    while left < right:
        if txt[left] != txt[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrom('raceCar'))

def check_vowels(txt):
    txt = txt.replace(' ', '').lower()
    vowels = 'aeiou'
    vowels_count = 0
    cons = 0
    for ch in txt:
        if ch in vowels:
            vowels_count += 1
        else:
            cons += 1
    return vowels_count, cons
print(check_vowels('Ashutosh pradhan'))

def non_repeating_ch(txt):
    txt = txt.replace(' ', '')
    data = {}
    for ch in txt:
        data[ch] = data.get(ch, 0) + 1
    ch_data = []
    for ch,count in data.items():
        if count == 1:
            ch_data.append(ch)
    return ch_data

print(non_repeating_ch('Ashutosh pradhan'))

def remove_du(s):
    seen = {}
    res = ''
    for i in s:
        if i not in seen:
            seen[i] =True
            res += i
    return res


print(remove_du('racecar'))


def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
arr = [1,2,3,4,5,2,1,1,2,3,6,6,67,7]

print(majorityElement(arr))


from collections import Counter

from collections import Counter

def majority_element(nums):
    # Phase 1: find candidate
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Phase 2: verify candidate
    if candidate is None:
        return None

    occ = nums.count(candidate)
    return candidate if occ > len(nums) // 2 else None

# Example
arr = [1,2,3,4,5,2,1,1,2,3,6,6,67,7]
print(majority_element(arr))  # None (no majority)

seen = {}
for i in arr:
    seen[i] = seen.get(i, 0) + 1
print(seen)
major = []
data = ''
for i in seen.values():
    if i >= len(arr) // 2:
        major.append(i)
    else:
        data = 'no data'


def fun(arr):
    count = 0
    ele = None
    for i in arr:
        if count == 0:
            ele = i
        count += 1 if i == ele else -1
    return ele
print(fun([1,2,1,2,1]))


def non_rep(txt):
    freq = {}
    for ch in txt:
        freq[ch]  = freq.get(ch, 0) + 1
    for ch in txt:
        if freq[ch] == 1:
            return ch
print(non_rep('Ashutosh pradhan'))


def max_rep(txt):
    freq = {}
    txt = txt.replace(' ', '')
    for i in txt:
        freq[i] = freq.get(i, 0) + 1
    return freq

print('max_rep===>>>',max_rep('Ashutosh pradhan'))

fruits = ['banana','papaya', 'apple', 'cherry']
# fruits = [1,5,4,2,6,3]
for i in range(1, len(fruits)):
    key = fruits[i]
    j = i - 1

    while j >= 0 and fruits[j] > key:
        fruits[j + 1] = fruits[j]
        j -= 1
    fruits[j+1] = key

print(fruits)


funcs = [lambda x: x+i for i in range(3)]
print([f(10) for f in funcs])


