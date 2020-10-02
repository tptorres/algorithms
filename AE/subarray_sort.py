# Type: Array, Two Pointers
def subarray_sort(array):
    res = []
    left, right = 1, len(array)-2

    while left < len(array) and array[left] >= array[left-1]:
        left += 1

    if left == len(array):
        return [-1, -1]

    while right >= 0 and array[right] <= array[right+1]:
        right -= 1

    maxNum = max(array[left-1:right+2])
    minNum = min(array[left-1:right+2])

    left -= 1
    right += 1

    while left >= 0 and minNum < array[left]:
        left -= 1
    while right < len(array) and maxNum > array[right]:
        right += 1

    return [left+1, right - 1]


# print(subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]))
