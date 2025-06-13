print('==============Check if Two Strings are Anagrams==========')
'''
 Logic:
If lengths differ → return False.

Count frequency of each character in both strings.

Compare the two frequency maps.
'''


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count_s = {}
    count_t = {}

    for ch in s:
        count_s[ch] = count_s.get(ch, 0) + 1
    for ch in t:
        count_t[ch] = count_t.get(ch, 0) + 1

    return count_s == count_t


print(is_anagram("listen", "silent"))
print(is_anagram("aabbcc", "baccab"))
print(is_anagram("rat", "car"))
print('========more optimize way========')

def is_anagrams(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for i in range(len(s)):
        count[s[i]] = count.get(s[i], 0) + 1
        count[t[i]] = count.get(t[i], 0) - 1
    for val in count.values():
        if val != 0:
            return False
    return True


print(is_anagrams("listen", "silent"))  # True
print(is_anagrams("hello", "world"))    # False
print(is_anagrams("aabbcc", "baccab"))  # True

