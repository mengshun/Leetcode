"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
"""

def myPow(x, n):
    return x ** n

def myPow2(x, n):
    if x == 0.0:
        return 0.0
    if n < 0:
        # 如果为负幂次 则转换为正的
        x, n = 1 / x, -n
    res = 1
    while n:
        if n & 1:
            # 判定n的二进制位最后一位是否是1
            res *= x
        x *= x
        # 移出已经计算过得最后一位
        n >>= 1
    return res


print(myPow(2.0, 10))
print(myPow(2.1, 3))
print(myPow(2.0, -2))
print(myPow2(2.0, 10))
print(myPow2(2.1, 3))
print(myPow2(2.0, -2))