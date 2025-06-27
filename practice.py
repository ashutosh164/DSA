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
        high = len(arr) - 1
    if low < high:
        pivote_index = partition(arr, low, high)
        quickshort(arr, low, pivote_index-1)
        quickshort(arr, pivote_index + 1, high)

nums = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]
quickshort(nums)
print(nums)



