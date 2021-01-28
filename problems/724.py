"""
724 寻找数组的中心索引
给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
"""

# 笨办法
def pivotIndex(nums):
    if len(nums) < 1:
        return -1
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

# 先求总和 如果两端相等 就等于说 2*单端和 + 当前值 = 总和
def pivotIndex2(nums):
    total = sum(nums)
    t = 0
    for i in range(len(nums)):
        if t * 2 + nums[i] == total:
            return i
        t += nums[i]
    return -1

    # total = sum(nums)
    # leftSum = 0
    # rightSum = 0
    # for i in range(len(nums)):
    #     leftSum += nums[i]
    #     rightSum = total - leftSum + nums[i]
    #     if leftSum == rightSum:
    #         return i
    # return -1

print(pivotIndex2([1, 7, 3, 6, 5, 6])) #3
print(pivotIndex2([1, 2, 3])) #-1
print(pivotIndex2([-1,-1,-1,0,1,1])) # 0
print(pivotIndex2([-1,-1,0,1,0,-1])) # 4
