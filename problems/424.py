"""
424. 替换后的最长重复字符
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 10**4
"""
import collections
def characterReplacement(s, k):
    # 初始化保存 子串在区间内出现频次的dict
    num = collections.defaultdict(int)
    n = len(s)
    # 初始化 区间内单个字符频次的最大值, 左右指针
    max_char_count = left = right = 0
    while right < n:
        # 对当前出现的字符 频次+1
        num[s[right]] += 1
        # 对历史 字符批次最大值 和 当前字符批次比较
        max_char_count = max(max_char_count, num[s[right]])
        # 如果区间长度-区间内字符出现最大频次 大于 给定值, 则左指针向右移, 同时左侧字符频次-1
        if right - left + 1 - max_char_count > k:
            num[s[left]] -= 1
            left += 1
        # 循环结束时 右指针 向右移动
        right += 1
    # 由于right 额外加了1 所以 不需要-1 了
    return right - left

print(characterReplacement("ABAB", 2)) # 4
print(characterReplacement("AABABBA", 1)) # 4