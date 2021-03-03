"""
567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False
"""

# 暴力解法 超时
def checkInclusion(s1, s2):

    # 求出 s1 所有的组合
    def zuhe(l):
        if len(l) == 1:
            return [l]
        res = []
        for i in range(len(l)):
            start = l[i:i + 1]
            other = l[:i] + l[i + 1:]
            res.extend([start + v for v in zuhe(other)])
        return res

    res = zuhe(list(s1))
    res = ["".join(v) for v in res]
    for v in res:
        if v in s2:
            return True
    return False

print(checkInclusion("ab", "eidbaooo"))
"""
"prosperity"
"properties"
"""

# import time
# begin = time.time()
# print(checkInclusion("prosperity", "properties"))
# end = time.time()
# print(end - begin)

import collections

def haxi(s1, s2):

    n1 = len(s1)
    n2 = len(s2)
    if n1 > n2:
        return False

    s1_count = collections.defaultdict(int)
    for v in s1:
        s1_count[v] += 1

    s2_list = list(s2)
    s2_count = collections.defaultdict(int)

    n = 0
    while n < n2:
        cur = s2_list[n]
        s2_count[cur] += 1
        if n >= n1:
            s2_count[s2_list[n - n1]] -= 1
        if len(s1_count) <= len(s2_count) and cur in s1_count:
            flag = True
            for k, v in s1_count.items():
                if s2_count[k] != v:
                    flag = False
                    break
            if flag:
                return True
        n += 1
    return False



print(haxi("a", "ab"))





