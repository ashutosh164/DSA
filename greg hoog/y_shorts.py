#  palindrom

string = 'abcdcba'
# string = 'abcdceba'

def is_palindrome(string):
    n = len(string)
    l = 0
    r = n - 1

    while l <= r:
        if string[l] == string[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

print(is_palindrome(string))

print('=========product of array except of self==========')

def product_except_self(arr):
    n = len(arr)
    left = [0]*n
    right = [0]*n
    l = 1
    r = 1
    for i, num in enumerate(arr):
        left[i] = l
        j = -i-1
        right[j] = r
        l*= num[i]
        r *= num[j]
    return [l*r for l, r in zip(left, right)]


# print(product_except_self([1,2,3,4]))

print('=====majority element=========')

def majority_element(arr):
    count = 0
    elm = None
    for i in arr:
        if count == 0:
            elm = i
        count += 1 if elm == i else -1
    return count

print(majority_element([1,1,1,2,3,4,4,4,4]))



