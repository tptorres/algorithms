def coin_change(denoms, target):
    dp = [[0 for _ in range(target+1)] for _ in range(len(denoms))]

    for i in range(len(denoms)):
        dp[i][0] = 1

    for i in range(len(denoms)):
        for t in range(1, target+1):
            if t >= denoms[i]:
                dp[i][t] = dp[i][t - denoms[i]]
            if i > 0:
                dp[i][t] += dp[i-1][t]

    return dp[-1][-1]


print(coin_change([1, 2, 3], 5))
