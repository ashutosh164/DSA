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





























