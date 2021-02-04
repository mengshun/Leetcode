"""
643. 子数组最大平均数 I
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
"""

def findMaxAverage(nums, k):
    n = len(nums)
    if k == 1:
        return max(nums)

    sum_value = sum(nums[:k])
    max_average = sum_value / k

    for i in range(n - k):
        sum_value = sum_value - nums[i] + nums[i+k]
        max_average = max(max_average, sum_value / k)

    return max_average


print(findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.75
