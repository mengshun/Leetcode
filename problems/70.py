"""
70 爬楼梯
"""

# 爬楼梯 一次可以爬1或者2个阶梯 类似斐波那契数列

def climbStairs(n):

    dp = {0:0, 1:1, 2:2}
    def count(t):
        if t in dp:
            return dp[t]
        dp[t] = count(t-1) + count(t-2)
        return dp[t]
    return count(n)


print(climbStairs(10))