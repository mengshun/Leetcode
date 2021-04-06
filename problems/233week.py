"""
5709. 最大升序子数组和
"""

def maxAscendingSum(nums):
    if not nums:
        return 0
    queue = [nums[0]]
    res = 0
    for v in nums[1:]:
        if v > queue[-1]:
            queue.append(v)
        else:
            res = max(res, sum(queue))
            queue = [v]
    res = max(res, sum(queue))
    return res




nums = [12,17,15,13,10,11,12]
print(maxAscendingSum(nums)) # 33


"""
积压订单的总数量
"""

import heapq
def getNumberOfBacklogOrders(orders):
    k = 10 ** 9 + 7
    buy_res = []
    sell_res = []
    for price, amount, orderType in orders:
        if orderType == 0:
            # 买
            while amount > 0 and sell_res and sell_res[0][0] <= price:
                amount = amount - sell_res[0][1]
                if amount >= 0:
                    heapq.heappop(sell_res)
                else:
                    sell_res[0][1] = -amount
            if amount > 0:
                heapq.heappush(buy_res, [-price, amount])
        else:
            # 卖
            while amount > 0 and buy_res and -buy_res[0][0] >= price:
                amount = amount - buy_res[0][1]
                if amount >= 0:
                    heapq.heappop(buy_res)
                else:
                    buy_res[0][1] = -amount
            if amount > 0:
                heapq.heappush(sell_res, [price, amount])
    return (sum([amount for _, amount in buy_res]) + sum([amount for _, amount in sell_res])) % k


# orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
# res = getNumberOfBacklogOrders(orders)
# print(res, res == 6)
#
# orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
# res = getNumberOfBacklogOrders(orders)
# print(res, res == 999999984)

orders = [[19,28,0],[9,4,1],[25,15,1]]
res = getNumberOfBacklogOrders(orders)
print(res, res == 39)


# 有界数组中指定下标处的最大值
"""
示例 1：

输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
示例 2：

输入：n = 6, index = 1,  maxSum = 10
输出：3
2 3 2 1 1 1 
6+1 = 7
7+3 = 10
 
"""

def maxValue(n, index, maxSum):
    if maxSum <= n + 1:
        return maxSum - n + 1
    left = right = index
    current_sum = n
    res = 2
    while current_sum < maxSum:
        if left > 0:
            left -= 1
        if right < n - 1:
            right += 1
        current_sum += (right - left + 1)
        if current_sum == maxSum:
            break
        res += 1

    return res if current_sum == maxSum else res - 1

print(maxValue(4, 2, 6)) # 2
print(maxValue(6, 1, 10)) # 3
print(maxValue(1, 0, 24)) # 24
