def min_coin_change(denoms, target):
    dp = [[float("inf") for _ in range(target+1)] for _ in range(len(denoms))]

    for i in range(len(denoms)):
        dp[i][0] = 0

    for i in range(len(denoms)):
        for c in range(1, target+1):
            coins1, coins2 = float("inf"), float("inf")
            if denoms[i] <= c:
                coins1 = 1 + dp[i][c - denoms[i]]
            if i > 0:
                coins2 = dp[i-1][c]

            dp[i][c] = min(coins1, coins2)

    return dp[-1][-1]


print(min_coin_change([1, 5, 10], 7))
