def LCS(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return helper(s1, s2, 0, 0, dp)


def helper(s1, s2, idx1, idx2, dp):
    if idx1 >= len(s1) or idx2 >= len(s2):
        return 0

    if dp[idx1][idx2] == -1:
        lg1 = 0
        if s1[idx1] == s2[idx2]:
            lg1 = 1 + helper(s1, s2, idx1+1, idx2 + 1, dp)
        lg2 = helper(s1, s2, idx1 + 1, idx2, dp)
        lg3 = helper(s1, s2, idx1, idx2 + 1, dp)

        dp[idx1][idx2] = max(lg1, lg2, lg3)
    return dp[idx1][idx2]


def LCS_tabulation(s1, s2):
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    max_length = 0

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])

    return max_length


def LCS_tabulation_opt(s1, s2):
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(2)]

    max_length = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            dp[i % 2][j] = 0  # why?? come back to
            if s1[i-1] == s2[j-1]:
                dp[i % 2][j] = 1 + dp[(i-1) % 2][j-1]
                max_length = max(max_length, dp[i % 2][j])

    return max_length


print(LCS_tabulation_opt("abdca", "cbda"))
print(LCS_tabulation_opt("passport", "ppsspt"))
