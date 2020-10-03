def fibonacci_numbers(n):
    if n < 2:
        return n

    return fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)


def fibonacci_numbers_memo(n):
    memo = [-1 for _ in range(n+1)]
    return fib_memo(n, memo)


def fib_memo(n, memo):
    if n < 2:
        return n

    if memo[n] >= 0:  # means it has been processed already ; overlapping subproblem
        return memo[n]

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


def fib_tabulation(n):
    memo = [-1 for _ in range(n+1)]

    memo[0] = 0
    memo[1] = 1

    for i in range(2, len(memo)):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


def fib_optimized(n):
    n1, n2, temp = 0, 1, 0
    for i in range(2, n+1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2


print(fibonacci_numbers(6))
print(fibonacci_numbers_memo(6))
print(fib_tabulation(5))
print(fib_optimized(6))
