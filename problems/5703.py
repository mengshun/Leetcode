"""
5703. 最大平均通过率
https://leetcode-cn.com/problems/maximum-average-pass-ratio/
"""
import heapq
def maxAverageRatio(classes, extraStudents) -> float:
    diff = lambda x, y: (x + 1) / (y + 1) - x / y
    hp = []
    res = 0
    for passNum, allNum in classes:
        res += passNum / allNum
        # python 只有小根堆 所以取负值 当拿到最小值的时候其实就拿到最大值了
        # 第一个元素就是 如果在当前班级插入一个通过的学生 增加的通过率
        hp.append((-diff(passNum, allNum), passNum, allNum))

    heapq.heapify(hp)
    # 针对额外的学生 一个一个的进行计算
    for _ in range(extraStudents):
        d, x, y = heapq.heappop(hp)
        res += -d
        heapq.heappush(hp, (-diff(x + 1, y + 1), x + 1, y + 1))

    return res / len(classes)



classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
print(maxAverageRatio(classes, extraStudents)) # 0.78333

classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
print(maxAverageRatio(classes, extraStudents)) # 0.53485