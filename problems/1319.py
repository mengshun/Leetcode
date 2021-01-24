"""
1319. 连通网络的操作次数
用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。
"""

class UnionFinder:
    def __init__(self, n):
        self.father = [x for x in range(n)]
        self.count = n

    def find(self, x):
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]
    def merge(self, x, y):
        findx = self.find(x)
        findy = self.find(y)
        if findx != findy:
            self.father[findx] = findy
            self.count -= 1



def makeConnected(n, connections):
    #线的条数必须至少是 n-1 条 才有可能链接成功
    if len(connections) < n-1:
        return -1

    uf = UnionFinder(n)
    for x, y in connections:
        uf.merge(x, y)

    return uf.count - 1
"""
首先需要明白一点, 如果有n台机器, 至少需要n-1条网线才能全部连通, 所以, 如果不满足n-1条网线直接返回-1
其次很容易想到使用并查集的连通分量来解决, 我们需要知道所给的线一共有多少组是已经连通的, 设这个是x组连通的, 呢么至少还需要x-1条网线才能连接成功
"""

print(makeConnected(4, [[0,1],[0,2],[1,2]])) # 1
print(makeConnected(5, [[0,1],[0,2],[3,4],[2,3]])) # 0