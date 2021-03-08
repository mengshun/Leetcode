"""
131 分割回文串
https://leetcode-cn.com/problems/palindrome-partitioning/
"""

def partition(s):
    res = []

    # 回文串判定
    def isPalindrome(ts):
        if not ts:
            return True
        if ts[0] != ts[-1]:
            return False
        return isPalindrome(ts[1:-1])
    # 回溯
    def backtrack(ts, path):
        if not ts:
            res.append(path)
            return
        n = len(ts)
        for i in range(1, n + 1):
            if isPalindrome(ts[:i]):
                backtrack(ts[i:], path + [ts[:i]])

    backtrack(s, [])

    return res



print(partition("ccaab"))


t = "ab"
res = [""]
for v in t:
    res += [v + x for x in res]
print(res)

t = [1,2]
res = [[]]
for v in t:
    res += [[v] + x for x in res]

print(res)




"""
5 最长回文串
"""

def maxlengths(s):
    n = len(s)
    if n < 2:
        return s
    # 前闭后闭区间 dp[i][j] i 到 j 是否是回文串 i <= j
    dp = [[False] * n for _ in range(n)]
    # 只有一个元素时 一定为真
    for i in range(n):
        dp[i][i] = True
    # 记录最长串的左右
    left = right = 0
    for j in range(1, n):
        # i <= j
        for i in range(j):
            # 第一个元素和最后一个元素一样
            if s[i] == s[j]:
                # 区间长度小于或等于3
                if j - i < 3:
                    dp[i][j] = True
                else:
                    # 区间长度大于3时 获取其内部区间值
                    dp[i][j] = dp[i+1][j-1]
            # 记录最长子串区间
            if dp[i][j] and j - i > right - left:
                left, right = i, j
    return s[left:right+1]
print(maxlengths("abcbad"))


"""
132. 分割回文串 II
https://leetcode-cn.com/problems/palindrome-partitioning-ii/
"""

# 暴力超时
def minCut(s):
    isPlindrome = lambda x: x == x[::-1]
    def backtrack(ts, r, path):
        if not ts:
            r.append(path)
        for i in range(1, len(ts) + 1):
            if isPlindrome(ts[:i]):
                backtrack(ts[i:], r, path + 1)
    res = []
    backtrack(s, res, -1)
    return min(res)

# dp

def minCut2(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    min_s = [n] * n
    for j in range(n):
        for i in range(j + 1):
            if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                dp[i][j] = True
                if i == 0:
                    min_s[j] = 0
                else:
                    min_s[j] = min(min_s[j], min_s[i-1] + 1)
    return min_s[-1]

def minCut3(s):
    n = len(s)
    dp = [n] * n
    isPlindrome = lambda x: x == x[::-1]
    for j in range(n):
        if isPlindrome(s[:j+1]):
            dp[j] = 0
        for i in range(j):
            if isPlindrome(s[i+1:j+1]):
                dp[j] = min(dp[j], dp[i-1] + 1)
    return dp[-1]

print(minCut("aab"))
print(minCut2("aaccb"))
print(minCut2("ababababababababababababcbabababababababababababa"))