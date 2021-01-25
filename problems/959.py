"""
959. 由斜杠划分区域
"""

class UnionFind:
    def __init__(self, n):
        self.father = {x:x for x in range(n)}
        #连通分量统计
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

def regionsBySlashes(grid):
    n = len(grid)
    uf = UnionFind(n * n * 4)
    for i in range(n):
        for j in range(n):
            cur = grid[i][j]
            start = 4 * (i * n + j)
            if cur == "/":
                uf.merge(start, start + 3)
                uf.merge(start + 1, start + 2)
            elif cur == "\\":
                uf.merge(start, start + 1)
                uf.merge(start + 3, start + 2)
            elif cur == " ":
                uf.merge(start, start + 1)
                uf.merge(start + 1, start + 2)
                uf.merge(start + 2, start + 3)

            if j > 0:
                uf.merge(start + 3, start - 3)
            if i > 0:
                uf.merge(start, start - 4 * n + 2)

    return uf.count



print(regionsBySlashes([" /", "/ "])) #2
print(regionsBySlashes(["/\\", "\\/"])) #5