def factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n-1)


def factorial_iter(n):
    if n == 0 or n == 1:
        return 1

    res = 1
    for i in range(2, n+1):
        res *= i

    return res


def factorial_dp(n):
    memo = [-1 for _ in range(n+1)]
    return helper(n, memo)


def helper(n, memo):
    if n == 1:
        return n

    if memo[n] >= 0:
        return memo[n]

    memo[n] = n * helper(n-1, memo)
    return memo[n]


print(factorial_dp(30))
