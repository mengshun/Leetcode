"""
115. 不同的子序列
https://leetcode-cn.com/problems/distinct-subsequences/
"""

def numDistinct(s: str, t: str):
    m, n = len(s), len(t)
    if n > m:
        return 0

    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][n] = 1
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j]
    return dp[0][0]

def numDistinctOther(s: str, t: str):
    m, n = len(s), len(t)
    if n > m:
        return 0

    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(i, m+1):
            if t[i-1] == s[j-1]:
                dp[j][i] = dp[j-1][i-1] + dp[j-1][i]
            else:
                dp[j][i] = dp[j-1][i]
    return dp[m][n]

"""
babgbag
bag


"""




print("numDistinct: ", numDistinctOther("rabbbit", "rabbit")) # 3
print("numDistinct: ", numDistinctOther("babgbag", "bag")) # 5
print("numDistinct: ", numDistinctOther("babb", "bbb")) # 1