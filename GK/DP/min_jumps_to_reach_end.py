import math


def min_jumps(arr):
    return helper(0, arr)


def helper(index, arr):
    # positive base case
    if index == len(arr) - 1:
        return 0

    if arr[index] == 0:
        return math.inf

    jumps = math.inf


print(min_jumps([2, 1, 1, 1, 4]))
