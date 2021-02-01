"""
55. 跳跃游戏
"""

def canJump(nums):
    n = len(nums)
    if n < 2:
        return True
    max_end = 0
    for i, v in enumerate(nums):
        if i + v >= n-1:
            return True
        if v == 0 and max_end == i:
            return False
        max_end = max(max_end, i + v)
    return False

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))