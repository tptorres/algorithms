def LPS(s):
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    return helper(0, len(s)-1, s, dp)


def helper(left, right, s, dp):
    if left == right:
        return 1
    if left > right:
        return 0

    if dp[left][right] == -1:
        if s[left] == s[right]:
            remaining_length = right - left - 1

            if remaining_length == helper(left+1, right-1, s, dp):
                dp[left][right] = 2 + remaining_length
                return 2 + remaining_length

        sub2 = helper(left+1, right, s, dp)
        sub3 = helper(left, right-1, s, dp)
        dp[left][right] = max(sub2, sub3)

    return dp[left][right]


def LPS_bottom_up(s):
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    n = len(s)

    # base cases
    for i in range(n):
        dp[i][i] = True

    max_length = 1
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if s[start] == s[end]:
                if end - start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    max_length = max(max_length, end - start + 1)
    return max_length


print(LPS_bottom_up("cddd"))
