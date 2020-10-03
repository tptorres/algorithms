def unbounded_knapsack(weights, profits, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(weights))]
    return knapsackHelper(0, weights, profits, capacity, dp)

# Top Down Memo


def knapsackHelper(index, weights, profits, capacity, dp):
    if capacity <= 0 or index >= len(weights):
        return 0

    if dp[index][capacity] == -1:
        profit1 = 0
        if weights[index] <= capacity:
            profit1 = profits[index] + knapsackHelper(index, weights, profits, capacity - weights[index], dp)

        profit2 = knapsackHelper(index+1, weights, profits, capacity, dp)
        dp[index][capacity] = max(profit1, profit2)

    return dp[index][capacity]

# Bottom-Up Tabulation


def knapsackBottom(weights, profits, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(weights))]

    for j in range(capacity+1):
        if j >= weights[0]:
            dp[0][j] = profits[0] + dp[0][j-weights[0]]

    for i in range(1, len(weights)):
        for j in range(1, capacity+1):
            if j >= weights[i]:
                dp[i][j] = max(dp[i-1][j], profits[i] + dp[i][j - weights[i]])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


print(knapsackBottom([1, 2, 3], [15, 20, 50], 8))
