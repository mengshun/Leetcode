"""
674. 最长连续递增序列
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

"""

# 贪心算法
def findLengthOfLCIS(nums):
    ans = 0
    start = 0
    for i in range(len(nums)):
        if i > 0 and nums[i-1] >= nums[i]:
            start = i
        ans = max(ans, i - start + 1)
    return  ans

def findLengthOfLCIS2(nums):
    if len(nums) < 2:
        return len(nums)
    ans = 0
    dp = [1 for _ in nums]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1] + 1
        ans = max(dp[i], ans)
    return ans





print(findLengthOfLCIS([1,3,5,4,7])) #3
print(findLengthOfLCIS2([1,3,5,4,7])) #3