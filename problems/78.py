"""
78. 子集 https://leetcode-cn.com/problems/subsets/
"""

# 数组 算法
def subsets(nums):
    res = [[]]
    for v in nums:
        res += [x + [v] for x in res]
    return res

# 回溯
def subsetsOther(nums):
    res = []
    def backtrace(numbers, path):
        res.append(path)
        for i in range(len(numbers)):
            backtrace(numbers[i+1:], path + [numbers[i]])
    backtrace(nums, [])
    return res

nums = [1,2,3]
res = subsets(nums)
print(len(res), res)
res = subsetsOther(nums)
print(len(res), res)

nums = [0]
res = subsets(nums)
print(len(res), res)


print("\n90. 子集 II")

def subsetsWithDup(nums):
    nums = sorted(nums)
    res = []
    def backtrace(numbers, path):
        # if path not in res:
        res.append(path)
        for i in range(len(numbers)):
            # [1,2,2] 对于子集[1,2] 已经 选择了第一个 2, 再去选择第二个2 依然是[1,2] 就会重复 所以跳过此次循环
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            backtrace(numbers[i+1:], path + [numbers[i]])
    backtrace(nums, [])
    return res

nums = [1,2,2]
res = subsetsWithDup(nums)
print(len(res), res)

# nums = [1,1,1,2,2]
# res = subsetsWithDup(nums)
# print(len(res), res)


