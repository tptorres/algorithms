import math


def min_jumps(arr):
    dp = [0 for _ in range(len(arr))]
    return helper(0, arr, dp)


def helper(index, arr, dp):
    # positive base case
    if index == len(arr) - 1:
        return 0
    if arr[index] == 0:
        return math.inf

    if dp[index] != 0:
        return dp[index]

    total_jumps = math.inf
    start, end = index + 1, index + arr[index]  # range 1 -> p (1,p]
    while start < len(arr) and start <= end:
        min_jumps = helper(start, arr, dp)  # start is the new index
        if min_jumps != math.inf:
            total_jumps = min(total_jumps, min_jumps + 1)

        start += 1

    dp[index] = total_jumps
    return total_jumps

# O(n^2) T | O(n) S


def min_jumps_tab(arr):
    n = len(arr)
    dp = [math.inf for _ in range(n)]
    dp[n-1] = 0

    for i in range(n-2, -1, -1):
        start, end = i + 1, min(i + arr[i] + 1, n)
        for j in range(start, end):
            dp[i] = min(dp[i], dp[j] + 1)

    return dp[0]


# def min_jumps_tab(nums):
#     n = len(nums)
#     min_jumps = 0
#     prev = 0

#     for start in range(n-1):
#         left, right = start + 1, start + nums[start]
#         current = math.inf
#         while left <= right and left < n:
#             temp = min(current, prev + 1)
#             current = temp

#             left += 1
#         prev = current


print(min_jumps_tab([2, 1, 1, 1, 4]))
