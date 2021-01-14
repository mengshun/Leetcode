"""
1018 可被 5 整除的二进制前缀
给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。

返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。

示例 1：

输入：[0,1,1]
输出：[true,false,false]
解释：
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。

示例 2：

输入：[1,1,1]
输出：[false,false,false]

示例 3：

输入：[0,1,1,1,1,1]
输出：[true,false,false,false,true,false]

示例 4：

输入：[1,1,1,0,1]
输出：[false,false,false,false,false]
"""


def prefixesDivBy51(nums):
    res = []
    mode_list = []
    for i in range(len(nums)):
        v = nums[i]
        mode_res = 0
        if i == 0:
            mode_res = v % 5
        else:
            mode_res = (mode_list[-1] * 2 + v) % 5
        mode_list.append(mode_res)
        res.append(mode_res == 0)
    return res

def prefixesDivBy5(nums):
    res = []
    last_mode = 0
    for i in range(len(nums)):
        v = nums[i]
        if i == 0:
            last_mode = v % 5
        else:
            last_mode = (last_mode * 2 + v) % 5
        res.append(last_mode == 0)
    return res

nums = [0,1,1]
print(prefixesDivBy5(nums))
nums = [1,1,1]
print(prefixesDivBy5(nums))
nums = [0,1,1,1,1,1]
print(prefixesDivBy5(nums))
nums = [1,1,1,0,1]
print(prefixesDivBy5(nums))

"""
首先需要先发现规律, nums[i]表示第i位的输入值, 
设A[i]代表第i个二进制组合值, i 每增加 1, A[i] = A[i-1] * 2 + nums[i], 
由于随着位数的推移, 数值会越来越大, 而5是一个特殊数值, 取模不会影响下次的结果, 
所以记录上一次的取模值, 模只需要记录一个就可以了, 故使用一个变量就OK
"""