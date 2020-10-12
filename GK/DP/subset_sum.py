def subset_sum(nums, s):
    dp = [[False for _ in range(s+1)] for _ in range(2)]

    # base cases for sum == 0
    dp[0][0] = dp[1][0] = True

    for s in range(1, s+1):
        dp[0][s] = dp[1][s] = nums[0] == s

    for i in range(1, len(nums)):
        for s in range(1, s+1):
            if dp[(i - 1) % 2][s]:
                dp[i % 2][s] = dp[(i - 1) % 2][s]
            elif nums[i] <= s:
                dp[i % 2][s] = dp[(i - 1) % 2][s - nums[i]]

    return dp[(len(nums)-1) % 2][-1]


print(subset_sum([1, 2, 3, 7], 6))
print(subset_sum([1, 2, 7, 1, 5], 10))
print(subset_sum([1, 3, 4, 8], 6))
