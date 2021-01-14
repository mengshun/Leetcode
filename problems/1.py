"""
1 两数之和
"""

def twoSum(nums, target):
    dp = {}
    for i, v in enumerate(nums):
        if target - v in dp:
            return [dp[target - v], i]
        else:
            dp[v] = i
    return []

print(twoSum([2,7,11,15], 9))