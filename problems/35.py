"""
35. 搜索插入位置
"""

def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

def searchInsert2(nums, target):
    n = len(nums)
    left, right, ans = 0, n-1, n
    while left <= right:
        mid = ((right - left) >> 1) + left
        if target <= nums[mid]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans




print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))

print(searchInsert2([1,3,5,6], 5))
print(searchInsert2([1,3,5,6], 2))
print(searchInsert2([1,3,5,6], 7))
print(searchInsert2([1,3,5,6], 0))