# '''write a funcitons  to hide the credit card number   '''
#
#
# def mask(number: str)->str:
#     digit = ''.join(filter(str.isdigit, number))
#     if len(digit) < 4:
#         raise ValueError('invalid credit card number')
#
#     return '*' * (len(digit) - 4) + digit[-4:]
#
#
# a = [1,2,3,4]
# b = [3,4,5,6]
# print(list(set(a) & set(b)))
#
# c = (1,2)
# print(type(c))
#
# d = {'a': 3, 'b': 1, 'c': 2}
#
# # print(dict(sorted(d.items(), key=lambda x: x[1])))
#
#
# d = {'a': 30, 'b': 10, 'c': 20, 'd': 5}
#
# items = []
#
# for k in d:
#     items.append((k, d[k]))
# print('items===>>', items)
# n = len(items)
# print(n)
# for i in range(n):
#     for j in range(i +1, n):
#         if items[i][1] > items[j][1]:
#             items[i], items[j] = items[j], items[i]
#
# sorted_dict = {}
#
# for item in items:
#     sorted_dict[item[0]] = item[1]
#
# print(sorted_dict)
#
#
# a = 256
# b = 256
# print(a is b) # True
#
# x = 257
# y = 257
# print(x is y) # False (usually)
#
# def create_multipliers():
#     return [lambda x: i * x for i in range(4)]
#
# for multiplier in create_multipliers():
#     print(multiplier(2), end=" ")
#


# keys = ['a', 'b', 'c']
# d = dict.fromkeys(keys, [])
# print(d)
# d['a'].append(1)
# print(d)
#
# b = [5,6]
#
# a = (1,2,b)
#
# b.append(7)
#
# print(a)
# data = [("Alice", 25),("Charlie", 30), ("Bob", 20), ]
#
# n = len(data)
#
# for i in range(n):
#     for j in range(0, n-i-1):
#         if data[j][1] > data[j+1][1]:
#             data[j], data[j+1] = data[j+1],data[j]
#
# print(data)
# x,y = [1,2]
# print(x,y)
#
# data = (1, 2, [3, 4])
#
# try:
#     data[2] += [5, 6]
# except TypeError:
#     print("An error occurred!")
#
# print(data)
#
#
# # Case A
# list_a = [1, 2, 3]
# list_a = [4, 5, 6]
# print(list_a)
# # Case B
# list_b = [1, 2, 3]
# list_b[:] = [4, 5, 6]
# nums = [10, 20, 30, 40, 50]
# for i in nums:
#     if i > 20:
#         nums.remove(i)
# print(nums)
#
# keys = ['a', 'b', 'c']
# d = dict.fromkeys(keys, [])
# d['a'].append(1)
# print(d)
# gen = (x for x in range(3))
# print(list(gen))
# print(list(gen))

def two_sum(arr, target):
    data = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in data:
            return diff, num
        data[num] = i

print(two_sum([2,5,7,20], 9))

'''reverse string'''

def rever_str(s):
    s = list(s)
    left, right = 0 , len(s) -1

    while left<right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

txt = 'hey,are,you,ok'
print(','.join([i[::-1] for i in txt.split(',')]))

def find_dup(arr):
    data = {}
    for num in arr:
        if num in data:
            return num
        data.add(num)


def longest_sub(txt):
    data = {}
    left = max_len = 0

    for right in range(len(txt)):
        if txt[right] in data:
            data.remove(txt[left])
            left += 1
        data.add(txt[right])
        max_len = max(max_len, right - left +1)
    return max_len

def is_valid(s):
    data = []
    mapping = {')':'(', '}':'{', ']':'['}

    for ch in s:
        if ch in mapping:
            if not data or data.pop() != mapping[ch]:
                return False
        else:
            data.append(ch)

    return not data


def find_missing(arr):
    n = len(arr)
    expected_sum = n * (n + 1)//2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

'''missing number using xor method'''

def missing(nums):
    result = 0
    for i in range(len(nums) + 1):
        result ^= i

    for num in nums:
        result ^= num

    return result
# print('missing number===>>')
# print(find_missing([3,0,1]))

'''merge 2 sorted array'''

arr = [2, 4, 60, 20, 4, 90]
for i in range(len(arr)):
    for j in range(0, len(arr) - i -1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sorted(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result

'''majority element'''

def majority_ele(nums):
    count = 0
    freq = None

    for num in nums:
        if count == 0:
            freq = num
        count += 1 if num == freq else - 1
    return freq
print(majority_ele([1,3,4,5,2,4]))


def majority_element(nums):
    count = 0
    ele = None
    for i in nums:
        if count == 0:
            ele = i
        count += 1 if i == ele else -1
    return ele
print(majority_element([2,2,1,1,1,2,2]))



def sort_dict(d):
    items = d.items()
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i][1]>items[j][1]:
                items[i], items[j] = items[j], items[i]
    return dict(items)


def move_zeo(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[j], arr[i]
            j += 1
            









