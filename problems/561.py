"""
561. 数组拆分 I
"""

def arrayPairSum(nums):
    sort_nums = sorted(nums)
    return sum(sort_nums[::2])

print(arrayPairSum([1,4,3,2]))
print(arrayPairSum([6,2,6,5,1,2]))



"""
面试题 01.04. 回文排列
"""

import collections
def canPermutePalindrome(s):
    # def isPalind(t):
    #     if not t:
    #         return True
    #     if t[0] == t[-1]:
    #         return isPalind(t[1:-1])
    #     return False

    queue = collections.defaultdict(int)
    for v in s:
        queue[v] ^= 1
    return sum(queue.values()) <= 1

def other(s):
    res = set()
    for v in s:
        if v in res:
            res.remove(v)
        else:
            res.add(v)
    return len(res) < 2



print(canPermutePalindrome("tactcoa")) # true
print(other("tactcoa")) # true


"""
566. 重塑矩阵
"""

def matrixReshape(nums, r, c):
    m = len(nums)
    n = len(nums[0])
    size = m * n
    if size != r * c:
        return nums
    # res = [[] for _ in range(r)]
    # count = 0
    # for l in nums:
    #     for v in l:
    #         res[count // c].append(v)
    #         count += 1
    # return res
    res = [[0] * c for _ in range(r)]
    for x in range(size):
        res[x // c][x % c] = nums[x // n][x % n]
    return res

print(matrixReshape([[1,2],[3,4]], 1, 4))