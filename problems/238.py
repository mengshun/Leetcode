"""
238. 除自身以外数组的乘积
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积
"""

def productExceptSelf(nums):

    n = len(nums)
    res = [1] * n

    # i 左侧元素的乘积
    for i in range(1, n):
        res[i] = res[i-1] * nums[i-1]

    r = 1 # 右侧元素的乘积
    for i in range(n-1, -1, -1):
        res[i] = res[i] * r
        r *= nums[i]

    return res



    # # 有问题  有0时 有问题
    # n = len(nums)
    # if n < 1:
    #     return []
    # if n < 2:
    #     return [0]
    # cur = 1
    # for v in nums[1:]:
    #     cur *= v
    # res = [cur]
    # for i in range(1, n):
    #     cur = int(cur / nums[i] * nums[i-1])
    #     res.append(cur)
    # return res


print(productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(productExceptSelf([1,0,3,4])) # [24,12,8,6]