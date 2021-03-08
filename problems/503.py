"""
503. 下一个更大的元素
https://leetcode-cn.com/problems/next-greater-element-ii/
"""

def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(2 * n):
        cur = nums[i % n]
        while stack and nums[stack[-1]] < cur:
            res[stack.pop()] = cur
        stack.append(i % n)
    return res


print(nextGreaterElements([1,2,1])) # [2,-1,2]
print(nextGreaterElements([1,2,3,4,3])) # [2,3,4,-1,4]