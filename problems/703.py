"""
703. 数据流中的第K大元素
"""

class KthLargest:

    def __init__(self, k: int, nums: [int]):
        t = [x for x in nums]
        t.sort(reverse=True)
        self.nums = t
        self.k = k

    def find(self, x, tmp):
        n = len(tmp)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if tmp[mid] == x:
                return mid
            elif tmp[mid] > x:
                left = mid + 1
            elif tmp[mid] < x:
                right = mid - 1
        return left


    def add(self, val: int) -> int:
        res = self.find(val, self.nums)
        self.nums.insert(res, val)
        return self.nums[self.k - 1]




obj = KthLargest(3, [4, 5, 8, 2])
obj.add(3);   # return 4
obj.add(5);   # return 5
obj.add(10);  # return 5
obj.add(9);   # return 8
obj.add(4);   # return 8

# print("=======")
#
# def find(x, tmp):
#     n = len(tmp)
#     left, right = 0, n-1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if tmp[mid] == x:
#             return mid
#         elif tmp[mid] > x:
#             right = mid - 1
#         elif tmp[mid] < x:
#             left = mid + 1
#     return left
#
# print(find(2, [1,2,2, 2, 5]))