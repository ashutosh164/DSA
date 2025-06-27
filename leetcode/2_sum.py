arr = [2, 7, 11, 15]
target = 9


def two_sum(arr, target):
    set = {}

    for item, value in enumerate(arr):
        numb = target - value
        if numb in set:
            return [set[numb], item]
        set[value] = item

print(two_sum(arr, target))

'''2nd method'''


def tow_sum2(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        new_val = arr[low] + arr[high]
        if new_val == target:
            return arr[low], arr[high]
        elif new_val < target:
            low += 1
        else:
            high -= 1
    print()

arr = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]
# arr = [2,1,5,7,9]


def func(arr, target):
    set = {}

    for item, val in enumerate(arr):
        num = target - val
        if num in set:
            return [set[num], val]
        set[val] = item

print(func(arr,10))


