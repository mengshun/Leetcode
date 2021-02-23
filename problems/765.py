"""
765. 情侣牵手
N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位

"""

def minSwapsCouples(row):
    n = len(row)  # 总人数
    N = n >> 1  # 情侣对数
    # 并查集
    parent = list(range(N))
    size = [1] * N

    # 查
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    # 并
    def merge(x, y):
        x, y = find(x), find(y)
        if x == y:
            return
        # 小树 向 大树靠
        if size[x] > size[y]:
            x, y = y, x
        # 大树 大小修改
        size[y] += size[x]
        # 合并
        parent[x] = y

    for i in range(N):
        # 获取相邻两项真正的组别
        x = row[2 * i] >> 1
        y = row[2 * i + 1] >> 1
        if x != y:
            merge(x, y)
    # 同一个组的 只统计一次
    groups = {}
    for i in range(N):
        x = find(i)
        if x not in groups:
            groups[x] = size[x]

    return sum(groups.values()) - len(groups)

# 贪心算法

def tanxin(row):
    n = len(row)
    res = 0
    for i in range(0, n-1, 2):
        if row[i] == row[i+1] ^ 1:
            # 是一对情侣 继续下次循环
            continue
        for j in range(i+1, n):
            if row[i] == row[j] ^ 1:
                row[i+1], row[j] = row[j], row[i+1]
                break
        res += 1
    return res



print(minSwapsCouples([0, 2, 1, 3])) # 1
print(tanxin([0, 2, 1, 3])) # 1
print(minSwapsCouples([3, 2, 0, 1])) # 0
print(tanxin([3, 2, 0, 1])) # 0
print(minSwapsCouples([9,12,2,10,11,0,13,6,4,5,3,8,1,7])) # 5
print(tanxin([9,12,2,10,11,0,13,6,4,5,3,8,1,7])) # 5


