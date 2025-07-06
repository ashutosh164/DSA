from http.cookiejar import is_HDN

print('=========sort linkedlist===========')
''' 
approach
============

fn(ll)
-> if ll == null or head.next == null
    return head
-> low = 0 , 
 
 
 '''



'''merge sort'''
arr = [3, 6, 2, 8, 4, 8, 9, 6, 1, 9, 0]

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    # low ... mid
    # mid+1 ... high
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1



def merge_sort(arr, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr,mid+1,high)
    merge(arr, low, mid, high)


if __name__ == '__main__':
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)