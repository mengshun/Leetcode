"""
803. 打砖块
有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：

一块砖直接连接到网格的顶部，或者
至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。

返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。

注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

示例 1：

输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
输出：[2]
解释：
网格开始为：
[[1,0,0,0]，
 [1,1,1,0]]
消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0]
 [0,1,1,0]]
两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
[[1,0,0,0],
 [0,0,0,0]]
因此，结果为 [2] 。
示例 2：

输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
输出：[0,0]
解释：
网格开始为：
[[1,0,0,0],
 [1,1,0,0]]
消除 (1,1) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [1,0,0,0]]
剩下的砖都很稳定，所以不会掉落。网格保持不变：
[[1,0,0,0],
 [1,0,0,0]]
接下来消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [0,0,0,0]]
剩下的砖块仍然是稳定的，所以不会有砖块掉落。
因此，结果为 [0,0] 。

提示:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] 为 0 或 1
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
所有 (xi, yi) 互不相同
"""

# #并查集  官方解释  用例执行可能有问题 下方有自己写的
# class UnionFind:
#     def __init__(self, n):
#         self.father = list(range(n))
#         self.size = [1] * n
#
#     #路径压缩，只要求每个不相交集合的「根结点」的子树包含的结点总数数值正确即可，因此在路径压缩的过程中不用维护数组 size
#     def merge(self, x, y):
#         x, y = self.find(x), self.find(y)
#         if x == y:
#             return
#         self.father[x] = y
#         self.size[y] += self.size[x]
#
#     def get_current_size(self, x):
#         return self.size[self.find(x)]
#
#     def find(self, x):
#         if x != self.father[x]:
#             self.father[x] = self.find(self.father[x])
#         return self.father[x]
#
# def hitBricks2(grid, hits):
#     rows = len(grid)
#     cols = len(grid[0])
#
#     def get_idx(x, y):
#         return x * rows + y
#
#     def is_in_area(x, y):
#         return x >= 0 and y >= 0 and x < rows and y < cols
#
#     #1. 把grid中的砖头全部敲碎, 通常算法问题不能修改原数据, 所以需要 copy一份
#     copy_grid = [[v for v in rowData] for rowData in grid]
#     # import copy
#     # copy.deepcopy(grid)
#     # 把copy的砖头敲碎
#     for x, y in hits:
#         copy_grid[x][y] = 0
#
#     #2 建图 吧砖块和砖块的关系输入并查集 size 表示二维网格的大小 也表示虚拟屋顶并查集的编号
#     size = rows * cols
#     finder = UnionFind(size + 1)
#
#     #先将下标为1 的与屋顶相连
#     for i, v in enumerate(copy_grid[0]):
#         if v == 1:
#             finder.merge(i, size)
#
#     #其余网格，如果是砖块向上、向左看一下，如果也是砖块，在并查集中进行合并
#     for i in range(1, rows):
#         for j in range(cols):
#             if copy_grid[i][j] == 1:
#                 #如果上方也是砖块
#                 if copy_grid[i - 1][j] == 1:
#                     finder.merge(get_idx(i-1, j), get_idx(i, j))
#                 #如果左侧也是砖块
#                 if j > 0 and copy_grid[i][j - 1] == 1:
#                     finder.merge(get_idx(i, j - 1), get_idx(i, j))
#
#     #3 按照hits 逆序 在 copy中 补回砖块, 把每一次因为补回砖块而与屋顶相连的砖块的增量记录到 res 数组中
#     hits_length = len(hits)
#     res = [0] * hits_length
#     for i in range(hits_length-1, -1, -1):
#         x = hits[i][0]
#         y = hits[i][1]
#         # 注意：这里不能用copy，语义上表示，如果原来在grid中，这一块是空白，这一步不会产生任何砖块掉落
#         # 逆向补回的时候，与屋顶相连的砖块数量也肯定不会增加
#         if grid[x][y] == 0:
#             continue
#         #补回之前与屋顶相连的砖块数
#         origin = finder.get_current_size(size)
#         #注意：如果补回的这个结点在第 1 行，要告诉并查集它与屋顶相连（逻辑同第 2 步）
#         if x == 0:
#             finder.merge(y, size)
#
#         for xc, yc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
#             newx = x + xc
#             newy = y + yc
#             if is_in_area(newx, newy) and copy_grid[newx][newy] == 1:
#                 finder.merge(get_idx(x, y), get_idx(newx, newy))
#
#         # 补回之后与屋顶相连的砖块数
#         current = finder.get_current_size(size)
#         # 减去的1是逆向补回的砖块（正向移除的砖块），与0比较大小，是因为存在一种情况，添加当前砖块，不会使得与屋顶连接的砖块数更多
#         res[i] = max(0, current - origin - 1)
#         copy_grid[x][y] = 1
#     return res

