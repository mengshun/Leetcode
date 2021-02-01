"""
839. 相似字符串组

"""

class UnionFind:
    def __init__(self, n):
        self.father = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.father[x] = y
        self.size[y] += self.size[x]
        self.count -= 1

def numSimilarGroups(strs):

    #检查是否具有相似性
    def checkStr(a, b):
        count = 0
        for x, y in zip(a, b):
            if x != y:
                count += 1
                if count > 2:
                    return False
        return True

    n = len(strs)
    uf = UnionFind(n)
    for i in range(n-1):
        for j in range(i + 1, n):
            if checkStr(strs[i], strs[j]):
                uf.merge(i, j)

    return uf.count



print(numSimilarGroups(["tars","rats","arts","star"])) # 2
print(numSimilarGroups(["omv","ovm"])) # 1

"""
看完题目意思是,可以分多少组, 每个组里面的每个元素在他自己组内总能找到一个与他相似的, 在其他组无法找到, 
所以并查集来解决, 每个元素当做一个点, 所有相似的可以连线, 最终看 有多少个连通分量
"""
