"""
1143. 最长公共子序列  https://leetcode-cn.com/problems/longest-common-subsequence/
"""

def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


print(longestCommonSubsequence("abcde", "ace"))


print("718. 最长重复子数组")
def findLength(A, B):
    m = len(A)
    n = len(B)
    dp = [[0] * (n+1) for _ in range(m+1)]
    res = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
            else:
                dp[i][j] = 0
    return res


print(findLength([1,2,3,2,1], [3,2,1,4,7]))
