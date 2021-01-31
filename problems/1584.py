"""
1584. 连接所有点的最小费用
给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。

连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
"""

def minCostConnectPoints(points):

    n = len(points)
    if n < 2:
        return 0
    father = list(range(n))
    rank = [1] * n

    def find(x):
        if x != father[x]:
            father[x] = find(father[x])
        return father[x]

    def merge(x, y):
        x, y = find(x), find(y)
        if x == y:
            return False
        if rank[x] > rank[y]:
            x, y = y, x
        rank[y] += rank[x]
        father[x] = y
        return True

    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])

    edges.sort()
    res = count = 0
    for v, x, y in edges:
        if merge(x, y):
            res += v
            count += 1
            if count == n - 1:
                break
    return res





print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) # 20
print(minCostConnectPoints([[3,12],[-2,5],[-4,1]])) # 18

