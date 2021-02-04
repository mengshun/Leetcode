"""
556. 下一个更大元素 III
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
"""

# 1 <= 你<= (2 << 32) - 1
def nextGreaterElement(n):

    s = str(n)
    strs = list(s)
    end = len(strs) - 1
    last = len(strs) - 1

    def deal(t):
        res = "".join(t)
        res = int(res)
        if res >= 0 and res < (2 << 32):
            return res
        return -1

    while end >= 0:
        if strs[end] >= strs[last]:
            if last == 0:
                print("递减序列")
                return -1
        else:
            for i in range(len(strs)-1, end, -1):
                if strs[i] > strs[end]:
                    strs[i], strs[end] = strs[end], strs[i]
                    t = strs[:end + 1] + sorted(strs[ end + 1 :])
                    return deal(t)
        last = end
        end -= 1
    print("没有找到解决方案")
    return -1


print(nextGreaterElement(12))
print(nextGreaterElement(230241)) # 230412