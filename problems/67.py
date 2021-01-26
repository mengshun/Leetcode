"""
67 二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。
"""



def addBinary(a, b):
    if len(a) < len(b):
        a, b = b, a
    a = [int(v) for v in a]
    b = [int(v) for v in b]

    for i in range(1, len(b) + 1):
        res = a[-i] + b[-i]
        if res < 2:
            a[-i] = res
            continue
        a[-i] = 0
        flag = 1
        n = len(a)
        start = i + 1
        while n >= start and flag == 1:
            if a[-start] == 1:
                a[-start] = 0
            else:
                a[-start] = 1
                flag = 0
            start += 1
        if flag == 1:
            a.insert(0, 1)

    return "".join([str(v) for v in a])





print(int("111", 2))


print(addBinary("11", "1"))







print("============其他训练==============")

# a,b 拼接后 求值 (a, b 均为二进制字符串)
def sumBinary(a, b):
    def transform(s):
        if len(s) == 0:
            return 0
        x = 1
        res = 0
        for i in range(1, len(s)+1):
            res += int(s[-i]) * x
            x = x * 2
        return res

    return transform(a) * (2**len(b)) + transform(b)



print(sumBinary("11", "1"))





def addToArrayForm(A, K):
    n = len(A) - 1
    while K != 0:
        res = A[n] + K
        K, A[n] = res // 10, res % 10
        n -= 1
        if n == -1 and K != 0:
            A.insert(0, 0)
            n = 0
    return A

print(addToArrayForm([1, 2, 0, 0], 111))

