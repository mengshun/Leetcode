"""
74. 搜索二微矩阵 https://leetcode-cn.com/problems/search-a-2d-matrix/
"""

# 一维 二分查找
def searchMatrix(matrix, target):
    # 基础 一维 二分查找
    m = len(matrix)
    n = len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = left + (right - left) // 2
        cur = matrix[mid // n][mid % n]
        if cur == target:
            return True
        elif target > cur:
            left = mid + 1
        elif target < cur:
            right = mid - 1
    return False

# 二维二分查找
def searchMatrixOther(matrix, target):
    # 右侧二分查找
    def right_bound(nums, t):
        left, right = 0, len(nums) # 左闭右开
        while left < right:
            mid = left + (right - left) // 2
            cur = nums[mid]
            if cur == t:
                left = mid + 1
            elif cur > target:
                right = mid
            elif cur < target:
                left = mid + 1
        return left - 1

    m = len(matrix)
    n = len(matrix[0])
    first_nums = [v[0] for v in matrix]
    row_idx = right_bound(first_nums, target)
    if row_idx < 0:
        return False
    column_idx = right_bound(matrix[row_idx], target)
    return matrix[row_idx][column_idx] == target





matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 16
print(matrix, searchMatrix(matrix, target))
print(matrix, searchMatrixOther(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(matrix, searchMatrix(matrix, target))
print(matrix, searchMatrixOther(matrix, target))



# 寻找一个数（基本的二分搜索）
print("寻找一个数（基本的二分搜索）")
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left) // 2
        # print(left, right, mid)
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
    return -1


nums = list(range(100))
print(binarySearch(nums, 2))
print(binarySearch(nums, 3))
print(binarySearch(nums, 4))
print(binarySearch(nums, 101))

print("寻找左侧边界的二分搜索")
def left_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        cur = nums[mid]
        if cur == target:
            right = mid
        elif cur < target:
            left = mid + 1
        else:
            right = mid
    return left

print(left_bound([1,2,3,4], 0))
print(left_bound([1,2,3,4], 5))
print(left_bound([1,2,2,2,2,3,4], 2))
print(left_bound([1,10,23], 16))

print("寻找右侧边界的二分查找")
#寻找右侧边界的二分查找

def right_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        cur = nums[mid]
        if cur == target:
            left = mid + 1
        elif cur > target:
            right = mid
        else:
            left = mid + 1
    return left - 1

print(right_bound([1,2,3,4], 0))
print(right_bound([1,2,3,4], 2))
print(right_bound([1,2,3,4], 10))
print(right_bound([1,2,2,2,2,3,4], 2))
print(right_bound([1,10,23], 16))
print(right_bound([1, 5, 10, 15], 0))




print("\n\n 240. 搜索二维矩阵 II")
""" https://leetcode-cn.com/problems/search-a-2d-matrix-ii/ """

def searchMatrixTwo(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    def findTarget(start, isVertical):
        left = start
        right = m-1 if isVertical else n-1
        while left <= right:
            mid = left + (right - left) // 2
            cur = matrix[mid][start] if isVertical else matrix[start][mid]
            if cur == target:
                return True
            elif cur > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    for i in range(min(m, n)):
        if findTarget(i, True) or findTarget(i, False):
            return True
    return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrixTwo(matrix, target))
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
print(searchMatrixTwo(matrix, target))


