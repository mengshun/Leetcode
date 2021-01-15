"""
1203 项目管理
公司共有 n 个项目和  m 个小组，每个项目要不无人接手，要不就由 m 个小组之一负责。

group[i] 表示第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。
（项目和小组都是从零开始编号的）小组可能存在没有接手任何项目的情况。

请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：

同一小组的项目，排序后在列表中彼此相邻。
项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，
其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。
如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。
"""
import collections

# 项目数量 n   小组数量 m
def sortItems(n, m, group, beforeItems):

    #无组的项目编组
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1
    #对同一个组的 项目进行整理
    group_dict= {i:[] for i in range(m)}
    for i in range(len(group)):
        group_dict[group[i]].append(i)

    result_group = []
    for i in range(len(beforeItems)):
        v = beforeItems[i]
        if len(v) > 0:
            for j in v:
                front = group[j]
                behind = group[i]
                if front == behind:
                    #同一个组 对项目进行排序
                    cur_group_items = group_dict[front]
                    front = j
                    behind = i
                    f_idx = cur_group_items.index(front)
                    b_idx = cur_group_items.index(behind)
                    if f_idx > b_idx:
                        cur_group_items.pop(f_idx)
                        cur_group_items.insert(b_idx, front)
                else:
                    #不同组 对组进行排序
                    if behind not in result_group:
                        result_group.append(behind)
                    if front not in result_group:
                        index = result_group.index(behind)
                        result_group.insert(index, front)
                    else:
                        f_idx = result_group.index(front)
                        b_idx = result_group.index(behind)
                        if f_idx > b_idx:
                            result_group.pop(f_idx)
                            result_group.insert(b_idx, front)

    # #判定组是否还需要调整  如果还需要调整则认为是有冲突的 则无解决方案
    # for i in range(len(beforeItems)):
    #     v = beforeItems[i]
    #     if len(v) > 0:
    #         for j in v:
    #             front = group[j]
    #             behind = group[i]
    #             if front == behind:
    #                 #同一个组 对项目进行排序
    #                 cur_group_items = group_dict[front]
    #                 front = j
    #                 behind = i
    #                 f_idx = cur_group_items.index(front)
    #                 b_idx = cur_group_items.index(behind)
    #                 if f_idx > b_idx:
    #                     return []
    #             else:
    #                 #不同组 对组进行排序
    #                 if behind not in result_group:
    #                     result_group.append(behind)
    #                 if front not in result_group:
    #                     return []
    #                 else:
    #                     f_idx = result_group.index(front)
    #                     b_idx = result_group.index(behind)
    #                     if f_idx > b_idx:
    #                         return []
    #判断组 是否添加完成
    if len(result_group) != m:
        for g in range(m):
            if g not in result_group:
                result_group.append(g)

    res = []
    for v in result_group:
        res += group_dict[v]

    hash_map = {}
    for i, v in zip(range(len(res)), res):
        hash_map[v] = i

    for i in range(len(beforeItems)):
        cur_list = beforeItems[i]
        for v in cur_list:
            if hash_map[v] > hash_map[i]:
                return []

    return res

def otherSortItems(n, m, group, pres):

    # tools function —— 基于BFS排序（队列）
    def bfs(items, indegrees, neighbours):
        q = collections.deque()
        res = []
        for item in items:
            if indegrees[item] == 0:
                q.append(item)
        while q:
            tmp = q.popleft()
            res.append(tmp)
            for n in neighbours[tmp]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    q.append(n)

        return res

    # -------------------- 准备工作 --------------------#
    # 初始化需要的数据结构
    indegrees_inG = collections.defaultdict(int)  # 组内的入度
    indegrees_betG = collections.defaultdict(int)  # 组间的入度
    neighbours_inG = collections.defaultdict(list)  # 组内节点的依赖关系
    neighbours_betG = collections.defaultdict(list)  # 组间的依赖关系
    groups = collections.defaultdict(list)  # 记录各小组中的元素
    res = []  # 解决方案

    # 将所有没分组的节点单独分为一组方便后续组间排序,并记录各小组中的元素
    for item in range(n):
        if group[item] == -1:
            group[item] = m
            m += 1

        groups[group[item]].append(item)  # 记录各小组中的元素
    group_num = m  # 记录小组数

    # 根据边的两边节点是否在同一group中分别更新组间和组内的依赖关系和入度数
    for item in range(n):
        for pre in pres[item]:
            if group[item] == group[pre]:  # 若两节点同组，则更新组内节点的依赖关系
                indegrees_inG[item] += 1
                neighbours_inG[pre].append(item)
            else:  # 若两节点同组，则更新组间的依赖关系
                indegrees_betG[group[item]] += 1
                neighbours_betG[group[pre]].append(group[item])

    # -------------------- 排序工作 --------------------#
    # 执行组间排序，res_betG为组间排序返回值
    res_betG = bfs(list(range(group_num)), indegrees_betG, neighbours_betG)
    if len(res_betG) != group_num:
        return []  # 若间排序返回值长度与组数不等说明连组间的依赖都无法实现，故返回[]

    # 按照排好的组间排序依次对每个小组进行组内排序
    for i in res_betG:
        tmp_res = bfs(groups[i], indegrees_inG, neighbours_inG)  # 执行组内排序
        res += tmp_res

    return res if len(res) == n else []  # 若最终长度与item个数不等说明连组内依赖无法实现，故返回[]

#最终答案
def sortParagrams(n, m, group, beforeItems):

    def bfs(items, deep, neighours):
        queue = collections.deque()
        for item in items:
            if deep[item] == 0:
                queue.append(item)
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for v in neighours[cur]:
                deep[v] -= 1
                if deep[v] == 0:
                    queue.append(v)
        return res

    group_items = collections.defaultdict(list)
    #对 -1 组进行重新编组
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1
        group_items[group[i]].append(i)
    #编组后 组的数量
    group_num = m

    #初始化数据
    deep_in = collections.defaultdict(int) #组内入度
    neighours_in = collections.defaultdict(list) #组内依赖关系
    deep_group = collections.defaultdict(int) #组间入度
    neighours_group = collections.defaultdict(list) #组间依赖关系

    for i in range(n):
        for pre in beforeItems[i]:
            if group[i] == group[pre]: #同一个组
                deep_in[i] += 1
                neighours_in[pre].append(i)
            else: #不同组
                deep_group[group[i]] += 1
                neighours_group[group[pre]].append(group[i])

    #对组进行排序
    sorted_group = bfs(list(range(group_num)), deep_group, neighours_group)
    if len(sorted_group) != group_num:
        return []

    #开始添加 并对组内进行排序
    res = []
    for group_no in sorted_group:
        original = group_items[group_no]
        sorted_items = bfs(original, deep_in, neighours_in)
        if len(original) != len(sorted_items):
            return []
        res += sorted_items

    return res

print(sortItems(5, 5, [2,0,-1,3,0], [[2,1,3],[2,4],[],[],[]]))
print(otherSortItems(5, 5, [2,0,-1,3,0], [[2,1,3],[2,4],[],[],[]]))
print(sortParagrams(5, 5, [2,0,-1,3,0], [[2,1,3],[2,4],[],[],[]]))

print(sortItems(8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]]))
print(otherSortItems(8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]]))
print(sortParagrams(8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]]))

print(sortItems(8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]]))
print(otherSortItems(8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]]))
print(sortParagrams(8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]]))