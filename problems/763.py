"""
763. 划分字母区间 https://leetcode-cn.com/problems/partition-labels/
"""
import collections
def partitionLabels(S):
    n = len(S)
    if n < 2:
        return 1

    def backtrace(s):
        length = len(s)
        idxMap = collections.defaultdict(int)
        for i in range(length):
            idxMap[s[i]] = max(idxMap[s[i]], i)

        left, right = 0, idxMap[s[0]]
        while left != right:
            if right == length:
                return length
            if s[left] != s[right]:
                right = max(idxMap[s[left]], right)
            left += 1
        return right + 1


    count = 0
    res = []
    while count < n:
        t = backtrace(S[count:])
        res.append(t)
        count += t
    return res


def partitionLabelsOther(S):
    idxMap = collections.defaultdict(int)
    n = len(S)
    for i in range(n):
        idxMap[S[i]] = i
    start = 0
    res = []
    right = 0
    for i in range(n):
        cur = S[i]
        maxIdx = idxMap[cur]
        right = max(maxIdx, right)
        if i == right:
            res.append(right-start+1)
            start = i + 1
    return res


print(partitionLabels("ababcbacadefegdehijhklij"))
print(partitionLabelsOther("ababcbacadefegdehijhklij"))
print(partitionLabelsOther("ababcbacadefegdehijhklijzxy"))
print(partitionLabels("hijhklij"))
