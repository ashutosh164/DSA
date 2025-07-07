''' hash set'''
from pkgutil import iter_modules

s = set()
s.add(1)
s.add(2)
s.add(3)

print(s)
# lookup if item in set - O(1)
if 1 in s:
    print(True)

# remove item form set - O(1)
s.remove(3)
print(s)
# set construction - O(n) n is the length of string
string = 'aaassssshhhhhhhhuuuuuu'

print(set(string))
# loop over items in set O(n)
for x in s:
    print(x)

# hashmap - Dictionaries

d = {'ashu': 1, 'jilu': 2, 'silu': 3}
# add key:val in dictionaries: O(1)
d['jyoti'] = 4

# if 'jilu' in d:
#     print(True)
#
# for key, val in d.items():
#     print(key,val)
#
#
# from collections import defaultdict
# default = defaultdict(list)
#
# default[2]
#
# print(default)
#
# from collections import Counter
# string = 'aaassssshhhhhhhhuuuuuutttttttt'
#
# print(string)
# print(Counter(string))
'''
return character with max repeate
'''

def char_count(string):
    char = {}
    for i in string:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1

    chr_freq = 0
    max_char = []
    for chr, val in char.items():
        if val > chr_freq:
            max_char = [chr]
            chr_freq = val
        elif val == chr_freq:
            max_char.append(chr)
    print(f'char with max freq {chr_freq}:{max_char}')
    return char

print(char_count(string))
print('===========two sum===========')

def two_sum(arr, target):
    hashmap = {}

    for item, val in enumerate(arr):
        diff = target - val
        if diff in hashmap:
            return [diff, val]
        hashmap[val] = item
    return hashmap

arr = [2,5,7,10]
target = 9
print(two_sum(arr, target))

'''
    2. Longest Substring Without Repeating Characters
    
    Problem: Find the length of the longest substring with all unique characters.
    HashMap Use: Track last index of each character.
    Difficulty: Medium
'''



