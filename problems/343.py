"""
343. 整数拆分
https://leetcode-cn.com/problems/integer-break/
"""

def integerBreak(n):
    dp = [1] * (n+1)
    for i in range(2, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
    return dp[n]

def integerBreakOther(n):
    if n <= 3:
        return n - 1
    # n = 3a + b
    a, b = n // 3, n % 3
    if b == 0:
        return 3 ** a
    elif b == 2:
        return 3 ** a * b
    elif b == 1:
        return 3 ** (a - 1) * 4





print(integerBreak(2)) # 1
print(integerBreak(10)) # 36
print(integerBreak(100)) # 36

print(integerBreakOther(2)) # 1
print(integerBreakOther(10)) # 36
print(integerBreakOther(100)) # 36
