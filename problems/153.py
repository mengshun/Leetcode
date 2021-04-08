"""
153. 寻找旋转排序数组中的最小值 https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
"""

def findMin(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    left, right = 0, n-1
    mid = left
    while nums[left] >= nums[right]:
        if left + 1 == right:
            mid = right
            break
        mid = left + (right - left) // 2
        if nums[mid] >= nums[left]:
            left = mid
        elif nums[mid] <= nums[right]:
            right = mid
    return nums[mid]



nums = [3,4,5,1,2]
print(findMin(nums)) # 1
nums = [5,1,2,3,4]
print(findMin(nums)) # 1


print("\n 154. 寻找旋转排序数组中的最小值 II")
def findMinTwo(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    left, right = 0, n-1
    mid = left
    while nums[left] >= nums[right]:
        if left + 1 == right:
            mid = right
            break
        if nums[left] == nums[right]:
            left += 1
            mid = left
            continue
        mid = left + (right - left) // 2
        if nums[mid] >= nums[left]:
            left = mid
        elif nums[mid] <= nums[right]:
            right = mid
    return nums[mid]

nums = [3,4,5,1,2]
print(findMinTwo(nums)) # 1
nums = [5,1,2,3,4]
print(findMinTwo(nums)) # 1
nums = [2,2,2,0,1]
print(findMinTwo(nums)) # 0
print(findMinTwo([4,3,4,4,4])) # 3
print(findMinTwo([1,1])) # 1
