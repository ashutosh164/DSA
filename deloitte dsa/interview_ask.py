txt = 'hey,are,you,ok'
out = 'yeh, era, uoy, ko'

s = ''
temp = ''
rev_w = [i[::-1] for i in txt]
# print(rev_w)
# print(s)
# print(temp)

txt = txt.split(',')
rev_word = [word[::-1] for word in txt]
out = ', '.join(rev_word)
print(out)

'''short the list and return the 2nd highest number'''

arr = [2, 4, 60, 20, 4, 90]

first = float('-inf')
second = float('-inf')

for num in arr:
    # If current number is greater than first
    if num > first:
        second = first
        first = num

    # If current number is between first and second
    elif num > second and num != first:
        second = num

print("Second highest:", second)


