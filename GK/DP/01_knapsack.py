

def knapsack(weights, profits, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(weights))]

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, len(weights)):
        for c in range(1, capacity+1):
            if c < weights[i]:
                dp[i][c] = dp[i-1][c]
            else:
                dp[i][c] = max(dp[i-1][c], profits[i] + dp[i-1][c - weights[i]])

    return dp[-1][-1]


def knapsack_opt(weights, profits, capacity):
    dp = [0 for _ in range(capacity+1)]

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[c] = profits[0]

    for i in range(1, len(weights)):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[c-weights[i]]
            profit2 = dp[c]

            dp[c] = max(profit1, profit2)
    return dp[-1]


def knapsack_opt2(weights, profits, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(2)]

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = dp[1][c] = profits[0]

    for i in range(1, len(weights)):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]

            profit2 = dp[(i - 1) % 2][c]
            dp[i % 2][c] = max(profit1, profit2)

    return dp[(len(weights)-1) % 2][-1]


print(knapsack_opt2([2, 3, 1, 4], [4, 5, 3, 7], 5))
print(knapsack_opt2([1, 2, 3, 5], [1, 6, 10, 16], 7))
