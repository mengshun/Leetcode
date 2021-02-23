"""
1438. 绝对差不超过限制的最长连续子数组
"""
from time import sleep
from collections import deque
from sortedcontainers import SortedList
def longestSubarray(nums, limit):
    s = SortedList()
    n = len(nums)
    left = right = ret = 0
    while right < n:
        s.add(nums[right])
        while s[-1] - s[0] > limit:
            s.remove(nums[left])
            left += 1
        right += 1
        ret = max(ret, right - left)
    return ret

def queueSubArray(nums, limit):
    n = len(nums)
    # 单调递减, 单调递增队列
    queMax, queMin = deque(), deque()
    left = right = ret = 0
    while right < n:
        while queMin and queMin[-1] > nums[right]:
            queMin.pop()
        while queMax and queMax[-1] < nums[right]:
            queMax.pop()
        queMin.append(nums[right])
        queMax.append(nums[right])
        while queMin and queMax and queMax[0] - queMin[0] > limit:
            if nums[left] == queMin[0]:
                queMin.popleft()
            if nums[left] == queMax[0]:
                queMax.popleft()
            left += 1
        right += 1
        ret = max(ret, right - left)
    return ret



print(longestSubarray([8, 2, 2, 4], 2))
print(queueSubArray([8, 2, 2, 4], 2))
print(queueSubArray([4, 3, 2, 1, 5], 4))

t = [4,6,2,1,3,5]
print(t)

queueMin, queueMax = deque(), deque()
for v in t:
    while queueMin and queueMin[-1] > v:
        queueMin.pop()
    while queueMax and queueMax[-1] < v:
        queueMax.pop()
    queueMin.append(v)
    queueMax.append(v)

print(queueMin, queueMax)



"""
766. 托普利茨矩阵
"""

def isToeplitzMatrix(matrix):
    if len(matrix) < 2:
        return True
    pre = matrix[0]
    n = len(pre)
    for v in matrix[1:]:
        for i in range(1, n):
            if v[i] != pre[i-1]:
                return False
        pre = v
    return True

print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))