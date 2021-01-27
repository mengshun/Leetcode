"""
1579. 保证图可完全遍历
"""

class UnionFind:
    def __init__(self, n):
        # 用列表省时间和内存
        self.father = list(range(n+1))
        self.count = n
        # 记录分支大小, 合并时吧小的合并到大的分支上, 提高效率
        self.size = [1] * (n+1)

    def find(self, x):
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        if self.size[x] < self.size[y]:
            x, y = y, x

        self.size[x] += self.size[y]
        self.father[y] = x
        self.count -= 1
        return True


def maxNumEdgesToRemove(n, edges):
    uf1 = UnionFind(n)
    uf2 = UnionFind(n)
    ans = 0

    for type, x, y in edges:
        if type == 3:
            if not uf1.merge(x, y):
                ans += 1
            else:
                uf2.merge(x, y)

    for type, x, y in edges:
        if type == 1:
            if not uf1.merge(x, y):
                ans += 1
        elif type == 2:
            if not uf2.merge(x, y):
                ans += 1

    if uf1.count != 1 or uf2.count != 1:
        return -1

    return ans



print(maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))# 2


"""
理解题目意思, 通俗的讲就是把类型3的连线 分别添加到类型1 和 类型2 后, 类型1,2都得是只有一个连通分量, 在这个大前提下, 如何尽可能去除多的连线, 而不影响这个结果.
1. 我们需要2个独立的并查集
2. 向2个并查集添加 相同的类型3的数据, 如果发现类型3 自身存在无用路径, 则结果count+1
3. 类型3数据遍历完成后, 开始分别向独立并查集添加数据, 同第二条一样, 发现无用路径, 结果 count+1
4. 全部添加完成, 需要先判定结果是否合法, 2个独立并查集是否真的只有1个连通分量, 存在任何一个大于1时, 直接返回-1
5. 最终返回 count
"""