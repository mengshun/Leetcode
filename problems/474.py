"""
474. 一和零
https://leetcode-cn.com/problems/ones-and-zeroes/
"""
def findMaxForm(strs, m, n):
    dp = [[0] * (n+1) for _ in range(m+1)]
    for v in strs:
        length = len(v)
        ones = v.count("1")
        zeros = length - ones
        for i in range(m, zeros-1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
    return dp[-1][-1]


print(findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))