"""
42 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""


def trap(height):
    n = len(height)
    if n < 3:
        return 0
    res = 0
    left = 0
    maxleft = height[left]
    right = n - 1
    maxright = height[right]
    res = 0

    while left < right:
        if maxleft < maxright:
            left += 1
            if maxleft < height[left]:
                maxleft = height[left]
            else:
                res += (maxleft - height[left])
        else:
            right -= 1
            if maxright < height[right]:
                maxright = height[right]
            else:
                res += (maxright - height[right])
    return res



print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6