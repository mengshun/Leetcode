"""
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
"""

def merge(nums1, m, nums2, n):
    l1 = nums1[:m]
    l1.extend(nums2)
    l1.sort()
    for i in range(len(l1)):
        nums1[i] = l1[i]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)


def merge2(nums1, m, nums2, n):
    nums1_copy = nums1[:m]
    nums1[:] = []

    a = 0
    b = 0

    while a < m and b < n:
        if nums1_copy[a] < nums2[b]:
            nums1.append(nums1_copy[a])
            a += 1
        else:
            nums1.append(nums1_copy[b])
            b += 1
    if a < m:
        nums1[a+b:] = nums1_copy[a:]
    elif b < m:
        nums1[a+b:] = nums2[b:]



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge2(nums1, m, nums2, n)
print(nums1)

nums1 = [1, 0]
m = 1
nums2 = [1]
n = 1
merge2(nums1, m, nums2, n)
print(nums1)