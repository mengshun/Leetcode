"""
338. 比特位计数
https://leetcode-cn.com/problems/counting-bits/
"""

global res
res = []
def countBits(num):
    global res
    n = len(res)
    if num < n:
        return res[:num+1]
    for v in range(n, num + 1):
        res.append(bin(v).count("1"))
    return res


print(countBits(2))
print(countBits(5))

# 数的二进制有多少个1
x = 10
count = 0
while x > 0:
    x &= (x-1)
    count += 1
print(count)

# 二进制翻转
print("二进制翻转")


def reverseBinary(num):
    res = 0
    cur = num
    count = 31
    while cur > 0:
        res += (cur & 1) << count
        cur >>= 1
        count -= 1
    return res
x = 11
res = reverseBinary(x)
print(x, res, bin(x), bin(res))
x = 0b00000010100101000001111010011100
res = reverseBinary(x)
print(x, res, bin(x), bin(res))
x = 0b11111111111111111111111111111101
res = reverseBinary(x)
print(x, res, bin(x), bin(res))
print("\n")
def reverseBits(n):
    m1 = 0x55555555 # 1位交换
    m2 = 0x33333333 # 2位交换
    m3 = 0x0f0f0f0f # 4位交换
    m4 = 0x00ff00ff # 8位交互
    m5 = 0x0000ffff # 16位交换
    # 不修改原数
    num = n
    num = num >> 1 & m1 | (num & m1) << 1
    num = num >> 2 & m2 | (num & m2) << 2
    num = num >> 4 & m3 | (num & m3) << 4
    num = num >> 8 & m4 | (num & m4) << 8
    num = num >> 16 & m5 | (num & m5) << 16
    return num
    # python 语言 num 左移16位 会超过 32位有效值
    # return num >> 16 | num << 16

x = 11
res = reverseBits(x)
print(x, res, bin(x), bin(res))

x = 0b00000010100101000001111010011100
res = reverseBits(x)
print(x, res, bin(x), bin(res))
x = 0b11111111111111111111111111111101
res = reverseBits(x)
print(x, res, bin(x), bin(res))
