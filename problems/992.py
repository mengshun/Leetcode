"""
992. K 个不同整数的子数组
https://leetcode-cn.com/problems/subarrays-with-k-different-integers/
"""

# 暴力解法  时间复杂度高
def subarraysWithKDistinct(A, K):
    t = set(A)
    if len(t) < K:
        return 0
    n = len(A)
    res = 0
    for i in range(n-K+1):
        tmp = set(A[i:i+K])
        if len(tmp) == K:
            res += 1
        begin = i + K
        while begin < n:
            tmp.add(A[begin])
            if len(tmp) == K:
                res += 1
            elif len(tmp) > K:
                break
            begin += 1
    return res

import collections
def subarraysWithKDistinct2(A, K):
    n = len(A)
    num1, num2 = collections.Counter(), collections.Counter()
    total1 = total2 = 0
    left1 = left2 = right = 0
    res = 0
    for right, num in enumerate(A):
        if num1[num] == 0:
            total1 += 1
        num1[num] += 1
        if num2[num] == 0:
            total2 += 1
        num2[num] += 1

        while total1 > K:
            num1[A[left1]] -= 1
            if num1[A[left1]] == 0:
                total1 -= 1
            left1 += 1
        while total2 > K - 1:
            num2[A[left2]] -= 1
            if num2[A[left2]] == 0:
                total2 -= 1
            left2 += 1

        res += left2 - left1
    return res





print(subarraysWithKDistinct([1,2,1,2,3], 2) )# 7
print(subarraysWithKDistinct([1,2,1,3,4], 3) )# 3
print(subarraysWithKDistinct([2,1,1,1,2], 1) )# 8
print(subarraysWithKDistinct([2,2,1,2,2,2,1,1], 2)) # 23

print(subarraysWithKDistinct2([1,2,1,2,3], 2) )# 7
# print(subarraysWithKDistinct2([1,2,1,3,4], 3) )# 3
# print(subarraysWithKDistinct2([2,1,1,1,2], 1) )# 8
# print(subarraysWithKDistinct2([2,2,1,2,2,2,1,1], 2)) # 23