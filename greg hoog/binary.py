

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high-low)//2)
        if arr[low] == target:
            return low
        elif target < arr[mid]:
            high =  mid - 1
        else:
            low = mid + 1
    return False

print(binary_search([1,2,3,4,5,6,7,8,9,10], 4))


