"""
1631 最小体力消耗路径
难度: 中等
"""

def minimumEffortPath(heights):
    if len(heights) == 0:
        return 0

    #行
    rows = len(heights)
    #列
    colums = len(heights[0])

    #并查集
    father = list(range(rows * colums))
    #用于统计分支大小, 小分支合并到大分支, 节省内存和时间
    size = [1] * len(father)
    #连线集合 [[x, y, abs(x-y)]] 第三个元素存两点差的绝对值
    edges = []

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

    for row in range(rows):
        for colum in range(colums):
            right_x, right_y = row, colum + 1
            if right_y < colums:
                val = abs(heights[right_x][right_y] - heights[row][colum])
                edges.append([row*colums+colum, right_x*colums+right_y, val])
            bottom_x, bottom_y = row + 1, colum
            if bottom_x < rows:
                val = abs(heights[bottom_x][bottom_y] - heights[row][colum])
                edges.append([row * colums + colum, bottom_x * colums + bottom_y, val])

    #对edges里面的 差值进行排序
    edges.sort(key= lambda val: val[-1])
    last_index = rows * colums - 1
    res = 0
    for x, y, val in edges:
        if find(0) == find(last_index):
            # 一旦发现已经连通  直接跳出循环
            break
        merge(x, y)
        res = max(res, val)

    return res




print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])) # 2
print(minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])) # 0
