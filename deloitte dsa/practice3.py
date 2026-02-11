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
    stack = set()
    longest = 0

    for right in range(len(txt)):
        while txt[right] in stack:
            stack.remove(txt[left])
            left += 1
        stack.add(txt[right])
        longest = max(longest, right-left+1)
    return longest

print(log_sub('abcbcab'))









