"""
53 最大子序和
"""

import collections

def maxSubArray(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    return max(dp)


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6