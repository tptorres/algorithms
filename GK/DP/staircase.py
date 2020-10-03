def staircase(n):
    if n < 0:
        return 0

    if n == 0:
        return 1

    return staircase(n-1) + staircase(n-2) + staircase(n-3)


def staircase_memo(n):
    memo = [-1 for _ in range(n+1)]
    return staircase_helper(n, memo)


def staircase_helper(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1

    if memo[n] >= 0:
        return memo[n]

    memo[n] = staircase(n-1) + staircase(n-2) + staircase(n-3)
    return memo[n]


def staircase_tabulation(n):
    memo = [-1 for _ in range(n+1)]
    memo[0], memo[1], memo[2] = 1, 1, 2

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]


def staircase_opt(n):
    n1, n2, n3, temp = 1, 1, 2, 0
    if n < 2:
        return n2

    for i in range(3, n+1):
        temp = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = temp

    return n3


print(staircase_opt(1))
