"""
995. K 连续位的最小翻转次数
"""


# 模拟翻转 会超时
def minKBitFlips(A, K):
    n = len(A)
    res = 0
    for i in range(n - K + 1):
        if A[i] == 1:
            continue
        for j in range(K):
            A[i + j] ^= 1
        res += 1
    for i in range(n):
        if A[i] ^ 1 == 1:
            return -1
    return res

import collections
# 滑动
def huadong(A, K):
    n = len(A)
    queue = collections.deque()
    res = 0
    for i in range(n):
        if queue and i >= queue[0] + K:
            queue.popleft()
        if len(queue) % 2 == A[i]:
            if i + K > n:
                return -1
            queue.append(i)
            res += 1
    return res



print(minKBitFlips([0, 0, 0, 0], 2))
print(huadong([0, 0, 0, 0], 2))


"""
319 灯泡开关
"""

def bulbSwitch(n):
    if n == 1:
        return 1
    res = 1
    while True:
        if res * res > n:
            break
        res += 1
    return res - 1

import math
def bulbSwitchMath(n):
    return int(math.sqrt(n))


# 位置索引的 因数个数为奇数 则为开, 偶数为关  完全平方数 满足这个条件
print(bulbSwitch(3))
print(bulbSwitchMath(3))