"""
14. 最长公共前缀
https://leetcode-cn.com/problems/longest-common-prefix/
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""

    def findPrefix(p, s):
        length, i = min(len(p), len(s)), 0
        while i < length:
            if p[i] == s[i]:
                i += 1
            else:
                break
        return p[:i]

    prefix = strs[0]
    for v in strs[1:]:
        prefix = findPrefix(prefix, v)
        if not prefix:
            return ""
    return prefix


print(longestCommonPrefix(["flower","flow","flight"]))