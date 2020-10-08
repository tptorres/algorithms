def count_palindromes(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    res = 0

    for i in range(n):
        dp[i][i] = True
        res += 1

    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if s[start] == s[end]:
                # check 2 length palindromes and everything inside current 2 chars
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    res += 1
    return res
