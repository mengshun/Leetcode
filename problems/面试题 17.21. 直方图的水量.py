"""
面试题 17.21. 直方图的水量
https://leetcode-cn.com/problems/volume-of-histogram-lcci/
"""

def trap(height):
    if not height:
        return 0
    n = len(height)
    leftMax = [0] * n
    leftMax[0] = height[0]
    rightMax = [0] * n
    rightMax[-1] = height[-1]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], height[i])
        rightMax[-i-1] = max(rightMax[-i], height[-i-1])
    res = 0
    for i in range(1, n-1):
        res += max(0, min(leftMax[i-1], rightMax[i+1]) - height[i])
    return res


def otherTrap(height):
    if len(height) < 3:
        return 0
    res = 0
    n = len(height)
    left, right = 0, n-1
    lHeight, rHeight = 0, 0
    while left < right:
        if height[left] < height[right]:
            if height[left] < lHeight:
                res += lHeight - height[left]
            else:
                lHeight = height[left]
            left += 1
        else:
            if height[right] < rHeight:
                res += rHeight - height[right]
            else:
                rHeight = height[right]
            right -= 1
    return res





print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(otherTrap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([2,0,2])) # 6
print(otherTrap([2,0,2])) # 6