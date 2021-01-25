"""
334. 递增的三元子序列
给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
"""

def increasingTriplet(nums):

    size = len(nums)
    if size < 3:
        return False

    dp = [1] * size

    for i in range(1, size):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] > 2:
                    return True
    return False

def other(nums):
    size = len(nums)
    if size < 3:
        return False

    res = [nums[0]]
    for v in nums[1:]:
        if v > res[-1]:
            res.append(v)
            if len(res) > 2:
                return True
            continue

        left, right = 0, len(res) - 1
        while left < right:
            mid = left + (right - left >> 1)
            if res[mid] < v:
                left = mid + 1
            else:
                right = mid
        res[left] = v

    return False

def good(nums):
    if len(nums) < 3:
        return False

    left = mid = float('inf')
    for v in nums:
        if v <= left:
            left = v
        elif v <= mid:
            mid = v
        elif v > mid:
            return True
    return False


print(increasingTriplet([5,4,3,2,1])) # false
print(other([5,4,3,2,1])) # false
print(increasingTriplet([1,2,3,2,1])) # false
print(other([1,2,3,2,1])) # false

print(increasingTriplet([20,100,10,12,5,13])) # True
print(other([20,100,10,12,5,13])) # True

print(good([20,100,10,12,5,13])) # True
