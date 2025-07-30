'''
1. get the binary bits between these numbers ranging from 3 to 9.
Find how many ones are present in that if the 1's count value is greater
 the last digit return the last number otherwise print the 1's count.
'''


def binary_one_count(start, end):
    total_one = 0
    for i in range(start, end+1):
        bin_str = bin(i)[2:]
        total_one += bin_str.count('1')
    if total_one > end:
        return end

    return total_one

print(binary_one_count(3,9))


'''
✅ Part 2: Minimum Operations in an Array

 Example: Minimum operations to make all elements equal by incrementing or decrementing (typical interview problem)
Logic: Choose the median as target. Each step is |element - median|. Sum it up.
'''
def min_operations_to_equal(arr):
    arr.sort()
    median = arr[len(arr) // 2]
    return sum(abs(x - median) for x in arr)

# Example usage:
arr = [1, 2, 3, 5]
print(min_operations_to_equal(arr))  # Output: 4






