def LPS(s):
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    return helper(0, len(s)-1, s, dp)


def helper(start, end, s, dp):
    if start > end:
        return 0
    if start == end:
        return 1

    if dp[start][end] == -1:
        if s[start] == s[end]:
            dp[start][end] = 2 + helper(start+1, end-1, s, dp)
        else:
            s1 = helper(start+1, end, s, dp)
            s2 = helper(start, end-1, s, dp)
            dp[start][end] = max(s1, s2)
    return dp[start][end]


def LPS_bottom(s):
    n = len(s)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    # base case is every 1 element subsequence is a palindrome
    for i in range(n):
        dp[i][i] = 1

    for start in reversed(range(0, n-1)):
        for end in range(start+1, n):
            if s[start] == s[end]:
                dp[start][end] = 2 + dp[start+1][end-1]
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])
    return dp[0][-1]


print(LPS_bottom("cddpdd"))
