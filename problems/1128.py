"""
1128. 等价多米诺骨牌对的数量
"""

def numEquivDominoPairs(dominoes):
    dp = {}
    count = 0
    for x, y in dominoes:
        key = (x, y)
        if x > y:
            key = (y, x)
        if key in dp:
            dp[key] += 1
        else:
            dp[key] = 0
        count += dp[key]
    return count

import collections
def numEquivDominoPairs2(dominoes):
    dp = collections.defaultdict(int)
    count = 0
    #由于元素的值在1-9之间 故可以求一个唯一值
    for x, y in dominoes:
        val = 10*x + y
        if x > y:
            val = 10*y+x
        count += dp[val]
        dp[val] += 1
    return count




# print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
print(numEquivDominoPairs2([[1,2],[1,2],[1,1],[1,2],[2,2]]))