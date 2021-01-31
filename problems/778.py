"""
778. 水位上升的泳池中游泳
在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？
"""
def swimInWater(grid):
    if len(grid) < 2:
        return 0
    N = len(grid)
    n = N * N
    #并查集
    father = list(range(n))
    size = [1] * len(father)

    def find(x):
        if x != father[x]:
            father[x] = find(father[x])
        return father[x]

    def merge(x, y):
        x, y = find(x), find(y)
        if x == y:
            return
        if size[x] > size[y]:
            x, y = y, x
        father[x] = y
        size[y] += size[x]

    edges = []
    for i in range(N):
        for j in range(N):
            #连接右方
            current = i * N + j
            right = current + 1
            if j + 1 < N:
                edges.append([current, right, max(grid[i][j], grid[i][j+1])])
            #连接下方
            bottom = current + N
            if i + 1 < N:
                edges.append([current, bottom, max(grid[i][j], grid[i + 1][j])])


    #排序
    edges.sort(key= lambda v: v[-1])

    res = 0
    last_idx = N * N - 1
    for x, y, d in edges:
        if find(0) == find(last_idx):
            break
        merge(x, y)
        res = max(res, d)
    return res




print(swimInWater([[0,2],[1,3]])) # 3
print(swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])) # 16