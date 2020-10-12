def can_partition(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    total = total // 2
    dp = [[False for _ in range(total+1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for s in range(1, total+1):
        dp[0][i] = nums[0] == s

    for i in range(1, len(nums)):
        for s in range(1, total+1):
            if dp[i-1][s]:
                dp[i][s] = dp[i-1][s]
            elif nums[i] <= s:
                dp[i][s] = dp[i-1][s - nums[i]]
    return dp[-1][-1]


def can_partition_opt(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    total //= 2
    dp = [[False for _ in range(total+1)] for _ in range(2)]

    dp[0][0] = dp[1][0] = True

    for s in range(total+1):
        dp[0][s] = dp[1][s] = nums[0] == s

    for i in range(1, len(nums)):
        for s in range(0, total + 1):
            if dp[(i - 1) % 2][s]:
                dp[i % 2][s] = dp[(i - 1) % 2][s]
            elif nums[i] <= s:
                dp[i % 2][s] = dp[(i - 1) % 2][s - nums[i]]

    return dp[(len(nums)-1) % 2][-1]


print(can_partition_opt([1, 2, 3, 4]))
print(can_partition_opt([1, 1, 3, 4, 7]))
print(can_partition_opt([2, 3, 4, 6]))
