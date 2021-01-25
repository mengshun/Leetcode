"""
300 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""

def lengthOfLIS(nums):
    n = len(nums)
    if n < 2:
        return n

    dp = [1] * n
    for j in range(1, n):
        for i in range(j):
            if nums[j] > nums[i]:
                dp[j] = max(dp[j], dp[i] + 1)

    return max(dp)


def lengthOfLIS2(nums):
    size = len(nums)
    if size < 2:
        return size

    cell = [nums[0]]
    for num in nums[1:]:
        if num > cell[-1]:
            cell.append(num)
            continue

        l, r = 0, len(cell) - 1
        while l < r:
            mid = l + (r - l) // 2
            if cell[mid] < num:
                l = mid + 1
            else:
                r = mid
        cell[l] = num
    return len(cell)




print(lengthOfLIS2([10,9,2,5,3,7,101,18])) # 4
print(lengthOfLIS2([0,1,0,3,2,3]))# 4
print(lengthOfLIS2([7,7,7,7,7,7,7]))# 1
print(lengthOfLIS2([10,9,2,5,3,4])) #3
print(lengthOfLIS2([3,5,6,2,5,4,19,5,6,7,12])) #6
