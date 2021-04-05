"""
347. 前 K 个高频元素  https://leetcode-cn.com/problems/top-k-frequent-elements/
"""
import collections
def topKFrequent(nums, k):
    counter = collections.defaultdict(int)
    for v in nums:
        counter[v] += 1
    counts = sorted(counter.values(), reverse=True)
    t = counts[k-1]
    return [k for k, v in counter.items() if v >= t]

print(topKFrequent([1,1,1,2,2,3], 2))


print("前K大元素")

import heapq
def maxKNums(nums, k):
    res = []
    for v in nums:
        heapq.heappush(res, v)
        if len(res) > k:
            heapq.heappop(res)
    return res

print(maxKNums([1,4,324,233,2, 3, 4,6,7], 2))