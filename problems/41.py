"""
41. 缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
"""

def firstMissingPositive(nums):
    dp = set(nums)
    n = len(nums)
    for i in range(1, n+1):
        if i not in dp:
            return i
    return n+1

def jinjie(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1
    for i in range(n):
        cur = abs(nums[i])
        if cur <= n:
            nums[cur - 1] = - abs(nums[cur - 1])
    for i in range(n):
        if nums[i] > 0:
            return i+1
    return n+1



print(firstMissingPositive([1,2,0])) # 3
print(jinjie([1,2,0])) # 3
print(firstMissingPositive([3,4,-1,1])) # 2
print(firstMissingPositive([7,8,9,11,12])) # 1