# 深度优先思路
def hitBricks(grid, hits):
    m, n = len(grid), len(grid[0])
    ans = [-1] * len(hits)

    def dfs(x, y):
        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
            grid[x][y] = 2
            ans = 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
            return ans
        return 0

    def is_stable(x, y):
        if x == 0: return True
        if x + 1 < m and grid[x + 1][y] == 2: return True
        if x - 1 >= 0 and grid[x - 1][y] == 2: return True
        if y + 1 < n and grid[x][y + 1] == 2: return True
        if y - 1 >= 0 and grid[x][y - 1] == 2: return True
        return False

    # 模拟最终的残局
    for x, y in hits:
        grid[x][y] -= 1
    # 标记稳定砖块。 注意不标记被打掉的砖块，因此这一步需要在“模拟最终的残局”之后
    for y in range(n):
        dfs(0, y)
    # 倒推
    for i in range(len(hits) - 1, -1, -1):
        x, y = hits[i]
        grid[x][y] += 1
        # 如果不稳定，打掉也没啥影响
        if not is_stable(x, y) or grid[x][y] == 0:
            ans[i] = 0
        else:
            # 否则 dfs 计算联通图大小，这里的联通指的是值为 1。
            # 实际指的是添加了 (x,y) 砖块之后，这些值为 1 的砖块会变成稳定砖块（我们用 2 表示）
            # 由于我们是反推，因此就是移除 (x, y) 砖块之后， 这些稳定的砖块会变成不稳定（掉落）
            ans[i] = dfs(x, y) - 1
    return ans

# 并查集思路

class UnionFinder:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        self.parent[x] = y
        self.size[y] += self.size[x]
    def get_size(self, x):
        return self.size[self.find(x)]

def hitBricks3(grid, hits):
    m, n = len(grid), len(grid[0])
    size = m * n
    grid_copy = [[v for v in t] for t in grid]
    for x, y in hits:
        grid_copy[x][y] = 0
    # 多加1 是 由于 多了一个顶, 将第一行的 有砖块的与顶相连接
    uf = UnionFinder(size + 1)

    for i in range(m):
        for j in range(n):
            if grid_copy[i][j] == 1:
                if i == 0:
                    # 与顶连接
                    uf.merge(j, size)
                else:
                    # 其余部分的 连接情况
                    #向上连接
                    if grid_copy[i-1][j] == 1:
                        uf.merge(i*n + j, (i-1)*n + j)
                    #向左连接
                    if j > 0 and grid_copy[i][j-1] == 1:
                        uf.merge(i*n + j, i*n + j - 1)

    res = [0] * len(hits)
    # 倒序
    for i in range(len(hits) - 1, -1, -1):
        #如果原位置就没有砖块 此次击碎 无效
        x, y = hits[i]
        if grid[x][y] == 0:
            continue
        # 补上砖块
        grid_copy[x][y] = 1
        origal_size = uf.get_size(size)
        #对上下左右进行一个连线
        current_idx = x * n + y
        #如果是第一行 还需要额外与顶部连接
        if x == 0:
            uf.merge(current_idx, size)
        #上
        if x > 0 and grid_copy[x-1][y] == 1:
            uf.merge(current_idx, current_idx - n)
        #下
        if x + 1 < m and grid_copy[x+1][y] == 1:
            uf.merge(current_idx + n, current_idx)
        #左
        if y > 0 and grid_copy[x][y - 1] == 1:
            uf.merge(current_idx, current_idx - 1)
        #右
        if y + 1 < n and grid_copy[x][y+1] == 1:
            uf.merge(current_idx + 1, current_idx)

        current_size = uf.get_size(size)
        res[i] = max(0, current_size - origal_size - 1)


    return res

# print(hitBricks2([[1,0,0,0],[1,1,1,0]], [[1,0]])) # [2]
# print(hitBricks2([[1,0,0,0],[1,1,0,0]], [[1,1],[1,0]])) # [0, 0]
# m = [[0,1,1,1,1,1],[1,1,1,1,1,1],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
# n = [[1,3],[3,5],[0,3],[3,3],[1,1],[4,2],[1,0],[3,0],[4,5],[2,1],[4,4],[4,0],[2,4],[2,5],[3,4],[0,5],[0,4],[3,2],[1,5],[4,1],[2,2],[0,2]]
# print(hitBricks2(m, n)) # [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1]

print(hitBricks([[1,0,0,0],[1,1,1,0]], [[1,0]])) # [2]
print(hitBricks([[1,0,0,0],[1,1,0,0]], [[1,1],[1,0]])) # [0, 0]
m = [[0,1,1,1,1,1],[1,1,1,1,1,1],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
n = [[1,3],[3,5],[0,3],[3,3],[1,1],[4,2],[1,0],[3,0],[4,5],[2,1],[4,4],[4,0],[2,4],[2,5],[3,4],[0,5],[0,4],[3,2],[1,5],[4,1],[2,2],[0,2]]
print(hitBricks(m, n)) # [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1]

print(hitBricks3([[1,0,0,0],[1,1,1,0]], [[1,0]])) # [2]
print(hitBricks3([[1,0,0,0],[1,1,0,0]], [[1,1],[1,0]])) # [0, 0]
m = [[0,1,1,1,1,1],[1,1,1,1,1,1],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
n = [[1,3],[3,5],[0,3],[3,3],[1,1],[4,2],[1,0],[3,0],[4,5],[2,1],[4,4],[4,0],[2,4],[2,5],[3,4],[0,5],[0,4],[3,2],[1,5],[4,1],[2,2],[0,2]]
print(hitBricks3(m, n)) # [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1]




