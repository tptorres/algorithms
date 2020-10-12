def count_subsets(nums, s):
    dp = [[0 for _ in range(s+1)] for _ in range(2)]

    # base case for sum == 0
    dp[0][0] = dp[1][0] = 1

    for i in range(1, s+1):
        dp[0][i] = dp[1][i] = 1 if nums[0] == i else 0

    for i in range(1, len(nums)):
        for s in range(1, s+1):
            dp[i % 2][s] = dp[(i - 1) % 2][s]
            if nums[i] <= s:
                dp[i % 2][s] += dp[(i - 1) % 2][s - nums[i]]

    return dp[(len(nums)-1) % 2][-1]


print(count_subsets([1, 1, 2, 3], 4))
print(count_subsets([1, 2, 7, 1, 5], 9))
