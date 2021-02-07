"""
1423. 可获得的最大点数   难度: 中等
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。
"""

def maxScore(cardPoints, k):
    n = len(cardPoints)

    def min_deal():
        sum_v = sum(cardPoints)
        count = n - k + 1
        begin = n - k
        t = sum(cardPoints[:begin])
        min_v = t
        for i in range(1, k+1):
            t = t - cardPoints[i-1] + cardPoints[begin + i - 1]
            print(t)
            min_v = min(min_v, t)
        return sum_v - min_v

    def huadong_deal():
        sum_v = sum(cardPoints[:k])
        res = sum_v
        for i in range(1, k+1):
            sum_v = sum_v - cardPoints[k-i] + cardPoints[n - i]
            res = max(res, sum_v)
        return res


    if (n >> 1) > k:
        # k值 小于 一半数据   直接求k个数的和
        return huadong_deal()
    else:
        # 求 除去k个数之外的最小值
        return min_deal()

# print(maxScore([1,2,3,4,5,6,1], 3)) # 12
# print(maxScore([9,7,7,9,7,7,9], 7))
print(maxScore([96,90,41,82,39,74,64,50,30], 8)) # 536

