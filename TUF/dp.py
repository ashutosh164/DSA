'''logest common substring'''


def longest_common_substring(a,b):
    m = len(a)
    n = len(b)

    dp = [[0]*(n+1) for _ in range(m +1)]

    max_len = 0
    end_index = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1]== b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i -1
            else:
                dp[i][j] = 0

    if max_len == 0:
        return ''
    else:
        return a[end_index - max_len + 1:end_index+1]

print(longest_common_substring('abcdefgh','xyzdefg'))


def logest_substring(string):
    char = set()
    l = 0
    res = 0
    for r in range(len(string)):
        while string[r] in char:
            char.remove(string[l])
            l += 1
        char.add(string[r])
        res = max(res, r-l +1)
    return res

print(logest_substring('abcdabcbcbb'))

dp = [[0] * (6 + 1) for _ in range(5 + 1)]
print(dp)




















