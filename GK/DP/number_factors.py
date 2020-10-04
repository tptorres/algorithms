# Brute Force
def number_factors(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2

    return number_factors(n-1) + number_factors(n-3) + number_factors(n-4)


# Top-Down Memo
def number_factors_memo(n):
    memo = [-1 for _ in range(n+1)]
    return memo_helper(n, memo)


def memo_helper(n, memo):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2

    if memo[n] >= 0:
        return memo[n]
    memo[n] = memo_helper(n-1, memo) + memo_helper(n-3, memo) + memo_helper(n-4, memo)
    return memo[n]

# Bottom Up


def number_factors_bottom(n):
    dp = [-1 for _ in range(n+1)]
    dp[0], dp[1], dp[2], dp[3] = 1, 1, 1, 2
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]

    return dp[n]


def number_factors_opt(n):
    n1, n2, n3, n4 = 1, 1, 1, 2
    temp = 0
    for i in range(4, n+1):
        temp = n1 + n2 + n4
        n1 = n2
        n2 = n3
        n3 = n4
        n4 = temp
    return n4


print(number_factors_bottom(7))
print(number_factors_opt(7))
