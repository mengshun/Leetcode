"""
673. 最长递增子序列的个数
给定一个未排序的整数数组，找到最长递增子序列的个数。
"""
import collections

def findNumberOfLIS(nums):
    n = len(nums)
    if n < 2:
        return n
    lengths = [1] * n
    counts = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                if lengths[j] + 1 > lengths[i]: #第一次遇到最长子序列
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]: #已经遇到过最长子序列
                    counts[i] += counts[j]

    longest = max(lengths)
    return sum(v for i, v in enumerate(counts) if lengths[i] == longest)


print(findNumberOfLIS([1,3,5,4,7])) #2
print(findNumberOfLIS([2,2,2,2,2])) #5
