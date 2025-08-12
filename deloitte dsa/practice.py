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































