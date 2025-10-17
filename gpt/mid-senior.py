print('============two sum===========')

def two_su(arr, target):
    stack = {}
    for i, val in enumerate(arr):
        diff = target - val
        if diff in stack:
            return [diff, val]
        stack[val] = i
    return []

print(two_su([2,3,5,7], 9))
'''
Q2. Longest Substring Without Repeating Characters (Sliding Window)
'''



