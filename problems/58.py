"""
58. 最后一个单词的长度
"""

def lengthOfLastWord(s):
    n = len(s)
    if n == 0:
        return 0
    end = n - 1
    while end >= 0 and s[end] == " ":
        end -= 1
    start = end
    while start >= 0 and s[start] != " ":
        start -= 1
    return end - start


print(lengthOfLastWord("hello world"))

