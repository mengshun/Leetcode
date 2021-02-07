"""
1208. 尽可能使字符串相等
给你两个长度相同的字符串，s 和 t。

将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。

如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
"""

def equalSubstring(s, t, maxCost):
    n = len(s)
    diff = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
    maxLength = start = end = 0
    total = 0
    while end < n:
        total += diff[end]
        while total > maxCost:
            total -= diff[start]
            start += 1

        maxLength = max(maxLength, end - start + 1)
        end += 1
    return maxLength

print(equalSubstring("abcd", "bcdf", 3)) # 3
print(equalSubstring("abcd", "cdef", 3)) # 1
print(equalSubstring("abcd", "acde", 0)) # 1