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








