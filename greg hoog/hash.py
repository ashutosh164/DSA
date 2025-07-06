''' hash set'''

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

if 'jilu' in d:
    print(True)









