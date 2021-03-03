"""
485. 最大连续1的个数
"""

def findMaxConsecutiveOnes(nums):
    n = len(nums)
    res = 0
    left = right = 0
    while right < n:
        if nums[right] == 0:
            res = max(res, right - left)
            left = right + 1
        right += 1
    res = max(res, right - left)
    return res

from builtins import str

def strfunction(nums):
    nums_str = "".join([str(x) for x in nums])
    res = nums_str.split("0")
    counts = [len(x) for x in res]
    return max(counts)

# 一次遍历
def bianli(nums):
    count = 0
    maxcount = 0
    for v in nums:
        if v == 0:
            maxcount = max(maxcount, count)
            count = 0
        else:
            count += 1
    maxcount = max(maxcount, count)
    return maxcount




print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(strfunction([1,1,0,1,1,1]))
print(bianli([1,1,0,1,1,1]))


"""
1004. 最大连续1的个数 III
"""

def longestOnes(A, K):
    n = len(A)
    res = count = left = right = 0
    while right < n:
        count += A[right] == 0
        while count > K:
            count -= A[left] == 0
            left += 1
        right += 1
        res = max(res, right - left)
    return res


print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(longestOnes([0, 0], 0))
