"""
665. 非递减数列
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
"""

def checkPossibility(nums):
    # 要使数组 nums 变成一个非递减数列，数组中至多有多少个 i 满足 nums[i] > nums[i+1]
    n = len(nums)
    count = 0
    for i in range(1, n):
        x, y = nums[i-1], nums[i]
        if x > y:
            count += 1
            if count > 1:
                return False
            if i == 1 or nums[i-2] <= nums[i]:
                nums[i-1] = y
            else:
                nums[i] = x
    return True




print(checkPossibility([4, 2, 3]))
print(checkPossibility([4, 2, 1]))
print(checkPossibility([3, 4, 2, 3]))
print(checkPossibility([3, 4, 2, 5]))  # 425  1425   3425

"""
425  1425   3425
修改前面的, 后面的还没遍历 不要修改
当符合递减条件时, 计次直接加1
    当第一个元素和第二个元素产生递减时, 将第一个元素修改为第二个元素的值
    当第二个元素和第三个元素产生递减时, 并且 第一个元素不大于第三个元素时, 依然将第二个元素改为第三个元素
    反之将第三个元素改为 第二个元素
"""

def jiyi(nums):
    n = len(nums)
    count = 0
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            count += 1
            if count > 1:
                return False
            if i == 1 or nums[i-2] <= nums[i]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
    return True



















# 非递减
def fuxi(nums):
    n = len(nums)
    count = 0
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            count += 1
            if count > 1:
                return False
            if i == 1 or nums[i-2] <= nums[i]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
    return True



print(fuxi([3, 4, 2, 3]))



