print('==========quick short=============')
def partition(arr, low, high):
    pivote = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickshort(arr, low=0, high=None):
    if high is None:
        high = len(arr) -1
    if low <= high:
        pivote_index = partition(arr, low, high)
        quickshort(arr, low, pivote_index - 1)
        quickshort(arr, pivote_index+1, high)

nums = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]
quickshort(nums)
print(nums)
print('==========2 sum============')

arr = [1,2,5,7,9]
target = 12

def func(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        val = arr[low] + arr[high]
        if val == target:
            return arr[low], arr[high]
        elif val < target:
            low += 1
        else:
            high -= 1
    print()
print(func(arr, target))

print('======for unsorted arry==========')

def fun2(arr, target):
    set = {}
    for item, val in enumerate(arr):
        num = target - val
        if num in set:
            return [num, val]
        set[val] = item
print(fun2(arr, target))
nums = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]

def sotred(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1
a =  sotred(nums)
print(nums[:a])










