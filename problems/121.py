"""
121. 买卖股票的最佳时机
"""

def maxProfit(prices):
    n = len(prices)
    res = [0] * n # res[i] 表示第i天的 最大利润, 没有利润为0
    dp = [0] * n
    dp[0] = prices[0] # dp[i] 表示从0到i之间 含i 的最小值
    for i in range(1, n):
        dp[i] = min(prices[i], dp[i-1])
        res[i] = max(0, prices[i] - dp[i-1])
    return max(res)

def maxProfit2(prices):
    n = len(prices)
    if n < 2:
        return 0
    min_money =  prices[0]
    res = 0
    for v in prices[1:]:
        res = max(res, v - min_money)
        min_money = min(v, min_money)
    return res


print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit2([7,1,5,3,6,4])) # 5



"""
152  乘积最大子数组
"""

def maxProduct(nums):
    n = len(nums)
    if n < 1:
        return 0
    dp_min = [nums[0]]
    dp_max = [nums[0]]
    for v in nums[1:]:
        if v > 0:
            min_v, max_v = min(v, dp_min[-1] * v), max(v, dp_max[-1] * v)
            dp_min.append(min_v)
            dp_max.append(max_v)
        else:
            min_v, max_v = min(v, dp_max[-1] * v), max(v, dp_min[-1] * v)
            dp_min.append(min_v)
            dp_max.append(max_v)
    return max(dp_max)


print(maxProduct([2,3,-2,4])) # 6
print(maxProduct([-2, 0, -1])) # 0


"""
697 数组的度
"""
import collections
def findShortestSubArray(nums):
    n = len(nums)
    if n < 2:
        return n
    count_dp = collections.defaultdict(int)
    dp_indexs = collections.defaultdict(list)
    for i, v in enumerate(nums):
        count_dp[v] += 1
        dp_indexs[v].append(i)

    max_count = max(count_dp.values())
    if max_count == 1:
        return 1
    res = float('inf')
    for k, v in count_dp.items():
        if v == max_count:
            indexs = dp_indexs[k]
            res = min(indexs[-1] - indexs[0] + 1, res)
    return res




print(findShortestSubArray([1, 2, 2, 3, 1])) # 2
print(findShortestSubArray([1,2,2,3,1,4,2])) # 6
