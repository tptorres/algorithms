def rod_cutting(lengths, prices, rod):
    dp = [[-1 for _ in range(rod+1)] for _ in range(len(lengths))]

    for i in range(len(prices)):
        dp[i][0] = 0

    for i in range(len(lengths)):
        for l in range(1, rod+1):
            profit1, profit2 = 0, 0
            if l >= lengths[i]:
                profit1 = prices[i] + dp[i][l-lengths[i]]

            if i > 0:
                profit2 = dp[i-1][l]
            dp[i][l] = max(profit1, profit2)

    return dp[-1][-1]


print(rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
