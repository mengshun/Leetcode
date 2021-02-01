"""
1518. 换酒问题
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

请你计算 最多 能喝到多少瓶酒。
"""


def numWaterBottles(numBottles, numExchange):
    if numBottles < numExchange:
        return numBottles
    # 一共喝了多少
    res = numBottles
    # 剩余空瓶子
    empty = numBottles
    while empty // numExchange > 0:
        #兑换的新瓶子
        new_bottles = empty // numExchange
        #新瓶子 全喝掉
        res += new_bottles
        #新瓶子喝完 + 原来兑换剩余的空瓶子
        empty = empty % numExchange + new_bottles

    return res


print(numWaterBottles(9, 3)) #13
