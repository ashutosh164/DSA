# ✅ Two Sum (Leetcode 1)
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

# ✅ Majority Element (Leetcode 169)
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

# ✅ Longest Consecutive Sequence (Leetcode 128)
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

# ✅ Subarray Sum Equals K (Leetcode 560)
def subarray_sum(nums, k):
    count = 0
    cum_sum = 0
    hashmap = {0: 1}
    for num in nums:
        cum_sum += num
        count += hashmap.get(cum_sum - k, 0)
        hashmap[cum_sum] = hashmap.get(cum_sum, 0) + 1
    return count

# ✅ Group Anagrams (Leetcode 49)
from collections import defaultdict

def group_anagrams(strs):
    hashmap = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        hashmap[key].append(word)
    return list(hashmap.values())

# ✅ Longest Substring Without Repeating Characters (Leetcode 3)
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

# ✅ Minimum Window Substring (Leetcode 76)
from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""
    t_count = Counter(t)
    window = {}
    have, need = 0, len(t_count)
    res, res_len = [-1, -1], float("inf")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1
        if c in t_count and window[c] == t_count[c]:
            have += 1
        while have == need:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            window[s[l]] -= 1
            if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""

# ✅ Valid Anagram (Leetcode 242)
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

# ✅ Longest Palindromic Substring (Leetcode 5)
def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        temp = expand(s, i, i)
        if len(temp) > len(res):
            res = temp
        temp = expand(s, i, i + 1)
        if len(temp) > len(res):
            res = temp
    return res

def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]
