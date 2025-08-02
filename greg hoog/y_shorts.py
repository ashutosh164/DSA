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





