"""
33. 搜索旋转排序数组  https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
# 互不相同的元素
"""
def search(nums, target):
    n = len(nums)
    left, right = 0, n-1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        else:
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[n-1]:
                    left = mid + 1
                else:
                    right = mid - 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target)) # 4

nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target)) # -1

"""
81. 搜索旋转排序数组 II https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
元素可能会一样的
"""

def searchTwo(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        if nums[mid] == nums[left]:
            left += 1
            continue
        elif nums[mid] == nums[right]:
            right -= 1
            continue
        if nums[mid] > nums[left]:
           if nums[left] <= target < nums[mid]:
               right = mid - 1
           else:
               left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False



print(searchTwo([1,0,1,1,1], 0))
print(searchTwo([2,2,0,1,1,2], 2))
print(searchTwo([3, 1], 1))