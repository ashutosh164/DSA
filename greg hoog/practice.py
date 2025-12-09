'''longest substring without repeating ch'''

txt = 'abcabcbbd'


l = 0
longest = 0
sett = set()

n = len(txt)

for i in range(n):
    if txt[i] in sett:
        sett.remove(txt[i])
        l += 1
    w = (i - l) + 1
    longest = max(longest, w)
    sett.add(txt[i])

print(longest)

'''fixed length sliding window problem'''
x = 2

def fun(a):
    global x
    x = 10

    def func(b):
        return b

    return x

print(fun(x))
print(x)








