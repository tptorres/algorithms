import math


def max_ribbon_length(ribbons, n):
    dp = [[-math.inf for _ in range(n+1)] for _ in range(len(ribbons))]

    for i in range(len(ribbons)):
        dp[i][0] = 0

    for i in range(len(ribbons)):
        for r in range(1, n+1):
            if i > 0:
                dp[i][r] = dp[i-1][r]
            if ribbons[i] <= r:
                if dp[i][r - ribbons[i]] != -math.inf:
                    dp[i][r] = max(dp[i][r], 1 + dp[i][r - ribbons[i]])

    return dp[-1][-1]


print(max_ribbon_length([3, 5, 7], 13))
