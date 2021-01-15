"""
947. 移除最多的同行或同列石头
n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。

给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。

 

示例 1：

输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5
解释：一种移除 5 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。
示例 2：

输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：3
解释：一种移除 3 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。
示例 3：

输入：stones = [[0,0]]
输出：0
解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。
"""

# 88ms  15MB
def removeStones(stones):
    n = 10010
    father = {}

    def getFaterValue(x):
        if x not in father:
            father[x] = x
            return x
        return father[x]

    def find(x):
        if x != getFaterValue(x):
            father[x] = find(getFaterValue(x))
        return father[x]

    def merge(x, y):
        father[find(x)] = find(y)

    for x, y in stones:
        merge(x, y + 10010)

    res = set()
    for x, _ in stones:
        res.add(find(x))

    return len(stones) - len(res)

# 下面方法虽然简洁 但是内存过大  180ms 49.3MB
def other(stones):
    n = 10010
    father = {x: x for x in range(n * 2)}

    def find(x):
        if x != father[x]:
            father[x] = find(father[x])
        return father[x]

    def merge(x, y):
        father[find(x)] = find(y)

    for x, y in stones:
        merge(x, y + n)
    res = set()
    for x, _ in stones:
        res.add(find(x))

    return len(stones) - len(res)





stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(removeStones(stones))
print(other(stones))

stones = [[1,2],[1,3],[3,3],[3,1],[2,1],[1,0]]
print(removeStones(stones))
print(other(stones))


""""
解答这道题核心就是需要统计所给出的所有点 可以 分成多少组的查并集,  而每一个查并集 都可以最终保留一个, 总点数 - 查并集数量  就是结果了
所给出的两种方案 思路都是一样的, 区别在于, 一个全量初始化节点, 一个每次用到的时候才会去初始化节点, 优点在于当有一个比较长的列表来计算节点时 会节省时间和内存
"""