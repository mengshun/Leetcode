"""
1178. 猜字谜
"""

# 暴力 超时
def findNumOfValidWords(words, puzzles):
    words_list = []
    for v in words:
        words_list.append(set(list(v)))

    puzzles_list = [set(list(v)) for v in puzzles]

    def findNum(s_list, s):
        count = 0
        for l in words_list:
            if s[0] in l:
                count += 1
                for word in l:
                    if word not in s_list:
                        count -= 1
                        break
        return count

    return [findNum(s_list, s) for s_list, s in zip(puzzles_list, puzzles)]


# 状态压缩 + 子集

import collections
def binaryNums(words, puzzles):
    frequency = collections.Counter()
    for word in words:
        mask = 0
        for c in word:
            mask |= (1 << (ord(c) - ord('a')))
        if str(bin(mask)).count("1") <= 7:
            frequency[mask] += 1

    def ziji(w):
        res = [""]
        for v in w:
            res += [v + x for x in res]
        return res

    res = []
    for p in puzzles:
        total = 0
        for perm in ziji(p[1:]):
            mask = 1 << (ord(p[0]) - ord('a'))
            for c in perm:
                mask |= (1 << ord(c) - ord('a'))
            total += frequency[mask]
        res.append(total)
    return res
def binaryNums2(words, puzzles):
    frequency = collections.Counter()
    for word in words:
        mask = 0
        for c in set(list(word)):
            mask |= (1 << (ord(c) - ord('a')))
        frequency[mask] += 1

    def ziji(w):
        res = [[]]
        for v in set(list(w)):
            res += [[v] + x for x in res]
        return res

    res = []
    for p in puzzles:
        total = 0
        for perm in ziji(p[1:]):
            mask = 1 << (ord(p[0]) - ord('a'))
            for c in perm:
                mask |= (1 << ord(c) - ord('a'))
            total += frequency[mask]
        res.append(total)
    return res

words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
print(findNumOfValidWords(words, puzzles)) # [1,1,3,2,4,0]
print(binaryNums(words, puzzles)) # [1,1,3,2,4,0]
print(binaryNums2(words, puzzles)) # [1,1,3,2,4,0]



# 子集

def subsets(nums):
    res = [[]]
    for i in nums:
        res += [[i] + v for v in res]
    return res

print(subsets([1, 2, 3]))
print(subsets([1, 2]))
print(subsets([1]))
print(str(bin(3)).count("1"))