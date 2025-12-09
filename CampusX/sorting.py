'''bubble short'''
arr = [5,2,4,8,5,10,34]

for i in range(len(arr) -1):
    flg = 0
    for j in range(len(arr) -1 -i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flg = 1
    if flg == 1:
        break
print(arr)

'''selection short'''
arr = [9,2,4,10,44,3]
for i in range(len(arr) -1):
    min = i
    for j in range(i +1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

print(arr)
print(arr[-2])




