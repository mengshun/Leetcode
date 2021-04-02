"""
239. 滑动窗口最大值   https://leetcode-cn.com/problems/sliding-window-maximum/
"""

import collections
def maxSlidingWindow(nums, k):
    # 双端队列
    queue = collections.deque()
    res = []
    for i in range(len(nums)):
        # 添加之前判定尾部是否有值小于当前值
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        queue.append(i)
        # 添加之后 查看首部索引是否在当前k范围内
        while queue[-1] - queue[0] > k-1:
            queue.popleft()
        # 当加入k次时 才开始向结果添加数据
        if i >= k-1:
            res.append(nums[queue[0]])
    return res


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1,-1], 1))
print(maxSlidingWindow([7,2,4], 2))